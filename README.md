
# 🪞 Mirrog

**Mirrog** is an open-source, privacy-first **multi-engine search frontend** built with **Flask + Python**.  
It provides a clean, responsive interface for **DuckDuckGo** and **Reddit**, complete with modern features like dark mode, pagination, and built-in webpage screenshots powered by Playwright.

---

## 🚀 Features

### 🌍 **Multi-Engine Search**
- 🦆 **DuckDuckGo HTML Search**
  - Uses the public endpoint `https://html.duckduckgo.com/html/`
  - Region, time, safe search, and site filters
  - Clean snippet extraction and term highlighting
- 👽 **Reddit Search**
  - Searches directly via `old.reddit.com`
  - Displays subreddit, post title, and content preview
  - Perfect for finding Reddit discussions and insights

---

### 💡 **Mirrog UI Enhancements**
- **Bootstrap 5**-based, responsive, and mobile-friendly
- 🌓 **Dark / Light mode** toggle (persistent between searches)
- 🧩 **Configurable filters** for region, safe search, and time
- 🔢 **Results per page setting** (10–50 results)
- 📸 **View Screenshot button** (uses Playwright to capture live webpage screenshots)
- ⚡ **Accurate pagination** with dynamic page-size support
- 🔎 **Highlighted search terms** and favicons for each result

---

### ⚙️ **Customization Ready**
- Extend with more engines (Google, Bing, YouTube, etc.)
- Modify search filters or UI easily
- Ideal base for privacy-focused search portals or meta-search apps

---

## 🧰 Requirements

- Python 3.8+
- Playwright for screenshots

**Install dependencies:**
```bash
pip install -r requirements.txt
playwright install chromium
````

**Dependencies:**

```
Flask
requests
beautifulsoup4
playwright
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/CalmhostAcct/mirrog.git
cd mirrog
pip install -r requirements.txt
playwright install chromium
python app.py
```

Then open:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🌐 Example Usage

Type your query and select your preferred search engine:

| Option               | Description                               |
| -------------------- | ----------------------------------------- |
| **Engine**           | Switch between DuckDuckGo 🦆 or Reddit 👽 |
| **Region**           | 🇺🇸 US, 🇬🇧 UK, 🇩🇪 DE, 🇫🇷 FR        |
| **Time**             | Past day, week, or month                  |
| **Safe search**      | On / Moderate / Off                       |
| **Results per page** | 10–50 customizable                        |
| **Site filter**      | Search within a specific site             |

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

## 📸 Screenshot Example

Each result includes a **📸 “View Screenshot”** button — click it to generate a real-time page preview captured by Playwright (Chromium-based).

---

## 📜 License

**Mirrog** is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

You are free to use, modify, and redistribute it under the same license.
Please preserve attribution to the original project.

---

## ❤️ Contributing

Contributions, issues, and pull requests are welcome!
Ideas for new features include:

* 🌈 Inline screenshot previews (modal display)
* 🖼️ Image and video search
* 🔄 Async loading and caching for faster performance
* ⚡ Persistent user preferences via cookies

---

### ✨ Author

**Calmhostacct and the Mirrog Project**
Built with ❤️ using Flask, Python, Bootstrap 5, and Playwright.

