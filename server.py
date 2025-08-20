from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Use your sk-proj key (keep it safe here, not in the iOS app)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_prompt = data.get("prompt", "")

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are BabyGPT, a cute loving AI."},
            {"role": "user", "content": user_prompt}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})

#if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)