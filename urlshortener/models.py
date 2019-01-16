import base58
from profanity_filter import ProfanityFilter
from sqlalchemy import desc
from sqlalchemy.event import listens_for

from .database import db

pf = ProfanityFilter()

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    public = db.Column(db.Boolean, default=False, nullable=False)

    clicks = db.relationship('UrlClick', lazy='select', backref=db.backref('url', lazy='joined'))

    def get_clean_id(self, id):
        if pf.is_clean(base58.b58encode_int(id).decode('utf-8')):
            return id
        else:
            return self.get_clean_id(id + 1)

    def generate_hash(self):
        latest = self.query.order_by(desc(Url.id)).first()
        max_id = 1
        if latest != None:
            max_id = latest.id + 1
        max_id = self.get_clean_id(max_id)
        self.id = max_id
        self.hash = base58.b58encode_int(max_id).decode('utf-8')
        return self.hash

    def __repr__(self):
        return '<Url {}>'.format(self.hash)

@listens_for(Url, 'before_insert')
def generate_hash(mapper, connect, self):
    self.generate_hash()

class UrlClick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
    ip_address = db.Column(db.String(255))
    referrer = db.Column(db.String(255))
    when = db.Column(db.DateTime())

    def __repr__(self):
        return '<UrlClick {}'.format(self.id)
