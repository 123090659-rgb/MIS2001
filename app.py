from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Hands-on 1")


@app.route("/exercise1")
def exercise1():
    return render_template("exercise1.html", title="Exercise 1")


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    # host="0.0.0.0" makes the app reachable from other devices on the network
    app.run(host="0.0.0.0", port=8000, debug=True)
