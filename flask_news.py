# coding=UTF-8
from flask_sqlalchemy import SQLAlchemy

from flask import render_template
from flask import Flask
from wsgiref.simple_server import make_server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:011022@localhost:3306/news'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class News(db.Model):
    """ 新闻模型 """
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(20))
    view_count = db.Column(db.Integer)
    is_valid = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime)

    # def __repr__(self):
    #     return '<News %r>' % self.title
    #


@app.route("/")
def index():
    '''新闻首页'''
    news_list = News.query.all()
    return render_template("index.html", news_list=news_list)


@app.route("/cat/<name>/")
def cat(name):
    '''新闻的类别'''
    # 查询类别为name的新闻数据
    return render_template("cat.html", name=name)


@app.route("/detail/<int:pk>/")
def detail(pk):
    '''新闻的类别'''
    # 查询类别为name的新闻数据
    return render_template("detail.html", pk=pk)


if __name__ == "__main__":
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run(debug=True)
