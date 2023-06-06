from flask import Flask, render_template, request
import requests
import openai

app = Flask(__name__)

# ChatGPT API endpoint
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Set your OpenAI API credentials
API_KEY = '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'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        condition = request.form.get("condition")
        severity = request.form.get("severity")
        message = request.form.get("message")
        response = chat_with_chatgpt(condition, severity, message)
        return render_template("index.html", response=response)
    return render_template("index.html")

def chat_with_chatgpt(condition, severity, message):
    # Constructing the prompt based on selected condition and severity
    prompt = f"Condition: {condition}\nSeverity: {severity}\nMessage: {message}\n"
    
    # Constructing the payload for the ChatGPT API
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ]
    }
    
    # Sending the request to the ChatGPT API
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(API_ENDPOINT, json=payload, headers=headers)
    data = response.json()
    
    # Extracting the model's reply from the API response
    reply = data["choices"][0]["message"]["content"]
    
    return reply

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')














