from flask import Flask, render_template
from sqlalchemy.sql.sqltypes import String, Integer, TIMESTAMP, Boolean
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, BaseView
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/news_flask?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456'

db = SQLAlchemy(app)


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(200), nullable=False)
    content = db.Column(String(2000), nullable=False)
    news_type = db.Column(String(20), nullable=False)
    img_url = db.Column(String(200))
    author = db.Column(String(20))
    view_count = db.Column(Integer)
    create_at = db.Column(TIMESTAMP(True), server_default=func.now())
    updated_at = db.Column(TIMESTAMP(True))
    is_vaild = db.Column(Boolean)

    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    '''新闻首页'''
    news_list = News.query.filter_by(is_vaild=1)
    return render_template('index.html', news_list=news_list)


@app.route('/news/<name>/')
def news(name):
    '''新闻类别'''
    news_list = News.query.filter(News.news_type == name)
    return render_template('new-category.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    '''新闻详细内容'''
    new = News.query.get(pk)
    return render_template('news-detail.html', new=new)


class MyAdmin(BaseView):
    pass


admin = Admin(app, name=u'新闻管理中心')
admin.add_view(ModelView(News, db.session))

if __name__ == '__main__':
    app.run(debug=True)
