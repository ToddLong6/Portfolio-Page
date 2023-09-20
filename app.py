from flask import Flask, render_template, request, redirect, url_for


LIST_OF_PROJECT = []

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run()