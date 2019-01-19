from flask import (
    current_app, Blueprint, flash, g, render_template, redirect, request, url_for
)

bp = Blueprint('info', __name__, url_prefix='/info')

@bp.route('/about', methods=['GET'])
def about():
    """Show About

    :returns: A rendered template"""
    return render_template('info/about.html')
