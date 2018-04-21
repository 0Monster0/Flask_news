# http://flask-mongoengine.readthedocs.io/en/latest/

from flask import Flask, render_template, abort
from flask_mongoengine import MongoEngine
from datetime import datetime

app2 = Flask(__name__)
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app2.config['SECRET_KEY'] = '123456'
app2.config['MONGODB_SETTINGS'] = {
    'db': 'flask_news',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app2)


class News(db.Document):

    meta = {
        'collection': 'news',
        '_ordering_': ['-create_at']
    }

    title = db.StringField(required=True, max_length=20)
    content = db.StringField(required=True)
    news_type = db.StringField(required=True)
    img_url = db.StringField()
    is_valid = db.BooleanField(default=True)
    create_at = db.DateTimeField(default=datetime.now())
    update_at = db.DateTimeField()


@app2.route('/')
def index():
    '''新闻首页'''
    news_list = News.objects.filter(is_vaild=True)
    return render_template('index.html', news_list=news_list)


@app2.route('/news/<name>/')
def news(name):
    '''新闻类别'''
    news_list = News.objects.filter(is_vaild=True, news_type=name)
    if not news_list:
        abort(404)
    return render_template('new-category.html', name=name, news_list=news_list)


@app2.route('/detail/<int:pk>/')
def detail(pk):
    '''新闻详细内容'''
    new = News.objects.get(pk)
    if not new:
        abort(404)
    return render_template('news-detail.html', new=new)


if __name__ == '__main__':
    app2.run(debug=True)
