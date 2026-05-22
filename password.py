#----------------------------------------------------
# ARCHIVO: password.py 
# Define la clase Password, la cual permite generar contraseñas
# aleatorias y validar que la contraseña cumpla todos los 
# requisitos establecidos.
#----------------------------------------------------

import random
import string
from exceptions import PasswordInvalidoError

#Clase que se encarga de generar i validar contraseñas
class Password:
    
    # Caracteres especiales validos 
    ESPECIALES = "¿¡?=)(/*+-%&$#!"
    
    # Inicializa la contraseña con la longitud solicitada.
    def __init__(self, longitud: int):
        
        self.longitud = longitud
        self.valor = ""    # Se llena al llamar a la funcion generar.
                
    # Método para generar una contraseña aleatoria.
    def generar(self) -> str :
        
        # Se construye un conjunto de caracteres únicos disponibles.
        pool = list(
            string.ascii_uppercase +      # Letras mayusculas
            string.ascii_lowercase +      # Letras minusculas
            string.digits +               # Números (0-9)
            self.ESPECIALES               # Caracteres especiales
        )
        
        # Elimina los duplicados
        pool= list(dict.fromkeys(pool))
        
        # se verifica que la contraseña tenga los caracteres suficientes únicos.
        if self.longitud > len(pool):
            raise PasswordInvalidoError(
                f"No es posible generar una contraseña de {self.longitud} caracteres "
                f"sin repetición. Máximo permitido con caracteres únicos: {len(pool)}."
            )
        
        # Se selecciona un caracter obligatorio de cada grupo.   
        mayus = random.choice(string.ascii_uppercase)
        minus = random.choice(string.ascii_lowercase)
        num = random.choice(string.digits)
        esp = random.choice(self.ESPECIALES)
        
        obligatorios = [mayus, minus, num, esp]
        
        # Elimina del pool los caracteres ya seleccionados
        pool_restante = [c for c in pool if c not in obligatorios]
    
        try:
            complemento = random.sample(pool_restante, self.longitud - 4)
        except ValueError:
            raise PasswordInvalidoError("Longitud demasiado grande")
        
         
              
        # Une y mezcla los caracteres
        result = obligatorios + complemento
        random.shuffle(result)
        
        self.valor = "".join(result)
        return self.valor

    
    # Se verifican todas las reglas establecidas para una contraseña correcta
    def validar(self) -> tuple[bool, str]:
    
        if not self.valor:
            return False, "No se ha generado contraseña"
       
        # Verificar longitud mínima.
        if len(self.valor) != self.longitud:
            return False,
        
        # Verificar al menos una mayuscula.
        if not any(c.isupper() for c in self.valor):
            return False
        
        # Verificar al menos una minuscula.     
        if not any(c.islower() for c in self.valor):
            return False
        
        # Verificar al menos un número.
        if not any(c.isdigit() for c in self.valor):
            return False
        
        # Verificar al menos un caracter especial.
        if not any(c in self.ESPECIALES for c in self.valor):
            return False
        
        # verifica que no haya caracteres repetidos
        if len(set(self.valor)) != len(self.valor):   
            return False
        
        return True
    
   
       
    
    
    