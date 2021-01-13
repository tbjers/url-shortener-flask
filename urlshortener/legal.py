from flask import (
    current_app,
    Blueprint,
    flash,
    g,
    render_template,
    redirect,
    request,
    url_for,
)

bp = Blueprint("legal", __name__, url_prefix="/legal")


@bp.route("/privacy", methods=["GET"])
def privacy():
    """Show Privacy Policy

    :returns: A rendered template"""
    return render_template("legal/privacy.html")


@bp.route("/terms", methods=["GET"])
def terms():
    """Show Terms of Service

    :returns: A rendered template"""
    return render_template("legal/terms.html")
