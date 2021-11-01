from flask import render_template
from flask import Flask
from wsgiref.simple_server import make_server

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run(debug=True)
