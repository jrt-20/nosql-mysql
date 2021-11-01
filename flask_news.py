# coding=UTF-8
from flask import render_template
from flask import Flask
from wsgiref.simple_server import make_server

app = Flask(__name__)

@app.route("/")
def hello_world():
    '''新闻首页'''
    return render_template("index.html")

@app.route("/cat/<name>/")
def cat(name):
    '''新闻的类别'''
    # 查询类别为name的新闻数据
    return render_template("cat.html",name=name)

@app.route("/detail/<int:pk>/")
def detail(pk):
    '''新闻的类别'''
    # 查询类别为name的新闻数据
    return render_template("detail.html",pk=pk)

if __name__ == "__main__":
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run(debug=True)
