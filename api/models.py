from api import db

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))
    start_date = db.Column(db.DateTime)

    def __init__(self, title, url, start_date):
        self.title = title
        self.url = url
        self.start_date = start_date
