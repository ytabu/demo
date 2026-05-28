from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")


@app.route("/")
def index():
    return render_template("index.html", page_url=request.url)


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
