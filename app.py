from flask import Flask, request, jsonify, render_template
from scraper import scrape_website  # Ensure you have this function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    # Explicitly check Content-Type header
    if request.headers.get("Content-Type") != "application/json":
        return jsonify({"error": "Unsupported Media Type, please send JSON"}), 415

    try:
        data = request.get_json(force=True)  # Force ensures it parses JSON
        url = data.get("url")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        # Call scraper function
        scraped_data = scrape_website(url)

        # Save data to JSON file
        import json
        with open("scraped_data.json", "w") as f:
            json.dump(scraped_data, f, indent=4)

        return jsonify(scraped_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
