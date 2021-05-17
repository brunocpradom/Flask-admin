# -*- coding: utf-8 -*-
# Python
import os

# Third
from app import app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell
from flask_script.commands import Clean, ShowUrls
from models.models import db

HERE = os.path.abspath(os.path.dirname(__file__))
migrate = Migrate(app, db)
manager = Manager(app)


def _make_context():
    """Return context dict for a shell session so you can access
    app, db, and the User model_pueri by default.
    """
    return {'app': app, 'db': db}


manager.add_command('server', Server(host="0.0.0.0", port=app.config['PORT']))
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('db', MigrateCommand)
manager.add_command("urls", ShowUrls())
manager.add_command("clean", Clean())


if __name__ == '__main__':
    manager.run()
