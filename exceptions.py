#----------------------------------------------------
# ARCHIVO: exceptions.py 
# Define todas las excepciones personalizadas para el juego cazador
# de contraseñas.
#----------------------------------------------------


#---------------------------------------
# EXCEPCIONES PERSONALIZADAS
# Estas excepciones se utilizan para manejar errores específicos del juego
#---------------------------------------

class LongitudInvalidaError(Exception):
    """ Errores relacionados con longitud de contraseña. """
    pass
class TipoDatoInvalidoError(Exception):
    """ Error cuando el tipo de dato ingresado es inválido. """
    pass

class PasswordInvalidaError(Exception):
    """ Error cuando la contraseña ingresada no cumple con los requisitos. """
    pass


