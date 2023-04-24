from config.db import bd,app,ma
class Administrativo(bd.Model):
    __tablename__='tbldirectivo'
    id = bd.Column(bd.Integer,primary_key=True)
    nameadministrativo = bd.Column(bd.String(50))
    emailadministrativo = bd.Column(bd.String(50))
    tipoadmin = bd.Column(bd.String(20))
    Idusuario_fk = bd.Column(bd.Integer, bd.ForeignKey('tblusuario.id'))
    
def __init__(self,nameadministrativo,emailadministrativo):
    self.nameadministrativo = nameadministrativo
    self.emailadministrativo = emailadministrativo
    
   
with app.app_context():
    bd.create_all()

class AdministrativoSchema(ma.Schema):
    class Meta:
        fields=('id','nameadministrativo','emailadministrativo')