from flask import Blueprint

main = Blueprint('statics', __name__)


@main.route('/img/<file>')
def img(file):
    path = 'statics/img/' + file
    body = b''
    with open(path, 'rb') as f:
        body += f.read()
    return body


@main.route('/css/<file>')
def css(file):
    path = 'statics/css/' + file
    body = b''
    with open(path, 'rb') as f:
        body += f.read()
    return body


@main.route('/js/<file>')
def js(file):
    path = 'statics/js/' + file
    body = b''
    with open(path, 'rb') as f:
        body += f.read()
    return body
