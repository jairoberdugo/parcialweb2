from config.db import bd,app,ma
class Estudiante(bd.Model):
    __tablename__='tblestudiante'
    id = bd.Column(bd.Integer,primary_key=True)
    nameestudiante = bd.Column(bd.String(50))
    emailestudiante = bd.Column(bd.String(50))
    claveestudiante = bd.Column(bd.String(20))
    usuarioestudiante = bd.Column(bd.String(29))
    estadoestudiante = bd.Column(bd.String(20))
    
def __init__(self,nameestudiante,emailestudiante, estadoestudiante):
    self.nameestudiante = nameestudiante
    self.emailestudiante = emailestudiante
    self.estadoestudiante = estadoestudiante
    
   
with app.app_context():
    bd.create_all()

class EstudianteSchema(ma.Schema):
    class Meta:
        fields=('id','nameestudiante','emailestudiante', 'estadoestudiante')