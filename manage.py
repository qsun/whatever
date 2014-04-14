#!/usr/bin/python

from flask.ext.script import Manager

from app import app


manager = Manager(app)


@manager.command
def hello():
    print("Hello")


@manager.command
def create_db():
    from app import db
    db.Base.metadata.create_all(db.e)


if __name__ == '__main__':
    manager.run()
