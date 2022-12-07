from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
GENDERIZE_ENDPOINT = "https://api.genderize.io?name="
AGIFY_ENDPOINT = "https://api.agify.io?name="
NATIONALIZE_ENDPOINT = "https://api.nationalize.io/?name="
COUNTRY_CODES_SHEET_ENDPOINT = "https://api.sheety.co/375eb1fef6b2da6ab4a8e11c94c5efc9/countryCodes/all"

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year)


@app.route("/guess/<name>")
def guess(name):
    response = requests.get(url=f"{GENDERIZE_ENDPOINT}{name}")
    data = response.json()
    gender = data["gender"]
    response = requests.get(url=f"{AGIFY_ENDPOINT}{name}")
    data = response.json()
    age = data["age"]
    response = requests.get(url=f"{NATIONALIZE_ENDPOINT}{name}")
    data = response.json()
    country_id = data["country"][0]["country_id"]
    response = requests.get(url=COUNTRY_CODES_SHEET_ENDPOINT)
    data = response.json()["all"]
    country_name = ""
    for country in data:
        if country["alpha2"] == country_id:
            country_name = country["name"]
        else:
            continue
    return render_template("guess.html", name=name, gender=gender, age=age, country_name=country_name)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/d71c6ad116ac61b8137b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
