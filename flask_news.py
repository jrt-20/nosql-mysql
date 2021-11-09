# coding=UTF-8
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from flask import render_template, flash, url_for,redirect
from flask import Flask
from wsgiref.simple_server import make_server

from form import NewsForm

app = Flask(__name__)

# 数据库连接属性
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:011022@localhost:3306/news'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456' # 解决报错A secret key is required to use CSRF.

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
    """新闻首页"""
    news_list = News.query.all()
    return render_template("index.html", news_list=news_list)


@app.route("/cat/<name>/")
def cat(name):
    """新闻的类别"""
    # 查询类别为name的新闻数据
    return render_template("cat.html", name=name)


@app.route("/detail/<int:pk>/")
def detail(pk):
    """新闻的类别"""
    # 查询类别为name的新闻数据
    return render_template("detail.html", pk=pk)


@app.route('/admin/')
@app.route('/admin/<int:page>')
def admin(page=None):
    """ 后台管理首页 """
    if page is None:  # 如果没有传这个参数,默认为第一页
        page = 1
    page_data = News.query.paginate(page=page, per_page=5)
    return render_template("admin/index.html", page_data=page_data)


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    """ 新增新闻 """

    form = NewsForm()
    if form.validate_on_submit():
        n1 = News(
            title=form.title.data,
            content=form.content.data,
            img_url=form.img_url.data,
            news_type=form.news_type.data,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        db.session.add(n1)
        db.session.commit()
        flash("新增成功")
        return redirect(url_for('admin'))
    return render_template("admin/add.html",form=form)


@app.route('/admin/update/<int:pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 修改新闻 """
    return render_template("admin/update.html")


@app.route('/admin/delete/<int:pk>/', methods=['POST'])
def delete(pk):
    """ 删除新闻 """
    return 'yes'


if __name__ == "__main__":
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run(debug=True)
