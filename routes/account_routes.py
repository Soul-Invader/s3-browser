from flask import Blueprint, request, jsonify
from models import db, Account
from utils.encryption import encrypt, decrypt

bp = Blueprint('account_routes', __name__, url_prefix='/accounts')

@bp.route('/add', methods=['POST'])
def add_account():
    account_name = request.form['account_name']
    access_key = request.form['access_key']
    secret_key = request.form['secret_key']
    
    # Encrypt keys
    encrypted_access_key = encrypt(access_key)
    encrypted_secret_key = encrypt(secret_key)

    new_account = Account(
        account_name=account_name,
        access_key=encrypted_access_key,
        secret_key=encrypted_secret_key
    )
    
    db.session.add(new_account)
    db.session.commit()

    return jsonify({"message": "Account added successfully!"})

@bp.route('/list', methods=['GET'])
def list_accounts():
    accounts = Account.query.all()
    decrypted_accounts = []
    
    for account in accounts:
        decrypted_accounts.append({
            "account_name": account.account_name,
            "access_key": decrypt(account.access_key),
            "secret_key": decrypt(account.secret_key)
        })
    
    return jsonify(decrypted_accounts)
