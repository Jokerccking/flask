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

import json

main = Blueprint('blog_api', __name__)