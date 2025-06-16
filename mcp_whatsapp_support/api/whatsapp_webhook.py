from flask import Flask, request

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    data = request.json
    # Process incoming WhatsApp messages
    print(f"Received message: {data}")
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
