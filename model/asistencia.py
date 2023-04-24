from flask import render_template
from datetime import date, datetime, timedelta
from config.db import bd,app,ma
class Asistencia(bd.Model):
    __tablename__='tblasistencia'
    id = bd.Column(bd.Integer,primary_key=True)
    idEstudiante_fk = bd.Column(bd.Integer, bd.ForeignKey('tblestudiante.id'))
    registrodentrada=bd.Column(bd.Integer)
    registrosalida=bd.Column(bd.Integer)
    fechayhora_entrd=bd.Column(bd.DateTime)
    fechayhora_sali=bd.Column(bd.DateTime)
    estado_sesion = bd.Column(bd.String(2))
    
    def __init__(self,registrodentrada,registrosalida, fechayhora_entrd, fechayhora_salid,estado_sesion):
        self.registrodentrada = registrodentrada
        self.registrosalida = registrosalida
        self.fechayhora_entrd = fechayhora_entrd
        self.fechayhora_sali = fechayhora_salid
        self.estado_sesion = estado_sesion
        
    
   
with app.app_context():
    bd.create_all()

class AsistenciaSchema(ma.Schema):
    class Meta:
        fields=('id','registrodentrada','registrosalida', 'fechayhora_entrd','idEstudiante_fk','fechayhora_salid')