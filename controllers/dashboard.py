from datetime import datetime, timedelta
import collections

from sqlalchemy import func

from extensions.extensions import db
from models.models import Access

def last_30_days_access():
#!--Calculando quantidade de acessos nos últimos 30 dias
    date_today = datetime.today()
    last_month = datetime.today() - timedelta(days = 30)

    access = dict(db.session.query(Access.hora, func.sum(Access.access)).filter(Access.data >= last_month, Access.data <= date_today).group_by('hora').all())
    access = collections.OrderedDict(sorted(access.items()))
    
    access_hour_thirty_days = []
    access_qtd_thirty_days = []
    for key, value in access.items():
        access_hour_thirty_days.append(str(key) + 'h')
        access_qtd_thirty_days.append(value)
    
    return access_hour_thirty_days, access_qtd_thirty_days

def last_7_days_access():
    #!-- Calculando quantidade de acessos nos últimos 7 dias
    date_today = datetime.today()
    last_seven_days = datetime.today() - timedelta(days=7)

    access = dict(db.session.query(Access.hora, func.sum(Access.access)).filter_by().filter(Access.data >= last_seven_days, Access.data <= date_today).group_by('hora').all())
    access = collections.OrderedDict(sorted(access.items()))
    
    access_hour_seven_days = []
    access_qtd_seven_days = []
    for key, value in access.items():
        access_hour_seven_days.append(str(key) + 'h')
        access_qtd_seven_days.append(value)
    
    return access_hour_seven_days, access_qtd_seven_days

def total_access():
    #!-- Calculando quantidade de acessos totais
    date_today = datetime.today()
    last_seven_days = datetime.today() - timedelta(days=7)

    access = dict(db.session.query(Access.hora, func.sum(Access.access)).group_by('hora').all())
    access = collections.OrderedDict(sorted(access.items()))

    access_hour_total = []
    access_qtd_total = []
    for key, value in access.items():
        access_hour_total.append(str(key) + 'h')
        access_qtd_total.append(value)
    
    return access_hour_total, access_qtd_total

def show_last_access():
    access_hour_30_days, access_qtd_30_days = last_30_days_access()
    access_hour_7_days, access_qtd_7_days = last_7_days_access()
    access_hour_total, access_qtd_total = total_access()

    access_dict = {}
    access_dict['access_hour_thirty_days']=access_hour_30_days
    access_dict['access_qtd_thirty_days']=access_qtd_30_days
    access_dict['access_hour_seven_days'] = access_hour_7_days
    access_dict['access_qtd_seven_days'] = access_qtd_7_days
    access_dict['access_hour_total'] = access_hour_total
    access_dict['access_qtd_total'] = access_qtd_total
    
    return access_dict