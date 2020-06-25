from flask import Flask
import os
#, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_login import (LoginManager, current_user, login_required,
                        login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from itsdangerous import URLSafeTimedSerializer
from flask_redis import FlaskRedis
from .config import BaseConfig

db = SQLAlchemy()
r = FlaskRedis()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object(BaseConfig)

    os.system('python3 create_db.py')
    db.init_app(app)
    r.init_app(app)
    migrate.init_app(app, db)
    bootstrap = Bootstrap(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from .crud import crud as crud_blueprint
    app.register_blueprint(crud_blueprint)

    from .share import share as share_blueprint
    app.register_blueprint(share_blueprint)

    login_manager = LoginManager()
    #login_manager.login_view = ''
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app