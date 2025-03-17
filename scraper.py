import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def scrape_website(url):
    # Automatically manage ChromeDriver
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (optional)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    # Extract title as an example
    title = driver.title

    driver.quit()

    # Data to be saved
    scraped_data = {
        "title": title,
        "url": url
    }

    # Save to a JSON file
    with open("scraped_data.json", "w", encoding="utf-8") as json_file:
        json.dump(scraped_data, json_file, indent=4)

    return scraped_data
