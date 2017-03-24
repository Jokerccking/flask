# 1，拆分页面
# 1.1 todo页面：
#       欢迎你xxx
#       todolist

# 2，组织数据
#   todo:
#   id,uid,content,ct,ut，
#   u.todos()
#
#

# 3, 逻辑详情：
#       todo：成功进入todo
#       add：添加一个todo，
#       delete： 删除一个todo
#       update，更新一个todo

# 4, 实现代码，一点点补全

# 5，美化页面

# 6，交互细节

from flask import (
    render_template,
    redirect,
    url_for,
    Blueprint,
)
from routes.user import current_user

main = Blueprint('todo', __name__)


@main.route('/')
def todo():
    u = current_user()
    if u is None:
        return redirect(url_for('index.login'))
    return render_template('todo.html', u=u)
