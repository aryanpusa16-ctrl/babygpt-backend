from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Load API key from Render environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Root route
@app.route("/")
def home():
    return "Backend is working ✅"

# ✅ Chat route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_prompt = data.get("prompt", "")

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",   # safer choice than plain "gpt-4"
            messages=[
                {"role": "system", "content": "You are BabyGPT, a cute loving AI."},
                {"role": "user", "content": user_prompt}
            ]
        )

        return jsonify({"reply": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))