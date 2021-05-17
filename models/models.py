from flask_security import RoleMixin, UserMixin


from extensions.extensions import db
from . import IdMixin

roles_users_table = db.Table('roles_users',
  db.Column('user_id', db.Integer(), 
  db.ForeignKey('user.id')),
  db.Column('roles_id', db.Integer(), 
  db.ForeignKey('roles.id')))

class User(db.Model,  UserMixin):

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())
    roles = db.relationship('Roles', secondary=roles_users_table,
    backref='user', lazy=True)

    def __str__(self):
        return self.first_name

class Roles(db.Model, RoleMixin):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))

class Access(db.Model, IdMixin):

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'access'

    data = db.Column(db.Date)
    hora = db.Column(db.Integer)
    access = db.Column(db.Integer)
    pagina = db.Column(db.String(100))

    def __str__(self):
        return self.access


class Formulario(db.Model, IdMixin):

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'formulario'

    email = db.Column(db.String(255))

    def __str__(self):
        return self.email




class SiteChanges(db.Model, IdMixin):

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'site_changes'

    name = db.Column(db.String(255))
    background_color = db.Column(db.String(255))
    headline_text = db.Column(db.String(255))
    headline_subtitle = db.Column(db.String(255))
    button_text = db.Column(db.String(255))
    who_i_am_text = db.Column(db.String(255))
    enterprise_name = db.Column(db.String(255))
    first_image = db.Column(db.String(255))
    second_image = db.Column(db.String(255))

    def __str__(self):
        return self.name

