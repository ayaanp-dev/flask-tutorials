from flask import Flask, render_template, url_for
import random
from flask_sqlalchemy import SQLAlchemy
from forms import PostForm


# Setup/Config things
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ayaan/Desktop/flasktutorials/tut4/cool_db.db'
app.config["SECRET_KEY"] = "thisismysecretkey"
db = SQLAlchemy(app)

#Database stuff
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	text = db.Column(db.String(250))

#Routes
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/postpost")
def post_post():
	form = PostForm()
	return render_template("post.html", form=form)

if __name__ == '__main__':
	app.run(debug=True)