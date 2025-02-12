from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/ban_check/<uid>', methods=['GET'])
def ban_check(uid):
    url = f"https://ff.garena.com/api/antihack/check_banned?lang=en&uid={uid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "authority": "ff.garena.com",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "referer": "https://ff.garena.com/en/support/",
        "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "B6FksShzIgjfrYImLpTsadjS86sddhFH"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return jsonify(response.json())
    except requests.exceptions.RequestException:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
