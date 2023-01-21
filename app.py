import datetime

from flask import Flask
from flask_jwt_extended import JWTManager

from controllers.UserController import user_api

app = Flask(__name__)
app.register_blueprint(user_api, url_prefix = '/users')

jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
jwt.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
