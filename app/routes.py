from flask import Blueprint, jsonify, request, render_template
from app import db
from app.models import ContactUser

# Blueprint for adding user
add_user = Blueprint('add_user', __name__)

@add_user.route('/')
def index():
    return render_template('index2.html')

@add_user.route('/submit', methods=['POST'])
def add_user_route():
    print('HELLO')
    name = request.form.get('name')
    email = request.form.get('email')
    messages = request.form.get('messages')
    
    new_user = ContactUser(name=name, email=email, messages=messages)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Message added successfully"}), 201

# Blueprint for getting users
get_users = Blueprint('get_users', __name__)

@get_users.route('/get', methods=['GET'])
def get_users_route():
    users = ContactUser.query.all()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email,"messages": user.messages} for user in users])
