from config.db import bd,app,ma
class Docente(bd.Model):
    __tablename__='tbldocente'
    id = bd.Column(bd.Integer,primary_key=True)
    namedocente = bd.Column(bd.String(50))
    emaildocente = bd.Column(bd.String(50))
    clavedocente = bd.Column(bd.String(20))
    usuariodocente = bd.Column(bd.String(29))
    
def __init__(self,namedocente,emaildocente):
    self.namedocente = namedocente
    self.emaildocente = emaildocente
    
   
with app.app_context():
    bd.create_all()

class DocenteSchema(ma.Schema):
    class Meta:
        fields=('id','namedocente','maildocente')