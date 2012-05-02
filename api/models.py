from api import db

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))
    start_date = db.Column(db.DateTime)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    venue = db.relationship('Venue',
        db.backref('show', lazy='dynamic'))
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    source = db.relationship('Source',
        db.backref('source', lazy='dynamic'))

    def __init__(self, title, url, start_date):
        self.title = title
        self.url = url
        self.start_date = start_date

    def save(self):
        db.session.add(self)
        db.session.commit()

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    url = db.Column(db.String(255))
    addr1 = db.Column(db.String(255))
    addr2 = db.Column(db.String(255))
    city = db.Column(db.String(150))
    state = db.Column(db.String(150))
    zip = db.Column(db.String(9))
    def save(self):
        db.session.add(self)
        db.session.commit()


class Source(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    url = db.Column(db.String(255))
    api_data = db.Column(db.Text)
    def save(self):
        db.session.add(self)
        db.session.commit()


