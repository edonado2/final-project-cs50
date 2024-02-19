import os
from flask import Flask, render_template
from helpers import make_api_call

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
api_key = os.getenv("TOKEN")

@app.route('/')
def home():
    genres_response = make_api_call("genre/movie/list?language=en")
    popular_response = make_api_call("discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc")
    if genres_response:
        genres = genres_response.get("genres", [])
    else:
        genres = []
        print("Failed to retrieve movie genres.")
        
    if popular_response:
        popular = popular_response["results"]
    else:
        popular = []
        print("Failed to retrieve popular movies.")   


    return render_template("index.html", genres=genres, popular=popular, api_key=api_key)

@app.route("/about")
def  about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/movies/<int:id>")
def get_movie(id):
    movie_details = make_api_call(f"movie/{id}?append_to_response=credits,videos&language=en")
    if "status_code" in movie_details:
        return f"Error getting movie details for {id}. Please try again later."
    else:
       return render_template("movie-detail.html", movie=movie_details)

if __name__ == "__main__":
    app.run(debug=False)
