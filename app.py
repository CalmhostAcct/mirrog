from flask import Flask, render_template_string, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote, urlencode
import re

app = Flask(__name__)

# ===============================
# HTML TEMPLATE WITH BOOTSTRAP 5
# ===============================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" data-bs-theme="{{ 'dark' if dark_mode else 'light' }}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mirrog</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body class="bg-body-secondary">
<div class="container py-5">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1 class="fw-bold">🔍 Mirrog</h1>
        <form method="GET" action="/" class="d-flex gap-2">
            <input type="hidden" name="dark" value="{{ 'off' if dark_mode else 'on' }}">
            <button class="btn btn-outline-secondary btn-sm">Toggle {{ 'Light' if dark_mode else 'Dark' }}</button>
        </form>
    </div>

    <form method="GET" action="/" class="mb-4">
        <div class="input-group mb-2">
            <input type="text" class="form-control" name="q" placeholder="Enter search query..." value="{{ query or '' }}" required>
            <button class="btn btn-primary" type="submit">Search</button>
        </div>
        <div class="d-flex gap-2 flex-wrap">
            <select name="region" class="form-select form-select-sm w-auto">
                <option value="">🌐 All regions</option>
                <option value="us-en" {% if region == 'us-en' %}selected{% endif %}>🇺🇸 US</option>
                <option value="uk-en" {% if region == 'uk-en' %}selected{% endif %}>🇬🇧 UK</option>
                <option value="de-de" {% if region == 'de-de' %}selected{% endif %}>🇩🇪 Germany</option>
                <option value="fr-fr" {% if region == 'fr-fr' %}selected{% endif %}>🇫🇷 France</option>
            </select>
            <select name="time" class="form-select form-select-sm w-auto">
                <option value="">⏱ Any time</option>
                <option value="d" {% if time == 'd' %}selected{% endif %}>Past Day</option>
                <option value="w" {% if time == 'w' %}selected{% endif %}>Past Week</option>
                <option value="m" {% if time == 'm' %}selected{% endif %}>Past Month</option>
            </select>
            <select name="safe" class="form-select form-select-sm w-auto">
                <option value="moderate" {% if safe == 'moderate' %}selected{% endif %}>🧩 Moderate</option>
                <option value="off" {% if safe == 'off' %}selected{% endif %}>🚫 Off</option>
                <option value="on" {% if safe == 'on' %}selected{% endif %}>✅ On</option>
            </select>
            <input type="text" name="site" class="form-control form-control-sm w-auto" placeholder="Site (optional)" value="{{ site or '' }}">
        </div>
    </form>

    {% if results %}
        <div class="mb-4">
            <p class="text-muted">Showing {{ results|length }} results for <strong>{{ query }}</strong></p>
        </div>
        {% for r in results %}
            <div class="card mb-3 shadow-sm">
                <div class="card-body">
                    <div class="d-flex align-items-center gap-2 mb-2">
                        <img src="https://www.google.com/s2/favicons?domain={{ r.url }}" width="16" height="16" alt="">
                        <h5 class="card-title mb-0">
                            {{ loop.index + page * 30 }}.
                            <a href="{{ r.url }}" target="_blank">{{ r.title|safe }}</a>
                        </h5>
                    </div>
                    <p class="card-text small">{{ r.snippet|safe }}</p>
                    <a href="{{ r.url }}" class="small text-muted">{{ r.url }}</a>
                </div>
            </div>
        {% endfor %}
        <div class="text-center d-flex justify-content-between">
            {% if page > 0 %}
                <a href="?{{ prev_page }}" class="btn btn-outline-secondary">← Previous</a>
            {% else %}
                <span></span>
            {% endif %}
            {% if next_page %}
                <a href="?{{ next_page }}" class="btn btn-outline-primary">Next →</a>
            {% endif %}
        </div>
    {% elif query %}
        <p class="text-muted">No results found.</p>
    {% endif %}
</div>
</body>
</html>
"""

# =========================================
# Scraper with DuckDuckGo HTML features
# =========================================
def scrape_duckduckgo(search_query, region="", time="", safe="moderate", site="", start=0):
    base_url = "https://html.duckduckgo.com/html/"
    q = f"{search_query} site:{site}" if site else search_query

    params = {
        "q": q,
        "kl": region,        # region
        "df": time,          # date filter
        "kp": {"on": -1, "off": 1}.get(safe, 0),  # safe search
        "s": start,          # correct pagination offset (30 per page)
    }

    response = requests.get(base_url, params=params, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for result in soup.find_all("div", class_="result"):
        title_tag = result.find("a", class_="result__a")
        snippet_tag = result.find("a", class_="result__snippet")

        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag.get("href")
            parsed = urlparse(link)
            query = parse_qs(parsed.query)
            if "uddg" in query:
                link = unquote(query['uddg'][0])
            snippet = snippet_tag.get_text(" ", strip=True) if snippet_tag else ""
            results.append({
                "title": highlight_terms(title, search_query),
                "url": link,
                "snippet": highlight_terms(snippet, search_query)
            })
    return results


def highlight_terms(text, query):
    """Highlight search terms inside snippets"""
    if not text or not query:
        return text
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", text)

# =========================================
# Flask routes
# =========================================
@app.route("/", methods=["GET"])
def index():
    query = request.args.get("q", "")
    region = request.args.get("region", "")
    time = request.args.get("time", "")
    safe = request.args.get("safe", "moderate")
    site = request.args.get("site", "")
    dark_mode = request.args.get("dark") == "on"
    page = int(request.args.get("page", 0))
    start = page * 30  # <-- FIXED pagination offset

    results = scrape_duckduckgo(query, region, time, safe, site, start) if query else None

    # pagination controls
    next_page_params = request.args.to_dict()
    next_page_params["page"] = page + 1
    next_page = urlencode(next_page_params) if query else None

    prev_page_params = request.args.to_dict()
    if page > 0:
        prev_page_params["page"] = page - 1
    prev_page = urlencode(prev_page_params) if page > 0 else None

    return render_template_string(
        HTML_TEMPLATE,
        results=results,
        query=query,
        region=region,
        time=time,
        safe=safe,
        site=site,
        dark_mode=dark_mode,
        next_page=next_page,
        prev_page=prev_page,
        page=page
    )

if __name__ == "__main__":
    app.run(debug=True)
