from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
from routes.auth import auth_bp
from routes.secrets import secrets_bp
from routes.share import share_bp

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Rate limiter - max 100 requests per minute per IP
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["100 per minute"]
    )

    # Register all blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(secrets_bp)
    app.register_blueprint(share_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)