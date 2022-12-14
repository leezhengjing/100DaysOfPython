from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import os
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy(app)
movie_api_key = os.environ["MOVIE_API_KEY"]
movie_search_url = "https://api.themoviedb.org/3/search/movie?api_key="
movie_details_url = "https://api.themoviedb.org/3/movie/"
movie_image_url = "https://image.tmdb.org/t/p/w500/"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Movie: {self.title}>'


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
# )
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template  ("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("movie_id")
    movie_to_edit = Movie.query.get(movie_id)
    edit_form = RateMovieForm()
    if edit_form.validate_on_submit():
        movie_to_edit.rating = float(edit_form.rating.data)
        movie_to_edit.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        new_movie = Movie(title=add_form.title.data)
        print(new_movie)
        response = requests.get(url=f"https://api.themoviedb.org/3/search/movie?api_key={movie_api_key}"
                                    f"&query={new_movie.title}")
        data = response.json()["results"]
        print(data)
        return render_template("select.html", data=data)
    return render_template("add.html", form=add_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/find")
def find_movie():
    movie_id = request.args.get("movie_id")
    response = requests.get(url=f"{movie_details_url}{movie_id}?api_key={movie_api_key}")
    data = response.json()
    title = data["title"]
    img_url = f"{movie_image_url}{data['poster_path']}"
    year = data["release_date"][:4]
    description = data["overview"]
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        img_url=img_url,
    )
    db.session.add(new_movie)
    db.session.commit()
    movie_in_database = Movie.query.filter_by(title=title).first()
    movie_in_database_id = movie_in_database.id
    return redirect(url_for('edit', movie_id=movie_in_database_id))


if __name__ == '__main__':
    app.run(debug=True)
