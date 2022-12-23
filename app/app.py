from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.update(
        {
            "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://sample:secret@db/sample",
            "SQLALCHEMY_ECHO": True,
            "sqlalchemy_track_modifications": False,
        },
    )

    from .entities import db
    db.init_app(app)

    from .examples import app as examples
    app.register_blueprint(examples)

    from .schemas import app as schemas
    app.register_blueprint(schemas)

    return app
