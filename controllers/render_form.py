from models.models import Formulario
from extensions.extensions import db

def render_form():
    email = request.data.get('email')
    if email:
        form = Formulario()
        form.email = email
        db.session.add(form)
        db.session.commit()
    
    return True
