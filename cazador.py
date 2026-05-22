#----------------------------------------------------
# ARCHIVO: cazador.py 
# Aqui se crea la clase Cazador, que representa al
# jugador en el juego.
#----------------------------------------------------

from cofre import Cofre

# Esta clase representa al jugador y permite administrar su progreso
class Cazador:
    def __init__(self, nombre: str = "Cazador"):
        self.nombre = nombre
        self.puntos_totales = 0
        self.rondas_jugadas = 0
        
        
    # Método para que el cazador intente abrir un cofre
    def abrir_cofre (self, cofre: Cofre):
        self.puntos_totales += cofre.puntos
        self.rondas_jugadas += 1
        print(cofre.abrir())
        
    
    # Método para mostrar el estado actual del cazador
    def mostrar_estado(self):
        print("\n" + "="*50) 
        print(f"   ESTADISTICAS DE {self.nombre.upper()}")
        print("="*50)
        print(f"Puntos totales : {self.puntos_totales}")
        print(f"Rondas jugadas : {self.rondas_jugadas}")
        print("="*50)