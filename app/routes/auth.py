from flask import Blueprint
from app.controllers.auth_controller import login, register, logout

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/logout', methods=['POST'])(logout)
