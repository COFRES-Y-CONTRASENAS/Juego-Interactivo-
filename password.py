#----------------------------------------------------
# ARCHIVO: password.py 
# Define la clase Password, la cual permite generar contraseñas
# aleatorias y validar que la contraseña cumpla todos los 
# requisitos establecidos.
#----------------------------------------------------

# Importaciones de modulos random (genera elementos aleatorios),
# string (conjunto de caracteres predefinidos) y la excepcion personalizada 
# PasswordInvalidoError (errores relacionados con contraseñas invalidas).
import random
import string
from exceptions import PasswordInvalidoError

# La clase password se encarga de generar y validar contraseñas mediante los metodos
# generar() y validar().
class Password:
    
    # Esta constante contiene la lista de caracteres especiales permitidos.
    ESPECIALES = "¿¡?=)(/*+-%&$#!"

    # Constructor que recibe los parametros de longitud y valor
    def __init__(self, longitud:int, valor: str=""):
        self.longitud = longitud
        self.valor = valor

    # Este metodo genera una contraseña alestoria valida segun las reglas establecidas
    def generar(self):
        # Genera una letra mayuscula aleatoria.
        mayus = random.choice(string.ascii_uppercase)
        # Genera una letra minuscula aleatoria.
        minus = random.choice(string.ascii_lowercase)
        # Genera un número aleatorio.
        numero = random.choice(string.digits)
        # Genera un caracter especial aleatorio.
        especial = random.choice(self.ESPECIALES)
        # Lista de caracteres oligatorios.
        obligatorios=[
            mayus,
            minus,
            numero,
            especial]

        # Conjunto de caracteres permitidos en una contraseña.
        resto = string.ascii_letters + string.digits + self.ESPECIALES

        # Bucle que sigue agreegndo caracteres hasta alcanzar la longitud establecida.
        while len(obligatorios)<self.longitud:

            caracter = random.choice(resto)
            # verifica que el ccaracter no este repetido.
            if caracter not in obligatorios:
                obligatorios.append(caracter)
                
        # Mezcla los caracteres.
        random.shuffle(obligatorios)

        # Convierte la lista en texto sin espacios, uniendo todos los elementos por
        # medio de la función join()
        self.valor = "".join(obligatorios)

        return self.valor
    
    # Este metodo valida que las contraseñas generadas cumplan con todas las reglas.
    def validar(self):
        
        # verifica si el usuario dejo vacio el campo.
        if not self.valor:
            raise PasswordInvalidoError(
                "No escribiste ninguna contraseña"
            )
        
        # Verifica longitud mínima.
        if len(self.valor) != self.longitud:
            raise PasswordInvalidoError(
                f"La contraseña debe tener exactamente {self.longitud} caracteres"
            )
            
        # Verifica al menos una mayuscula (A-Z).
        if not any(c.isupper() for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener al menos una mayúscula"
            )
            
        # Verifica al menos una minuscula (a-z).
        if not any(c.islower() for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener al menos una minúscula"
            )

        # Verifica al menos un digito (0-9)
        if not any(c.isdigit() for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener al menos un número"
            )

        # Verifica al menos un caracter especial (¿¡?=)(/*+-%&$#!).
        if not any(c in self.ESPECIALES for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener un carácter especial ' ¿¡?=)(/*+-%&$#! ' "
            )
        # Verifica que la contraseña no tenga caracteres repetidos. 
        # La función set() elimina los duplicados.
        if len(set(self.valor)) != len(self.valor):
            raise PasswordInvalidoError(
                "No se permiten caracteres repetidos"
            )
        # Si pasa todas las validaciones la contraseña es valida.
        return True

   
       
    
    
    