from flask import Flask, render_template, url_for
import random
from flask_sqlalchemy import SQLAlchemy


# Setup/Config things
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ayaan/Desktop/flasktutorials/tut4/cool_db.db'
db = SQLAlchemy(app)

#Database stuff
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	text = db.Column(db.String(250))

#Routes
@app.route("/")
def home():
	random_num = random.randint(0, 100)
	names = ["Joe", "Bill", "Jane", "Wendy"]
	return render_template("index.html", cool_num=random_num, names=names)

@app.route("/about/")
def about():
	return render_template("about.html")

if __name__ == '__main__':
	app.run(debug=True)