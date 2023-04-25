from config.db import bd,app,ma
class Administrativo(bd.Model):
    __tablename__='tbladministrativo'
    id = bd.Column(bd.Integer,primary_key=True)
    fullname = bd.Column(bd.String(50))
    email = bd.Column(bd.String(50))
    IdUsuario_fk = bd.Column(bd.Integer, bd.ForeignKey('tblusuario.id'))
    password = bd.Column(bd.String(50))
    
    def __init__(self,fullname,email, IdUsuario_fk, password):
        self.fullname = fullname
        self.email = email
        self.IdUsuario_fk = IdUsuario_fk
        self.password = password
    
   
with app.app_context():
    bd.create_all()

class AdministrativoSchema(ma.Schema):
    class Meta:
        fields=('id','fullname','email','IdUsuario_fk','password')