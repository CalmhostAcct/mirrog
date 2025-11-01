# 🪞 Mirrog

**Mirrog** is an open-source, lightweight **frontend for DuckDuckGo** written in **Flask + Python**.  
It provides a clean, fast, and responsive web interface for DuckDuckGo’s HTML search endpoint — ideal for building privacy-focused or custom search wrappers.

---

## 🚀 Features

- 🔍 **DuckDuckGo HTML Scraping**
  - Uses the public HTML endpoint (`https://html.duckduckgo.com/html/`)
  - Supports region, safe search, time filters, and site-specific queries

- 💡 **Mirrog UI Enhancements**
  - Clean **Bootstrap 5** interface
  - **Dark / Light mode** toggle
  - **Favicons**, query **highlighting**, and numbered results
  - **Pagination** (accurate `&s=$(page*30)` support)
  - Works entirely client-side — no JS dependencies required

- ⚙️ **Customization Ready**
  - Modify filters, HTML layout, or backend scraper easily
  - Great starting point for building your own search engine or meta-search proxy

---

## 🧰 Requirements

- Python 3.8+
- `pip install -r requirements.txt`

**Dependencies:**
```

Flask
requests
beautifulsoup4

````

---

## ▶️ Run Locally

```bash
git clone https://github.com/yourusername/mirrog.git
cd mirrog
pip install -r requirements.txt
python app.py
````

Then open:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌐 Example Usage

Type your search query, apply filters, and view results instantly.

**Supports:**

* Region: 🇺🇸 US, 🇬🇧 UK, 🇩🇪 DE, 🇫🇷 FR
* Safe search: On / Off / Moderate
* Time: Day / Week / Month
* Site filter: `site:example.com`

---

## 🧱 Project Structure

```
mirrog/
│
├── app.py                 # Main Flask app
├── README.md              # This file
├── requirements.txt       # Python dependencies
└── LICENSE                # GPL-3.0 license
```

---

## 📜 License

**Mirrog** is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

You are free to use, modify, and redistribute it under the same license.
Please preserve attribution to the original project.

---

## ❤️ Contributing

Contributions, issues, and pull requests are welcome!
If you have ideas to improve Mirrog (like caching, async requests, or UI themes), open an issue or submit a PR.

---

### ✨ Author

**Calmhostacct and the Mirrog Project** — Built with ❤️ using Flask, Python, and Bootstrap 5.
