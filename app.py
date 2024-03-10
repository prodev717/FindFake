from flask import Flask,render_template,request
import json

app = Flask(__name__)

model = 0
with open("model.json","r") as f:
	model = json.load(f)

@app.route("/model")
def mod():
	return model

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/check",methods=["POST"])
def score():
	if request.method == "POST":
		return render_template("score.html",domain=request.form["domain"])

if __name__ == '__main__':
	app.run(debug=True,host="localhost",port=9000)