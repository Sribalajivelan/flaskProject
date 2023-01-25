from mongo_config import db


class User(db.Document):
    name = db.StringField()
    email = db.StringField()
