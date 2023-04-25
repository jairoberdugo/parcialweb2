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


#  ----  GUARDAR USUARIO EN LA BASE DE DATOS -----
@app.route("/saveusuario", methods=['POST'])
def saveusuario():
    namerol = request.json['namerol'] 
    newusuario = Usuario(namerol)
    bd.session.add(newusuario)
    bd.session.commit()     
    return "usuario,rol registrado."

# --- GUARDAR ADMINISTRATIVO EN LA BASE DE DATOS ----
@app.route("/saveadmin", methods=['POST'])
def saveadmin():
    fullname = request.json['fullname']
    email = request.json['email']
    idUsuario_fk = request.json['idUsuario_fk']
    password = request.json['password']
    newadmin = Administrativo(fullname, email, idUsuario_fk, password)
    bd.session.add(newadmin)
    bd.session.commit()     
    return "admin guardado"

# --- GUARDAR ESTUDIANTE EN LA BASE DE DATOS ----
@app.route("/savestudent", methods=['POST'])
def savestudent():
    fullname = request.json['fullname']
    email = request.json['email']
    idUsuario_fk = request.json['idUsuario_fk']
    password = request.json['password']
    estado = request.json['estado']
    newestudiante = Estudiante(fullname, email, idUsuario_fk, password, estado)
    bd.session.add(newestudiante)
    bd.session.commit()     
    return "estudiante guardado"

# ----- GUARDAR ASISTENCIA EN BASE DE DATOS (SIN CONDICIONES) --------
@app.route("/saveasistencia", methods=['POST'])
def saveasistencia():
    fechayhora_entrd = request.json['fechayhora_entrd']
    fechayhora_salid = request.json['fechayhora_salid']
    estado_sesion = request.json['estado_sesion']
    idEstudiante_fk = request.json['idEstudiante_fk']
    registro_ent= request.json['registro_ent']
    registro_sali= request.json['registro_sali']
    newasistencia = Asistencia(fechayhora_entrd, fechayhora_salid, estado_sesion, idEstudiante_fk, registro_ent, registro_sali)
    bd.session.add(newasistencia)
    bd.session.commit()     
    return "asistencia guardada"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')