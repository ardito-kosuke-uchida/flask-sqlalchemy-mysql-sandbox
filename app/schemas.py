from flask import Blueprint, jsonify
from .db import db
from .entities import Item


app = Blueprint("schemas", __name__, url_prefix="/schemas")

@app.route("/reset")
def reset():
    db.drop_all()
    db.create_all()
    return jsonify({})

