#----------------------------------------------------
# ARCHIVO: exceptions.py 
# Define todas las excepciones personalizadas para el juego cazador
# de contraseñas.
#----------------------------------------------------


#---------------------------------------
# EXCEPCIONES PERSONALIZADAS
# Estas excepciones se utilizan para manejar errores específicos del juego
#---------------------------------------

class CazadorException(Exception):
    """ Excepcion base para el juego cazador de contraseñas. """
    pass    

class LongitudInvalidaError(CazadorException):
    """ Errores relacionados con longitud de contraseña. """
    def __init__(self, mensaje = "La longitud de la contraseña debe ser minimo de 8 caracteres."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class TipoDatoInvalidoError(CazadorException):
    """ Error cuando el tipo de dato ingresado es inválido. """
    def __init__(self, mensaje = "Ingresa un número válido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ContraseñaInvalidaError(CazadorException):
    """ Error cuando la contraseña ingresada no cumple con los requisitos. """
    def __init__(self, mensaje = "La contraseña generada no cumple todas las reglas."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

