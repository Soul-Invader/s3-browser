from flask import Flask
from config import Config
from flask_migrate import Migrate
from db import db  # Import db from db.py

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database with app
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import routes after initializing the app and db
from routes import account_routes, s3_routes

# Register Blueprints for routes
app.register_blueprint(account_routes.bp)
app.register_blueprint(s3_routes.bp)

if __name__ == "__main__":
    app.run(debug=True)
