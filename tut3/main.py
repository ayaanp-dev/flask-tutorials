from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

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