from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/d71c6ad116ac61b8137b"
    blog_response = requests.get(url=blog_url)
    blog_posts = blog_response.json()
    return render_template("index.html", posts=blog_posts)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    blog_url = "https://api.npoint.io/d71c6ad116ac61b8137b"
    blog_response = requests.get(url=blog_url)
    blog_posts = blog_response.json()
    return render_template("post.html", posts=blog_posts, blog_id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
