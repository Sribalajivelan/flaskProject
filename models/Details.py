from MongoConfig import db


class Detail(db.Document):
    name = db.StringField(default=None)
    dept = db.StringField(default=None)
