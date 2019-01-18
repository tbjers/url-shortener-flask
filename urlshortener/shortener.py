from bs4 import BeautifulSoup
import datetime
from flask import (
    current_app, Blueprint, flash, g, render_template, redirect, request, url_for
)
from sqlalchemy import desc
from urllib import request as url_request

from .database import db
from .models import Url, UrlClick

bp = Blueprint('shortener', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    """Lists URLs

    :returns: A rendered template"""
    urls = db.session.query(Url).order_by(desc(Url.hits)).limit(10)
    return render_template('shortener/index.html', urls=urls)

@bp.route('/', methods=['POST'])
def create():
    """Creates a new URL from input parameters

    :returns: A redirect"""
    if request.method == 'POST':
        url = request.form['url']
        public = False
        title = None
        error = None

        try:
            html = url_request.urlopen(url).read()
            html[:60]
            soup = BeautifulSoup(html, 'html.parser')
            og_title = soup.find('meta', property='og:title')
            current_app.logger.info('og:title={}, title={}'.format(og_title, soup.title))
            if og_title:
                title = og_title['content']
            else:
                title = soup.find('title').string
                current_app.logger.info('could not find og:title, defaulting to <title/>: {}'.format(title))
        except Exception as ex:
            error = 'Title could not be parsed from webpage'

        if not url:
            error = 'URL required'

        if 'public' in request.form:
            public = True

        if error is not None:
            flash(error)
            return redirect(url_for('shortener.index'))
        else:
            item = Url(url=url, public=public, title=title)
            db.session.add(item)
            db.session.commit()
            current_app.logger.info('created URL {} with hash {}'.format(item.url, item.hash))
            return redirect(url_for('shortener.info', hash=item.hash))

@bp.route('/<string:hash>', methods=['GET'])
def open_url(hash):
    current_app.logger.info('redirect to hash = {}'.format(hash))
    url = db.session.query(Url).filter_by(hash=hash).first_or_404()
    click = UrlClick(ip_address=request.remote_addr, referrer=request.referrer, when=datetime.datetime.today())
    url.hits = url.hits + 1
    url.updated = datetime.datetime.today()
    url.clicks.append(click)
    db.session.commit()
    return redirect(url.url)

@bp.route('/<string:hash>/info', methods=['GET'])
def info(hash):
    url = db.session.query(Url).filter_by(hash=hash).first_or_404()
    return render_template('shortener/info.html', url=url)
