# Universal Web Scraper

## 📌 Overview

This is a **Universal Web Scraper** that allows users to extract data dynamically from any website. The user provides a URL through a web interface, and the scraped data is saved in JSON format.

## 🏰️ Folder Structure

```
web_scraping_project/
│── static/
│   └── styles.css         # Optional CSS for frontend styling
│── templates/
│   └── index.html         # Frontend HTML form
│── app.py                 # Flask server handling routes
│── scraper.py             # Web scraping logic using Selenium & Pandas
│── requirements.txt       # List of dependencies
│── scraped_data.json      # JSON file where scraped data is saved
│── README.md              # Project Documentation
│── screenshots/           # Folder containing UI and response screenshots
```

## 🚀 Features

✅ Accepts any website URL as input via UI or API  
✅ Scrapes dynamic web pages using Selenium  
✅ Saves extracted data in `scraped_data.json`  
✅ Flask-powered API with a user-friendly frontend  
✅ Supports JSON-based API calls for automated scraping

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS (Bootstrap optional)
- **Backend:** Python (Flask, Selenium, Pandas)
- **Data Storage:** JSON

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/pandeyaditya0002/Universal-Web-Scraper
cd web_scraping_project
```

### 2️⃣ Install Dependencies

Make sure you have **Python 3.8+** installed, then run:

```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up WebDriver (ChromeDriver)

- Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
- Extract it and place it in the project directory.

### 4️⃣ Run Flask Server

```sh
python app.py
```

> The app will be available at: `http://127.0.0.1:5000/`

---

## 📌 How to Use

### **1️⃣ Web Interface**

- Open `http://127.0.0.1:5000/` in your browser.
- Enter the website URL in the input field.
- Click **Scrape**.
- View extracted data in `scraped_data.json`.

![Web UI](./Screenshot%202025-03-17%20190526.png)

### **2️⃣ API Request (Using Postman or cURL)**

#### 📌 Endpoint: `/scrape`

**Request:**

```sh
curl -X POST http://127.0.0.1:5000/scrape \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```

**Response (Example JSON Output):**

```json
{
  "title": "Example Website",
  "url": "https://example.com",
  "data": {
    "headings": ["Welcome", "Latest News"],
    "links": ["/about", "/contact"]
  }
}
```

![Postman Response](screenshots/postman_response.png)

---

## 🛠 Troubleshooting

🔹 **Error: Unsupported Media Type (415)**

- Ensure you're sending JSON (`Content-Type: application/json`)
- Use Postman or cURL with `-H "Content-Type: application/json"`

🔹 **Error: Selenium WebDriver Issue**

- Check if ChromeDriver is installed and matches your Chrome version.

🔹 **Error: Flask Not Found**

- Ensure you installed dependencies: `pip install -r requirements.txt`

---

## 🌜 License

This project is open-source and free to use under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to contribute by improving the scraper or enhancing the UI.

---

### 🚀 Happy Scraping!

