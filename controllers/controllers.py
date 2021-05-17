import os
from flask import request,url_for

from models.models import SiteChanges, Formulario
from extensions.extensions import db

def make_site_changes():

    site_has_new_content =True
    new_values = SiteChanges.query.filter_by(name = 'new').first()
    if not new_values:
        site_has_new_content = False
        new_values = SiteChanges()
    new_values.name = 'new'
    new_values.background_color = request.form.get('color')
    new_values.headline_text = request.form.get('titulo')
    new_values.headline_subtitle = request.form.get('subtitulo')
    new_values.button_text = request.form.get('botao')
    new_values.who_i_am_text = request.form.get('quemeusou')
    new_values.enterprise_name = request.form.get('nomedaempresa')
    new_values.first_image = url_for(
        'static', filename ='images/' + request.form.get('imagem')
        )
    new_values.second_image = url_for(
        'static', filename ='images/' + request.form.get('imagem2')
    )
    if not site_has_new_content:
        db.session.add(new_values)
    db.session.commit()
    return True
    
def delete_images():
    site_vars=SiteChanges.query.filter_by(name='new').first()
    try:        
        file_to_remove = os.getcwd() + os.path.abspath(site_vars.first_image)
        os.remove(file_to_remove)
    except:
        pass
    try:
        file_to_remove_2 =os.getcwd() + os.path.abspath(site_vars.second_image)
        os.remove(file_to_remove_2)
    except:
        pass

    return True


def render_content_to_site():
    check =SiteChanges.query.filter_by(name = 'new').first()
    name = 'new' if check else 'default'

    vars = SiteChanges.query.filter_by(name = name).first()

    content = {}
    content['background_color'] = vars.background_color
    content['headline_text'] = vars.headline_text
    content['headline_subtitle'] = vars.headline_subtitle
    content['button_text'] = vars.button_text
    content['who_i_am_text'] = vars.who_i_am_text
    content['enterprise_name'] = vars.enterprise_name
    content['image'] = vars.first_image
    content['image2'] = vars.second_image
    return content


def render_form_data():
    email = request.form.get('email')
    if email:
        form = Formulario()
        form.email = email
        db.session.add(form)
        db.session.commit()
    
    return True