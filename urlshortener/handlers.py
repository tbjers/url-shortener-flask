from flask import render_template

def _page_not_found(e):
    return render_template('error_404.html'), 404

def init_handlers(app):
    app.register_error_handler(404, _page_not_found)
