#importo las dependencias de trabajo
from config.db import app, bd

#importamos los modelos

from model.usuario import Usuario, UsuarioSchema
from model.estudiante import Estudiante, EstudianteSchema
from model.administrativo import Administrativo, AdministrativoSchema
from model.asistencia import Asistencia, AsistenciaSchema

