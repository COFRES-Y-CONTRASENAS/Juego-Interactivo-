#----------------------------------------------------
# ARCHIVO: juego.py 
# Modulo que cocntiene la clase JuegoCazador, a cual controla el flujo del juego 
# (menú, rondas, salida). Administra el puntaje acumulado y el historial de rondas
# y permite al usuario jugar tantas rondas como lo desee. 
#----------------------------------------------------
from password import Password
from cofre import Cofre
from exceptions import (LongitudInvalidaError,TipoDatoInvalidoError,
                        PasswordInvalidaError)



# Esta clase representa al jugador y permite administrar su progreso
class Juego_Cazador:
    
    # Anuncio de bienvenida al jugador
    ANUNCIO = """
     
    CAZADOR DE CONTRASEÑAS
                 
El juego consiste en generar contraseñas, abrir cofres y 
acumular puntos. ¡Vamos a jugar!
    
    """  
    def __init__(self):
        
        self.puntaje = 0
        self.rondas_jugadas = 0
        self.historial = []  # Lista donde se almacenan las rondas jugadas
        
    def _separador(self):
        print("\n" + "─" * 55)
        
    def _mostrar_estado(self):
         print(f"\n  Ronda: {self.ronda}  | Puntaje acumulado: {self.puntaje}")
         
     # Solicitar longitud con validación 
    def _pedir_longitud(self) -> int:
        entrada = input("\n Ingresa la longitud de la contraseña (mínimo 8): ").strip()
        
        # Validar que sea un entero positivo
        if not entrada.isdigit():
            raise TipoDatoInvalidoError( f"'{entrada}' no es un número válido. "
                "Debes ingresar un entero positivo.")
    
        longitud =int(entrada)
        
        # Validar longitud mínima de 8
        if longitud < 8:
            raise LongitudInvalidaError(f"La longitud mínima permitida es 8. Ingresaste: {longitud}.")

        return longitud
    
    def _jugar_ronda(self):
        
        self.ronda += 1
        self._separador()
        self._mostrar_estado()
        print()
        
        resultado = ""
        
        
        try:
            longitud = self._pedir_longitud()
            password = Password(longitud)
            clave = password.generar()
            print(f"\n  Contraseña generada: {clave}")
 
            # ── 3. Validar y abrir cofre ──
            if password.validar():
                # Contraseña válida → cofre positivo aleatorio
                cofre = Cofre.abrir_aleatorio()
                self.puntaje += cofre.puntos
                resultado = f"✅ Válida → {cofre}"
                print(f"\n  ✅ ¡Contraseña VÁLIDA!")
                print(f"  {cofre}")
            else:
                # Contraseña inválida (caso de seguridad; rara vez ocurre
                # con el generador actual, pero se maneja por robustez)
                raise PasswordInvalidaError(
                    "La contraseña generada no cumple los requisitos."
                )
 
        except TipoDatoInvalidoError as e:
            # El usuario escribió algo que no es un número
            print(f"\n   Error de entrada: {e}")
            cofre = Cofre.abrir_maldito()
            self.puntaje += cofre.puntos
            resultado = f"❌ Entrada inválida → {cofre}"
            print(f"  {cofre}")
 
        except LongitudInvalidaError as e:
            # El usuario ingresó una longitud menor a 8
            print(f"\n ❌Longitud inválida: {e}")
            cofre = Cofre.abrir_maldito()
            self.puntaje += cofre.puntos
            resultado = f"❌ Longitud inválida → {cofre}"
            print(f"  {cofre}")
 
        except PasswordInvalidaError as e:
            # La contraseña no cumple los requisitos
            print(f"\n  Contraseña inválida: {e}")
            cofre = Cofre.abrir_maldito()
            self.puntaje += cofre.puntos
            resultado = f"❌ Contraseña inválida → {cofre}"
            print(f"  {cofre}")
 
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"\n  Error inesperado: {e}")
            cofre = Cofre.abrir_maldito()
            self.puntaje += cofre.puntos
            resultado = f"❌ Error inesperado → {cofre}"
            print(f"  {cofre}")
 
        # ── 5. Guardar en historial y mostrar puntaje ──
        self.historial.append({
            "ronda":     self.ronda,
            "resultado": resultado,
            "puntaje":   self.puntaje,
        })
        print(f"\n  Puntaje actual: {self.puntaje}")
 
    # ── Menú y vistas secundarias ─────────────────────────
 
    def _mostrar_menu(self):
        """Muestra las opciones del menú principal."""
       
        print("\n  │      MENÚ PRINCIPAL         │")
     
        print("  │  1. Generar contraseña      │")
        print("  │  2. Ver historial           │")
        print("  │  3. Salir del juego         │")
     
 
    def _ver_historial(self):
        """Muestra el historial completo de todas las rondas jugadas."""
        self._separador()
        if not self.historial:
            print("\n  No hay rondas jugadas aún.")
            return
        print("\n  HISTORIAL DE RONDAS\n")
        print(f"  {'Ronda':<8} {'Resultado':<42} {'Puntaje'}")
        print("  " + "-" * 58)
        for h in self.historial:
            print(f"  {h['ronda']:<8} {h['resultado']:<42} {h['puntaje']}")
 
    def _mostrar_resultado_final(self):
        """Muestra la pantalla de despedida con el puntaje final y una calificación."""
        self._separador()
        print("\n  FIN DEL JUEGO\n")
        print(f"  Rondas jugadas : {self.ronda}")
        print(f"  Puntaje final  : {self.puntaje}")
 
        # Calificación según puntaje final
        if self.puntaje >= 100:
            print("\n  ¡Eres un MAESTRO Cazador de Contraseñas!")
        elif self.puntaje >= 50:
            print("\n  ¡Buen trabajo, Cazador!")
        elif self.puntaje >= 0:
            print("\n  Sigue practicando, ¡puedes mejorar!")
        else:
            print("\n  Los cofres malditos te dominaron... ¡inténtalo de nuevo!")
 
        print("\n  ¡Gracias por jugar! \n")
 
    # ── Punto de entrada del juego ────────────────────────
 
    def iniciar(self):
        """
        Método principal que lanza el juego y controla el bucle central.
 
        Flujo:
          - Muestra el banner y las instrucciones.
          - Entra en un bucle que muestra el menú y procesa la opción elegida.
          - Sale del bucle cuando el usuario elige la opción 3.
          - Muestra el resultado final.
        """
        print(self.ANUNCIO)
        print("  Bienvenido, Cazador. Las contraseñas son tu arma.")
        print("  Genera contraseñas válidas para abrir cofres y ganar puntos.")
        print("  ¡Cuidado! Los cofres malditos restan 20 puntos.\n")
 
        jugando = True
 
        while jugando:
            self._mostrar_menu()
            opcion = input("\n  Elige una opción (1/2/3): ").strip()
 
            if opcion == "1":
                self._jugar_ronda()
 
            elif opcion == "2":
                self._ver_historial()
 
            elif opcion == "3":
                jugando = False
 
            else:
                print("\n   Opción no válida. Por favor elige 1, 2 o 3.")
 
        self._mostrar_resultado_final()