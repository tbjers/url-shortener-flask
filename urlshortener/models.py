import base58
import datetime
import spacy
from profanity_filter import ProfanityFilter
from sqlalchemy import desc
from sqlalchemy.event import listens_for

from .database import db

nlp = spacy.load("en_core_web_sm")
pf = ProfanityFilter(nlps={"en": nlp})
nlp.add_pipe(pf.spacy_component, last=True)


class UrlClick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey("url.id"), nullable=False)
    ip_address = db.Column(db.String(255))
    referrer = db.Column(db.String(255))
    when = db.Column(db.DateTime)

    def __repr__(self):
        return "<UrlClick {}".format(self.id)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    public = db.Column(db.Boolean, default=False, nullable=False)
    hits = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.datetime.today)
    updated = db.Column(db.DateTime)

    clicks = db.relationship("UrlClick", backref="url")

    def _get_clean_id(self, id):
        doc = nlp(base58.b58encode_int(id).decode("utf-8"))
        if doc._.is_profane:
            return self._get_clean_id(id + 1)
        return id

    def _generate_hash(self):
        latest = self.query.order_by(desc(Url.id)).first()
        max_id = 1
        if latest != None:
            max_id = latest.id + 1
        max_id = self._get_clean_id(max_id)
        self.id = max_id
        self.hash = base58.b58encode_int(max_id).decode("utf-8")

    def __repr__(self):
        return "<Url {}>".format(self.hash)


@listens_for(Url, "before_insert")
def _generate_hash(mapper, connect, self):
    self._generate_hash()
