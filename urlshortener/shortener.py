from flask import (
    current_app, Blueprint, flash, g, render_template, redirect, request, url_for
)

from .database import db
from .models import Url, UrlClick

bp = Blueprint('shortener', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    """Lists URLs

    :returns: A rendered template"""
    urls = Url.query.all()
    return render_template('shortener/index.html', urls=urls)

@bp.route('/', methods=['POST'])
def create():
    """Creates a new URL from input parameters

    :returns: A redirect"""
    if request.method == 'POST':
        url = request.form['url']
        title = request.form['title']
        public = False
        error = None

        if not title:
            error = 'Title required'

        if not url:
            error = 'URL required'

        if 'public' in request.form:
            public = True

        if error is not None:
            flash(error)
        else:
            item = Url(url=url, public=public, title=title)
            db.session.add(item)
            db.session.commit()
            current_app.logger.info('created URL {} with hash {}'.format(item.url, item.hash))
            return redirect(url_for('shortener.index'))
