from flask import Blueprint, render_template

bp = Blueprint('services', __name__, url_prefix='/services')

@bp.route('/')
def serv():
    return render_template('services.html')


