from flask import Flask, render_template, url_for, request, redirect
import random
from flask_sqlalchemy import SQLAlchemy
from forms import PostForm
import os


# Setup/Config things
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
app.config["SECRET_KEY"] = "thisismysecretkey"
db = SQLAlchemy(app)

#Database stuff
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	text = db.Column(db.String(250))

if not os.path.exists("posts.db"):
	db.create_all()

#Routes
@app.route("/")
def home():
	posts = Post.query.all()
	return render_template("index.html", posts=posts)

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/postpost", methods=["GET", "POST"])
def post_post():
	form = PostForm()
	if request.method == "POST":
		if form.validate_on_submit():
			uname = form.nick.data
			text = form.text.data
			post = Post(username=uname, text=text)
			db.session.add(post)
			db.session.commit()
			return redirect("/")
		else:
			print("error, form isn't valid")
	return render_template("post.html", form=form)

if __name__ == '__main__':
	app.run(debug=True)