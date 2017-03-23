from flask import Flask
from routes.user import main as user_routes

app = Flask(__name__)

app.secret_key = 'test for good'

app.register_blueprint(user_routes)

if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2000,
    )
    app.run(**config)
