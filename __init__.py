from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///test.db'
    db = SQLAlchemy(app)

    db.init_app(index)

    # blueprint for authentication routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .index import index as main_blueprint
    app.register_blueprint(main_blueprint)

    return app