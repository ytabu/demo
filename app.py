from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os
import re

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.route("/")
def index():
    return render_template("index.html", page_url=request.url)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        errors = {}
        if not name:
            errors["name"] = "お名前を入力してください。"
        if not email:
            errors["email"] = "メールアドレスを入力してください。"
        elif not EMAIL_RE.match(email):
            errors["email"] = "正しいメールアドレスの形式で入力してください。"
        if not message:
            errors["message"] = "お問い合わせ内容を入力してください。"

        if errors:
            return render_template(
                "contact.html",
                errors=errors,
                form={"name": name, "email": email, "message": message},
            )

        flash("お問い合わせを送信しました。ありがとうございました！")
        return redirect(url_for("contact"))

    return render_template("contact.html", errors={}, form={})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
