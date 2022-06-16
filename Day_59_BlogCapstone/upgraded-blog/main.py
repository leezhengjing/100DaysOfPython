from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/ba374f453b0faea9ff86"
response = requests.get(blog_url)
data = response.json()


@app.route("/")
def index():
    return render_template("index.html", posts=data)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
