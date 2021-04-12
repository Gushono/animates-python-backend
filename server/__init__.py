import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from configurations.authenticator import verify_auth
from configurations.enviroment_variables import DATABASE_URL

db = SQLAlchemy()
ma = Marshmallow()


def start_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api("swagger.yaml", arguments={"host_with_port": f"127.0.0.1"})
    app.app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app.app)
    CORS(app.app)
    ma.init_app(app.app)
    app.app.before_request(verify_auth)
    return app
