#importamos las librerias a trabajar
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/parcialweb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bd = SQLAlchemy(app)
ma = Marshmallow(app)