from flask import (
    jsonify,
    request,
    redirect,
    url_for,
    Blueprint,
)
from routes.user import current_user
from models.blog import Blog
from models.blog import Comment

main = Blueprint('blog_api', __name__)


@main.route('/all')
def ball():
    u = current_user()
    if u is None:
        return redirect(url_for('index.login'))
    bs = u.blogs()
    ms = []
    for b in bs:
        ms.append(b.to_dict())
    return jsonify(ms)


@main.route('/add', methods=['POST'])
def add():
    u = current_user()
    form = request.json
    uid = form.get('uid')
    if u is None or uid is None:
        return redirect(url_for('blog.blog'))
    b = Blog.new(form)
    return jsonify(b.to_dict())


@main.route('/delete/<int:bid>')
def delete(bid):
    u = current_user()
    if u is None:
        return redirect(url_for('blog.blog'))
    b = Blog.popi(bid)
    return jsonify(b.to_dict())


@main.route('/cmtadd', methods=['POST'])
def cmtadd():
    u = current_user()
    form = request.json
    bid = form.get('bid')
    if u is None or bid is None:
        return redirect(url_for('blog.blog'))
    form['um'] = u.username
    cmt = Comment.new(form)
    return jsonify(cmt.to_dict())


@main.route('/cmtdelete/<int:cid>')
def cmtdelete(cid):
    u = current_user()
    if u is None:
        return redirect(url_for('blog.blog'))
    cmt = Comment.pop(cid)
    return jsonify(cmt.to_dict())
