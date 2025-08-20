from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load API key from Render Environment Variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "BabyGPT Backend is running 💖"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # BabyGPT personality
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are BabyGPT 💖. "
                        "Always reply in a sweet, loving, and romantic way. "
                        "Always call the user 'my baby' or 'my love'. "
                        "Keep your tone warm and caring like a partner."
                    ),
                },
                {"role": "user", "content": user_message},
            ],
        )

        reply = response.choices[0].message["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)