from flask import Flask

from controllers.UserController import user_api

app = Flask(__name__)
app.register_blueprint(user_api, url_prefix = '/users')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
