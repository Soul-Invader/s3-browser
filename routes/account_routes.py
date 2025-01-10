from flask import Blueprint, request, jsonify
from models import db, Account
from utils.encryption import encrypt

account_bp = Blueprint('account', __name__)

@account_bp.route('/add', methods=['POST'])
def add_account():
    data = request.json
    name = data.get('name')
    access_key = data.get('access_key')
    secret_key = data.get('secret_key')

    if not name or not access_key or not secret_key:
        return jsonify({'error': 'All fields are required'}), 400

    # Encrypt the credentials
    encrypted_access_key = encrypt(access_key)
    encrypted_secret_key = encrypt(secret_key)

    account = Account(name=name, access_key=encrypted_access_key, secret_key=encrypted_secret_key)
    db.session.add(account)
    db.session.commit()

    return jsonify({'message': 'Account added successfully'}), 201
