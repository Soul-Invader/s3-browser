from flask import Blueprint, request, jsonify
from utils.aws_client import get_s3_client, list_buckets
from models import Account
from utils.encryption import decrypt

bp = Blueprint('s3_routes', __name__, url_prefix='/s3')

@bp.route('/list_buckets', methods=['GET'])
def list_s3_buckets():
    account_id = request.args.get('account_id')
    account = Account.query.get(account_id)

    if account:
        # Decrypt the AWS credentials
        access_key = decrypt(account.access_key)
        secret_key = decrypt(account.secret_key)

        # Get S3 client using decrypted credentials
        s3_client = get_s3_client(access_key, secret_key)
        
        # List S3 buckets
        buckets = list_buckets(s3_client)
        return jsonify([bucket['Name'] for bucket in buckets])
    else:
        return jsonify({"error": "Account not found"}), 404
