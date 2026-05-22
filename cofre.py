#----------------------------------------------------
# ARCHIVO: cofre.py 
# Define la clase Cofre para representar los tipos de cofres del juego,
# abrir cofres de forma aleatoria y retorna los puntos obtenidos por el jugador.
#----------------------------------------------------

import random

# Representa los cofres que puede ganar o perder el jugador 
class Cofre:
    
    TIPOS = {
        "Común":      {"puntos": 10},
        "Raro":       {"puntos": 25},
        "Legendario": {"puntos": 50},
        "Maldito":    {"puntos": -20}
    }
    # se inicializa un cofre con el tipo indicado
    def __init__(self, tipo: str):
        
        if tipo not in self.TIPOS:
            raise ValueError((f"Tipo de cofre desconocido: '{tipo}'. "
                            f"Tipos válidos: {list(self.TIPOS.keys())}"))
            
        self.tipo = tipo
        self.puntos = self.TIPOS [tipo]["puntos"]
    
    @classmethod 
    # Método para abrir el cofre y obtener puntos
    def abrir_aleatorio(cls) -> "Cofre":
        
        tipos_positivos = ["Común","Raro","Legendario"]
        tipo_elegido = random.choice(tipos_positivos)
        return cls(tipo_elegido)
    
    
    @classmethod
    # La función abrir_maldito crea y retorna siempre el cofre maldito disminuyendo
    # el puntaje del jugador en -20 cada ve que el jugador se equivoque al ingresar la conraseña.
    def abrir_maldito(cls) -> "Cofre":
        return cls("Maldito")
 
    # Representación en texto  
    def __str__(self) -> str:
        signo = "+" if self.puntos >= 0 else ""
        return f"Cofre {self.tipo} ({signo}{self.puntos} puntos)"
 
        
        
        
        
        
       