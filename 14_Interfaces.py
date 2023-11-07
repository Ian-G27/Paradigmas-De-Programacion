#==============================================================================
#  Ian Diego Buendia Alvarez
#  ESFM IPN 2023
#==============================================================================
#  Del directorio aplicacion, el subdirectorio repositorio
#  el archivo basedeadtos.py : trae el objeto BaseDeDatos
#==============================================================================
from aplicacion.repositorio.basededatos import BaseDeDatos

#===============================================================================
#  Del directorio aplicacion, el subdirectorio repositorio,
#  el archivo s3.py: traes el objeto s3
#===============================================================================
from aplicacion.repositorio.s3 import S3

#===============================================================================
#  Del directorio aplicacion, el subdirectorio repositorio,
#  el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#===============================================================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

#===============================================================================
#  Del directorio aplicacion, el subdirectorio modelos,
#  el archivo usuario.py : trae el objeto Usuario
#===============================================================================
from aplicacion.modelos.usuario import Usuario

#================================================================================
#  Del directorio aplicacion, el subdirectorio negocios,
#  el archivo manejodeincripciones.py : trae el onjeto ManejoDeIncripciones
#================================================================================
from aplicacion.negocios.manejodeincripciones import ManejoDeInscripciones

#===============================
#  Crea el objeto Usuario
#================================
usuario = Usuario("Roberto", "Jimenez", 18 )

#============================================
#  Crear el objeto s3
#============================================
repositorioS3 = S3("3213211321","sdf324223","MiCubeta")

#=======================================================
#  Interface inscribirUsuario del objeto ManejoDeIncripciones
#==============================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#============================================================
#  Crear el objeto sistemadearchivos
#============================================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

#==================================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#===================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#==============================================================================
# Crear el objetos basededatos
#============================================================================
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#=========================================================================
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#========================================================================
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")
