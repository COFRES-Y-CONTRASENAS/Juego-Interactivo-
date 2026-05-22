#----------------------------------------------------
# ARCHIVO: password.py 
# Define la clase Password para representar contraseñas.
#----------------------------------------------------


import random
import string
from exceptions import LongitudInvalidaError, ContraseñaInvalidaError

#Clase que se encarga de generar i validar contraseñas
class Password:
    def __init__(self, longitud: int):
        if not isinstance(longitud, int) or longitud < 8:
            raise LongitudInvalidaError()
        self.longitud = longitud
        self.valor = ""
                
    # Método para generar una contraseña aleatoria
    def generar(self) -> str :
        caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + "¿¡?=)(/*+-%&$#!"
        
        for _ in range(200):
            self.valor= ''.join(random.choice(caracteres) for _ in range(self.longitud))
            
            if self._es_valido():
                return self.valor
            
        # El sistema genera una contraseña valida si el usuario no lo logra.
        self.valor = self._generar_()
        return self.valor
    
    # Se verifican todas las reglas establecidas para una contraseña correcta
    def _es_valida(self) -> bool:
        """Verifica todas las reglas del enunciado."""
        if len(self.valor) != self.longitud:
            return False
        if not any(c.isupper() for c in self.valor):
            return False
        if not any(c.islower() for c in self.valor):
            return False
        if not any(c.isdigit() for c in self.valor):
            return False
        if not any(c in "¿¡?=)(/*+-%&$#!" for c in self.valor):
            return False
        if len(set(self.valor)) != len(self.valor):   # Sin caracteres repetidos
            return False
        return True
    
    def _generar_forzada(self) -> str:
        """Genera una contraseña garantizada que cumpla todas las reglas."""
        partes = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice("¿¡?=)(/*+-%&$#!")
        ]
        resto = [random.choice(string.ascii_letters + string.digits + "!?#$%&*+-_") 
                for _ in range(self.longitud - 4)]
        
        pwd = ''.join(partes + resto)
        pwd_list = list(pwd)
        random.shuffle(pwd_list)
        return ''.join(pwd_list)[:self.longitud]
    
    # Método para validar la contraseña ingresada por el jugador
    def validar(self) -> tuple [bool,str]:
        if self._es_valida():
            return True, "Contraseña válida"
        return False, "La contraseña no cumple con todos los requisitos."
       
    
    
    