import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from server.configurations.authenticator import verify_auth
from server.configurations.enviroment_variables import DATABASE_URL, HOST, PORT
from server.configurations.filters import before_request

db = SQLAlchemy()
ma = Marshmallow()


def start_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api("swagger.yaml", arguments={"host_with_port": f"{HOST}:{PORT}"})
    app.app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.app.before_request(before_request)
    db.init_app(app.app)
    CORS(app.app)
    ma.init_app(app.app)

    return app
