from flask import Flask
app = Flask(__name__)


@app.route("/192.168.0.82:5000")
def hello_world():
    return "hello world"


if __name__ == "__main__":
    app.debug = True
    app.run()