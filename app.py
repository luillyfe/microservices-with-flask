from flask import Flask

app = Flask(__name__)
print(__name__)

@app.route("/")
def welcome():
    return "Landing page"

app.run(port=5000)