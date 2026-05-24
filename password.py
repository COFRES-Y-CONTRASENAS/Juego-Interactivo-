#----------------------------------------------------
# ARCHIVO: password.py 
# Define la clase Password, la cual permite generar contraseñas
# aleatorias y validar que la contraseña cumpla todos los 
# requisitos establecidos.
#----------------------------------------------------
import random
import string
from exceptions import PasswordInvalidoError

class Password:

    ESPECIALES = "¿¡?=)(/*+-%&$#!"

    def __init__(self, longitud:int, valor: str=""):
        self.longitud = longitud
        self.valor = valor


    def generar(self):
        mayus=random.choice(string.ascii_uppercase)

        minus=random.choice(string.ascii_lowercase)

        numero=random.choice(string.digits)

        especial=random.choice(self.ESPECIALES)

        obligatorios=[
            mayus,
            minus,
            numero,
            especial]

        resto=string.ascii_letters + string.digits + self.ESPECIALES

        while len(obligatorios)<self.longitud:

            caracter=random.choice(resto)

            if caracter not in obligatorios:

                obligatorios.append(caracter)

        random.shuffle(obligatorios)

        self.valor="".join(obligatorios)

        return self.valor

    def validar(self):

        if not self.valor:
            raise PasswordInvalidoError(
                "No escribiste ninguna contraseña"
            )
        
        # Verificar longitud mínima.
        if len(self.valor) != self.longitud:
            raise PasswordInvalidoError(
                f"La contraseña debe tener exactamente {self.longitud} caracteres"
            )
            
        # Verificar al menos una mayuscula (A-Z).
        if not any(c.isupper() for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener al menos una mayúscula"
            )
            
        # Verificar al menos una minuscula (a-z).
        if not any(c.islower() for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener al menos una minúscula"
            )

        # Verificar al menos un digito (0-9)
        if not any(c.isdigit() for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener al menos un número"
            )

        # Verificar al menos un caracter especial (¿¡?=)(/*+-%&$#!).
        if not any(c in self.ESPECIALES for c in self.valor):
            raise PasswordInvalidoError(
                "Debe tener un carácter especial ' ¿¡?=)(/*+-%&$#! ' "
            )
        # Verificar que la conraseña no tenga caracteres repetidos
        if len(set(self.valor)) != len(self.valor):
            raise PasswordInvalidoError(
                "No se permiten caracteres repetidos"
            )

        return True

   
       
    
    
    