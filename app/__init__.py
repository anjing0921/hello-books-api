from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
def create_app(test_config=None):
    app = Flask(__name__)


    from .models.books import Book
    from .models.authors import Author

    from .routes.route_books import books_bp
    app.register_blueprint(books_bp)

    return app