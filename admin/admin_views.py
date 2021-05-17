from flask import redirect, url_for,request
from flask_admin.contrib.sqla import ModelView 
from flask_security import current_user
from flask_admin import BaseView, expose, helpers
from flask_admin.contrib.fileadmin import BaseFileAdmin, LocalFileStorage
from flask_admin.menu import MenuLink

from controllers.controllers import ( make_site_changes, render_content_to_site, 
        render_form_data, delete_images
        )

class UserModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)

    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))

    column_list = ['email', 'password']

class Personalizar(BaseView):
    @expose('/', methods=['GET','POST'])
    def index(self):
        if request.method == 'POST':
            make_site_changes()
            content = render_content_to_site()
            return self.render('/personalizar.html',**content)
        
        if request.method == 'GET':
            content = render_content_to_site()
            return self.render('/admin/personalizar.html',**content) 

    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)

class Grafico_de_acessos(BaseView):
    @expose('/')
    def grafico(self):        
        return self.render('/admin/dashboard.html')
    
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)

class FileAdmin(BaseFileAdmin):
    def __init__(self, base_path, *args, **kwargs):
        storage = LocalFileStorage(base_path)
        super(FileAdmin, self).__init__(*args, storage=storage, **kwargs)

    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)

class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return (current_user.is_active and
                current_user.is_authenticated)