import functools
from flask import Blueprint, jsonify
from .db import db
from .entities import Item


app = Blueprint("examples", __name__, url_prefix="/examples")


def _response(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        response = func(*args, **kwargs)
        if response is None:
            return jsonify({})
        else:
            return response

    return wraps


@_response
@app.route("/add")
def add():
    with db.session() as session, session.begin():
        for n in range(3):
            session.add(Item(name=str(n)))


@_response
@app.route("/bulksave")
def bulksave():
    with db.session() as session, session.begin():
        def _bulksave():
            for item in session.query(Item):
                item.name = 'hoge'
                yield item
        session.bulk_save_objects(_bulksave())


@_response
@app.route("/bulksave2")
def bulksave2():
    with db.session() as session, session.begin():
        def _bulksave2():
            for n in range(3):
                yield Item(name=str(n))

        session.bulk_save_objects(_bulksave2())


@app.route("/test")
@_response
def test():
    with db.session() as session, session.begin():
        session.query(Item.id.in_([n for n in range(10000)])).all()
