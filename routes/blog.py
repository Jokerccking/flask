# 1，拆分页面
# 1.1 blog页面：
#       欢迎你xxx
#       todolist

# 2，组织数据
#   blog:
#   id,uid,content,ct，
#   u.blogs(), comments()

#   Comment:
#   id, uid, bid, content , ct
#
#

# 3, 逻辑详情：
#       blog：成功进入blog
#       add：添加一个blog，
#       delete： 删除一个blog
#       update，更新一个blog

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

main = Blueprint('blog', __name__)
