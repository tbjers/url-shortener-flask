from .database import db

class Url(db.Model):
    hash = db.Column(db.String(255), primary_key=True)
    url = db.Column(db.String(255))
    title = db.Column(db.String(80), nullable=False)
    public = db.Column(db.Boolean, default=False, nullable=False)

    clicks = db.relationship('UrlClick', lazy='select', backref=db.backref('url', lazy='joined'))

    def __repr__(self):
        return '<Url {}>'.format(self.hash)

class UrlClick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_hash = db.Column(db.String(255), db.ForeignKey('url.hash'), nullable=False)
    ip_address = db.Column(db.String(255))
    referrer = db.Column(db.String(255))
    when = db.Column(db.DateTime())

    def __repr__(self):
        return '<UrlClick {}'.format(self.id)
