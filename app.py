#importo las dependencias de trabajo
from flask import Flask, request, jsonify, json, render_template
from config.db import app, bd

#importamos los modelos

from model.usuario import Usuario, UsuarioSchema
from model.estudiante import Estudiante, EstudianteSchema
from model.administrativo import Administrativo, AdministrativoSchema
from model.asistencia import Asistencia, AsistenciaSchema

usuario_schema = UsuarioSchema()
usuario_schema = UsuarioSchema(many=True)

estudiante_schema = EstudianteSchema()
estudiante_schema = EstudianteSchema(many=True)

administrativo_schema = AdministrativoSchema()
administrativo_schema= AdministrativoSchema(many=True)

asistencia_schema = AsistenciaSchema()
asistencia_schema = AsistenciaSchema(many=True)


#  ----  GUARDAR A UN USUARIO ADMINISTRATIVO EN LA BASE DE DATOS -----
@app.route("/saveuser_admin", methods=['POST'])
def rutanueva():
    rol = request.json['rol']
    usuario = request.json['user']
    clave = request.json['clave']
    newuserad = Usuario(rol,usuario,clave)
    fullname = request.json['fullname'] 
    email = request.json['email']
    tipoadmin = request.json['tipoadmin']
    newuser = Administrativo(fullname, email,tipoadmin)
    bd.session.add(newuserad)
    bd.session.add(newuser)
    bd.session.commit()     
    return "administrativo guardado"




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')