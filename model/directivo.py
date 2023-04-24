from config.db import bd,app,ma
class Directivo(bd.Model):
    __tablename__='tbldirectivo'
    id = bd.Column(bd.Integer,primary_key=True)
    namedirectivo = bd.Column(bd.String(50))
    emaildirectivo = bd.Column(bd.String(50))
    clavedirectivo = bd.Column(bd.String(20))
    usuariodirectivo = bd.Column(bd.String(29))
    
def __init__(self,namedirectivo,emaildirectivo):
    self.namedirectivo = namedirectivo
    self.emaildirectivo = emaildirectivo
    
   
with app.app_context():
    bd.create_all()

class DirectivoSchema(ma.Schema):
    class Meta:
        fields=('id','namedirectivo','emaildirectivo')