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

# ------ ACTUALIZAR TABLA USUARIO ------------
@app.route("/updateusuario", methods=['POST'])
def updateusuario():    
    id = request.json['id'] 
    namerol = request.json['namerol'] 
    usuario = Usuario.query.get(id)  
    usuario.namerol = namerol # aqui le actualizo el valor al campo. 
    bd.session.commit()     
    return "se actualizo usuario correctamente"

# ------ ACTUALIZAR TABLA ADMINISTRATIVO ------------
@app.route("/updateadmin", methods=['POST'])
def updateadmin():    
    id = request.json['id'] 
    fullname = request.json['fullname'] 
    email = request.json['email']
    password = request.json['password']
    admin = Administrativo.query.get(id)  
    admin.fullname = fullname
    admin.email = email
    admin.password = password
    bd.session.commit()     
    return "se actualizo administrativo correctamente"

# ------ ACTUALIZAR TABLA ESTUDIANTE ------------
@app.route("/updatestudent", methods=['POST'])
def updatestudent():    
    id = request.json['id'] 
    fullname = request.json['fullname'] 
    email = request.json['email']
    password = request.json['password']
    estado = request.json['estado']
    student = Estudiante.query.get(id)  
    student.fullname = fullname
    student.email = email
    student.password = password
    student.estado = estado
    bd.session.commit()     
    return "se actualizo estudiante correctamente"

# ------ ACTUALIZAR TABLA ESTUDIANTE ------------
@app.route("/updateasistencia", methods=['POST'])
def updateasistencia():
    id = request.json['id'] 
    fechayhora_entrd = request.json['fechayhora_entrd']
    fechayhora_salid = request.json['fechayhora_salid']
    estado_sesion = request.json['estado_sesion']
    re = request.json['registroentrada']
    rs = request.json['registrosalida']
    asist = Asistencia.query.get(id)  #busco registro por el id
    asist.fechayhora_entrd = fechayhora_entrd
    asist.fechayhora_salid = fechayhora_salid
    asist.estado_sesion = estado_sesion
    asist.registroentrada = re
    asist.registrosalida = rs
    bd.session.commit()
    return "se actualizo asistencia correctamente"

# ---------------- ELIMINAR EN TABLA USUARIO ------------
@app.route("/euser", methods=['POST'])
def euser():
    id = request.json['id'] 
    usuario = Usuario.query.get(id)
    bd.session.delete(usuario)
    bd.session.commit()
    return jsonify(UsuarioSchema.dump(usuario))

# --------------- ELIMINAR EN TABLA ADMINISTRATIVO ---------
@app.route("/eadmin", methods=['POST'])
def eadmin():
    id = request.json['id'] 
    admin = Administrativo.query.get(id)
    bd.session.delete(admin)
    bd.session.commit()
    return jsonify(AdministrativoSchema.dump(admin))

# --------------- ELIMINAR EN TABLA ESTUDIANTE ---------
@app.route("/estudent", methods=['POST'])
def estudent():
    id = request.json['id'] 
    student = Estudiante.query.get(id)
    bd.session.delete(student)
    bd.session.commit()
    return jsonify(EstudianteSchema.dump(student))

# El sistema debe contar con una funcionalidad que permita a los profesores y directivos del colegio 
# ver en tiempo real el estado de entrada y salida de los estudiantes, así como el registro de sus
# actividades en el sistema. Esto permitirá al colegio llevar un control riguroso sobre la asistencia
# de los estudiantes.

@app.route('/consultaext', methods=['GET'])
def dostablas():
    results = bd.session.query(Estudiante, Asistencia).join(Asistencia).all() 
    dato={}   
    i=0
    for estudiante, asistencia in results:
        i+=1	       
        dato[i] = {
        'Nombre: ':estudiante.fullname,
        'registro entrada: ' :estudiante.registroentrada,
        'registro salida: ': estudiante.registrosalida,
		'Fecha y hora de entrada: ':asistencia.fechayhora_entrd,
        'Fecha y hora de salida: ':asistencia.fechayhora_salid,                     
        }
        print(Estudiante.fullname,Asistencia.fechayhora_entrd , Asistencia.fechayhora_salid)
    return jsonify(dato)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')