from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db = SQLAlchemy(app)

# Import routes after initializing the app and db
from routes import account_routes, s3_routes

# Register Blueprints for routes
app.register_blueprint(account_routes.bp)
app.register_blueprint(s3_routes.bp)

if __name__ == "__main__":
    app.run(debug=True)
