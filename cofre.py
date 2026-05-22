#----------------------------------------------------
# ARCHIVO: cofre.py 
# Define la clase Cofre para representar cofres.
#----------------------------------------------------

# Representa los cofres que puede ganar o perder el jugador 
class Cofre:
    def __init__(self, tipo, puntos):
        self.tipo = tipo
        self.puntos = self._definir_puntos()
        
    # Metodo que define los puntos segun el tipo de cofre, devolviendo un entero
    def _definir_puntos(self) -> int:
        puntos= {
            "Común": 10,
            "Raro": 25,
            "Legendario": 50,
            "Maldito": -20
        }
        return puntos.get(self.tipo, 0)

    # Método para abrir el cofre y obtener puntos
    def abrir(self) -> str:
        signo = "+" if self.puntos > 0 else ""
        return f"Haz abierto un cofre ** {self.tipo}**  {signo}{self.puntos} puntos"
    
    def __str__(self):
        return f"{self.tipo} ({self.puntos} pts)"