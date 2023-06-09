from config.db import bd,app,ma
class Estudiante(bd.Model):
    __tablename__='tblestudiante'
    id = bd.Column(bd.Integer,primary_key=True)
    fullname = bd.Column(bd.String(50))
    email = bd.Column(bd.String(50))
    estado = bd.Column(bd.String(20))
    IdUsuario_fk = bd.Column(bd.Integer, bd.ForeignKey('tblusuario.id'))
    password = bd.Column(bd.String(20))
    
    def __init__(self,fullname,email, estado, password):
        self.fullname = fullname
        self.email = email
        self.estado = estado
        self.password = password
    
   
with app.app_context():
    bd.create_all()

class EstudianteSchema(ma.Schema):
    class Meta:
        fields=('id','fullname','email', 'estado','IdUsuario_fk','password')