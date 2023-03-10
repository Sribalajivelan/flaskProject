import datetime

from flask import Flask
from flask_jwt_extended import JWTManager

from controllers.detail_controller import detail_api
from controllers.user_controller import user_api

app = Flask(__name__)
app.register_blueprint(user_api, url_prefix = '/users')
app.register_blueprint(detail_api, url_prefix = '/details')

jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'Your_Secret_Key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
jwt.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
