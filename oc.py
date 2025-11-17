from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    msgs = [
        "Welcome to OpenShift!",
        "Your Python app is running correctly.",
        "This is a multi-message response.",
        "Have a great day!"
    ]

    # Join multiple messages with new lines
    return "\n".join(msgs)

if __name__ == "__main__":
    print("Application starting...")
    app.run(host="0.0.0.0", port=8080)
