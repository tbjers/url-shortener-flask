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

    :returns: A rendered template"""
    if request.method == 'POST':
        url = request.form['url']
        title = request.form['title']
        public = request.form['public']
        error = None

        if not title:
            error = 'Title required'

        if not url:
            error = 'URL required'

        if not public:
            public = False
        else:
            public = True

        if error is not None:
            flash(error)
        else:
            item = Url(url=url, public=public, title=title)
            item.hash = item.generate_hash()
            current_app.logger.info(item.hash)
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('shortener.index'))
