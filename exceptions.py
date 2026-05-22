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
    def __init__(self, mensaje="❌ La longitud debe ser mínimo 8 caracteres."):
        super().__init__(mensaje)

class PasswordInvalidoError(Exception):
    """ Error cuando la contraseña ingresada no cumple con los requisitos. """
    pass


