from flask import Blueprint, jsonify, request, current_app
from models.user import User

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return {"error": "Missing required fields"}, 400

    if User.query.filter_by(email=email).first():
        return {"error": "Email already exists"}, 400

    new_user = User(name=name, email=email, password=password)
    db = current_app.extensions['sqlalchemy'].db
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user": new_user.to_dict()}), 201