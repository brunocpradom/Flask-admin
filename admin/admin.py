import os

from flask import url_for
from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import Admin
from werkzeug.utils import secure_filename
from flask_admin import helpers

from admin.admin_views import  (
    UserModelView, FileAdmin, Personalizar, Grafico_de_acessos,LogoutMenuLink
)
from models.models import User,SiteChanges, Formulario, Roles
from extensions.extensions import db

def init_admin(app):
    path = os.path.join(os.path.dirname(__file__), '../static/images')
    print(path)
    user_datastore = SQLAlchemyUserDatastore(db, User, Roles)
    security = Security(app, user_datastore)
    admin = Admin(
        app, name='microblog', base_template='my_master.html',template_mode='bootstrap4',
        )
    # admin.add_view(ModelView(User, db.session))
    # admin.add_view(ModelView(SiteChanges, db.session))
    admin.add_view(UserModelView(Formulario, db.session))
    admin.add_view(Personalizar())
    admin.add_view(Grafico_de_acessos())
    admin.add_view(FileAdmin(path,'/static/images/', name = 'Imagens'))
    admin.add_view(UserModelView(User, db.session))
    admin.add_link(LogoutMenuLink(name='Logout', category='', url="/logout"))
    # Add administrative views here

    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template = admin.base_template,
            admin_view = admin.index_view,
            get_url = url_for,
            h = helpers
        )
    return app

# @app.before_first_request
# def create_user():
#     user_datastore.create_user(email='admin', password='admin')
#     db.session.commit()