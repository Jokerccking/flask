from flask import (
    jsonify,
    request,
    redirect,
    url_for,
    Blueprint,
)
from routes.user import current_user
from models.todo import Todo

import json

main = Blueprint('todo_api', __name__)


@main.route('/all')
def tall():
    u = current_user()
    if u is None:
        return redirect(url_for('index.login'))
    tds = u.todos()
    ms = []
    for td in tds:
        t = td.to_dict()
        ms.append(t)
    return jsonify(ms)


@main.route('/add', methods=['POST'])
def add():
    u = current_user()
    form = request.form
    if u is None or form.get('uid') is None:
        return redirect(url_for('.tall'))
    td = Todo.new(form)
    return jsonify(td.to_dict())


@main.route('/delete')
def delete():
    u = current_user()
    form = json.loads(request.get_data())
    tdid = form().get('id')
    if u is None or tdid is None:
        return redirect('/todo')
    td = Todo.pop(int(tdid))
    return jsonify(td.to_dict())


@main.route('/update')
def update():
    u = current_user()
    form = json.loads(request.get_data())
    tdid = form.get('tid')
    if u is None or tdid is None:
        return redirect('/todo')
    td = Todo.find(int(tdid))
    utd = td.update(form.get('content'))
    return jsonify(utd.to_dict())
