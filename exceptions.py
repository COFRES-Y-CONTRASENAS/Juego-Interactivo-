#----------------------------------------------------
# ARCHIVO: exceptions.py 
# Define todas las excepciones personalizadas para el juego cazador
# de contraseñas.
#----------------------------------------------------


#---------------------------------------
# EXCEPCION BASE 
# todas las demas herendan de esta clase
#---------------------------------------

class CazadorException(Exception):
    """ Excepcion base para el juego cazador de contraseñas. """
    pass    

#---------------------------------------
# EXCEPCION DE CONTRASEÑA 
# se lanza cuando el jugador ingresa una contraseña incorrecta
#---------------------------------------

class ContraseñaIncorrecta(CazadorException):
    """ Errores relacionados con contraseñas incorrectas. """
    pass

class ContraseñaMuyCorta(ContraseñaIncorrecta):
    """ Error cuando la contraseña ingresada es demasiado corta. """
    pass

class ContraseñaSinMayuscula(ContraseñaIncorrecta):
    """ Error cuando la contraseña ingresada no contiene mayúsculas. """
    pass

class ContraseñaSinMinuscula(ContraseñaIncorrecta):
    """ Error cuando la contraseña ingresada no contiene minúsculas. """
    pass    

class ContraseñaSinNumero(ContraseñaIncorrecta):
    """ Error cuando la contraseña ingresada no contiene números. """
    pass

class ContraseñaSinCaracterEspecial(ContraseñaIncorrecta):
    """ Error cuando la contraseña ingresada no contiene caracteres especiales. """
    pass

class ContraseñaConRepeticion(ContraseñaIncorrecta):
    """ Error cuando la contraseña tiene caracteres repetidos. """
    pass

#---------------------------------------
# -
#---------------------------------------