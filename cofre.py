#----------------------------------------------------
# ARCHIVO: cofre.py 
# Define la clase Cofre para representar los tipos de cofres, 
# asignar la cantidad de puntos de cada tipo y aplicar penalizaciones
# al insertar datos invalidos.
#----------------------------------------------------

# Representa los cofres que puede abrir el jugador 
class Cofre:
    
    # Diccionario que contiene los tipos de cofres y los puntos que obtendrá 
    # al abrirlos cuando la contraseña suministrada sea valida.
    TIPOS = {
        "Común":      {"puntos": 10},
        "Raro":       {"puntos": 25},
        "Legendario": {"puntos": 50},
        "Maldito":    {"puntos": -20}
    }
    # Constructor que recibe el parametro tipo.
    def __init__(self, tipo):
                       
        self.tipo = tipo
        self.puntos = self.TIPOS [tipo]["puntos"]
   
    # Decorador que modifica el metodo sin crear un objeto
    @classmethod
    # El metodo abrir_maldito crea y retorna siempre el cofre maldito disminuyendo
    # el puntaje del jugador en -20 cada vez que el jugador se equivoque al ingresar un dato.
    def abrir_maldito(cls) -> "Cofre":
        return cls("Maldito")
 
    # El metodo especial __str__ permite mostrar la información de manera clara al usuario.
    def __str__(self) -> str:
        signo = "+" if self.puntos >= 0 else ""
        return f"Cofre {self.tipo} ({signo}{self.puntos} puntos)"

        
        
        
        
       