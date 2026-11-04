from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Get your API key from OpenWeatherMap
API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", "London").strip()

    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            return jsonify({"error": "City not found"}), 404

        if response.status_code == 401:
            return jsonify({
                "error": "Invalid API key or API key not activated"
            }), 401

        response.raise_for_status()
        data = response.json()

        formatted = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }

        return jsonify(formatted), 200

    except requests.exceptions.Timeout:
        return jsonify({"error": "Weather API request timed out"}), 504

    except requests.exceptions.RequestException:
        return jsonify({"error": "Unable to fetch weather data"}), 502


if __name__ == "__main__":
    app.run(debug=True)