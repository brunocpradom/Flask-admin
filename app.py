import os

from flask import Flask, render_template, request, jsonify,redirect,url_for,flash

from controllers.controllers import ( make_site_changes, render_content_to_site, 
        render_form_data, delete_images
        )
from controllers.helpers import access_count
from controllers import dashboard
from models.models import User,SiteChanges, Formulario, Roles
from extensions.extensions import db
from admin.admin import init_admin

def create_app():
    app = Flask(__name__)
    app.config.from_object('extensions.config.LocalConfig')
    db.app = app
    db.init_app(app)
    app = init_admin(app)
    
    return app

app = create_app()

@app.route('/')
def index():
    access_count()
    content = render_content_to_site()
    return render_template('index.html', **content)

@app.route('/dashboard')
def grafico_de_acesso():
    content = dashboard.show_last_access()
    return render_template('grafico_de_acesso.html',**content)

@app.route('/reset_site',methods =['DELETE'])
def reset_site():
    # delete_images()   
    SiteChanges.query.filter_by(name='new').delete()
    db.session.commit()

    return jsonify(success=True)

@app.route('/render_form', methods = ['POST'])
def render_form():
    render_form_data()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug =True)