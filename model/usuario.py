from config.db import bd,app,ma
class Usuario(bd.Model):
    __tablename__='tblusuario'
    id = bd.Column(bd.Integer,primary_key=True)
    namerol = bd.Column(bd.String(20))
    
    def __init__(self,namerol):
        self.rol = namerol
    
   
with app.app_context():
    bd.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','namerol')