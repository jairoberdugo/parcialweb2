from config.db import bd,app,ma
class Usuario(bd.Model):
    __tablename__='tbldocente'
    id = bd.Column(bd.Integer,primary_key=True)
    usuario = bd.Column(bd.String(50))
    clave = bd.Column(bd.String(50))
    rol = bd.Column(bd.String(20))
    
def __init__(self,usuario,rol):
    self.usuario = usuario
    self.rol = rol
    
   
with app.app_context():
    bd.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','usuario','rol')