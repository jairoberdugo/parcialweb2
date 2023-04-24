from config.db import bd,app,ma
class Asistencia(bd.Model):
    __tablename__='tblasistencia'
    id = bd.Column(bd.Integer,primary_key=True)
    idEstudiante_fk = bd.Column(bd.Integer, bd.ForeignKey('tblestudiante.id'))
    registrodentrada=bd.Column(bd.Integer)
    registrosalida=bd.Column(bd.Integer)
    fechayhora=bd.Column(bd.String(50))
    
def __init__(self,registrodentrada,registrosalida, fechayhora):
    self.registrodentrada = registrodentrada
    self.registrosalida = registrosalida
    self.fechayhora = fechayhora
    
   
with app.app_context():
    bd.create_all()

class AsistenciaSchema(ma.Schema):
    class Meta:
        fields=('id','registrodentrada','registrosalida', 'fechayhora')