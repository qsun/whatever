from main import app
from flask import render_template, request, redirect, url_for
from models import Topic


@app.route('/')
@app.route('/p/<int:page>')
def index_page(page=0):
    items = Topic.recent(n=20, page=0)
    return render_template('index.html', items=items)


@app.route('/add')
def add_page():
    return render_template('add.html')


@app.route('/create', methods=["POST"])
def create_page():
    title = request.form['title']
    description = request.form['description']
    topic = Topic.create_topic(title, description)
    return redirect(url_for('topic_page', topic_id=topic.id))


@app.route('/topics/<int:topic_id>')
def topic_page(topic_id):
    topic = Topic.find_by_id(topic_id)
    if topic:
        return render_template('topic.html', topic=topic)
    else:
        return 'Page not found', 404


@app.route('/topics/<int:topic_id>', methods=["POST"])
def append_comment_page(topic_id):
    comment = request.form['comment']
    topic = Topic.find_by_id(topic_id)
    if topic:
        topic.append_comment(comment)
        return redirect(url_for('topic_page', topic_id=topic.id))
    return 'Page not found', 404
