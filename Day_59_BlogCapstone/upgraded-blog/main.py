from flask import Flask, render_template, request
import requests
import smtplib
import os

app = Flask(__name__)

blog_url = "https://api.npoint.io/ba374f453b0faea9ff86"
response = requests.get(blog_url)
data = response.json()
my_gmail = os.environ["MY_GMAIL"]
my_ymail = os.environ["MY_YMAIL"]
yahoo_password = os.environ["YAHOO_PASSWORD"]

@app.route("/")
def index():
    return render_template("index.html", posts=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", request_method=request.method)
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_ymail, password=yahoo_password)
            connection.sendmail(
                from_addr=my_ymail,
                to_addrs=my_gmail,
                msg=f"Subject:Blog Contact\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )
        return render_template("contact.html", request_method=request.method)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post in data:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
