from datetime import datetime
from models.models import Access
from extensions.extensions import db

def access_count():    
    data_atual = datetime.now().strftime('%Y-%m-%d')
    hora_atual = datetime.now().hour
    data = Access.query.filter_by(data=data_atual, hora=hora_atual).first()
    if not data:
        # --- Cria entrada com data,hora,access(1)
        dados = Access(data=data_atual, hora=hora_atual, access=1)

        db.session.add(dados)
        db.session.commit()
    else:
        data.access = int(data.access) + 1
        db.session.commit()

# def insert_form(nome,email,telefone):
#     form = Formulario(nome = nome, email = email,telefone = telefone)
#     db.session.add(form)
#     db.session.commit()