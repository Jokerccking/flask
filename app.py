from flask import Flask
from routes.user import main as user_routes
from routes.statics import main as statics_routes
from routes.todo import main as todo_routes
from routes.todo_api import main as todo_api_routes

app = Flask(__name__)

app.secret_key = 'test for good'

app.register_blueprint(user_routes)
app.register_blueprint(statics_routes, url_prefix='/statics')
app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(todo_api_routes, url_prefix='/todo/api')

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
