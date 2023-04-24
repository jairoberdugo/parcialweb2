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

