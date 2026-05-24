#----------------------------------------------------
# ARCHIVO: juego.py 
# Modulo que cocntiene la clase JuegoCazador, a cual controla el flujo del juego 
# (menú, rondas, salida). Administra el puntaje acumulado y el historial de rondas
# y permite al usuario jugar tantas rondas como lo desee. 
#----------------------------------------------------
from password import Password
from cofre import Cofre
from exceptions import (LongitudInvalidaError,TipoDatoInvalidoError,
                        PasswordInvalidoError)



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
        self.ronda = 0
        self.historial = []  # Lista donde se almacenan las rondas jugadas
        
    def _separador(self):
        print("\n" + "─" * 55)
        
    def _mostrar_estado(self):
         print(f"\n  Ronda: {self.ronda}  | Puntaje acumulado: {self.puntaje}")
         
     # Solicitar longitud con validación 
    def _pedir_longitud(self) -> int:
        entrada = input("\n Ingresa la cantidad de caracteres de la contraseña (mínimo 8): ").strip()
        
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

        resultado=""
        try:
            longitud = self._pedir_longitud()

            pwd = input(
                "\nEscribe tu contraseña: ")

            password = Password( longitud,pwd)
            password.validar()

            # Determinar cofre según longitud

            if longitud == 8:
                cofre = Cofre("Común")

            elif longitud == 12:
                cofre = Cofre("Raro")

            elif longitud >= 14:
                cofre = Cofre("Legendario")

            else:
                cofre = Cofre("Común")

            self.puntaje += cofre.puntos

            resultado=f"✅ Correcta → {cofre}"

            print("\n✅ Contraseña válida")
            print(cofre)

        except (TipoDatoInvalidoError,LongitudInvalidaError,
                PasswordInvalidoError) as e:
            
            print(f"\n❌ {e}")

            cofre = Cofre.abrir_maldito()

            self.puntaje += cofre.puntos

            resultado=f"❌ Inválida → {cofre}"

            print(cofre)


        self.historial.append({
            "ronda":self.ronda,
            "modo": "Generar",
            "resultado":resultado,
            "puntaje":self.puntaje
            })

        print(f"\nPuntaje actual: {self.puntaje}")
        
        
    def _descifrar_password(self):
        self._separador()
        print("""\nDESCIFRAR CONTRASEÑA""")

        longitud = 8

        password = Password(longitud)

        pwd_secreto=password.generar()

        intentos=7
        
        resultado = ""
        
        self.ronda += 1
        # estado visible tipo ahorcado
        progress = ["_"] * longitud
        
        print(f"\nPista inicial:")
        print(f"✓ Longitud: {longitud}")
        print("✓ Tiene mayúsculas")
        print("✓ Tiene minúsculas")
        print("✓ Tiene números")
        print("✓ Tiene caracteres especiales '¿¡?=)(/*+-%&$#!' ")

        while intentos > 0:
            
            print(f"\nPista actual: ")
            print(" ".join(progress))
            
            print(f"\nIntentos restantes: {intentos}")
            intento=input("\nAdivina la contraseña: ")

            if intento == pwd_secreto:
                
                puntos_ganados = 50
                self.puntaje += puntos_ganados
                resultado = (f"Descifrada (+{puntos_ganados})")
                print("\n🎉 ¡Correcto!")
                print("✅Has descifrado la contraseña")
                print(f"\nGanaste {puntos_ganados} puntos.")
                print(f"Puntaje actual: {self.puntaje}")
                
                self.historial.append({
                    "ronda" : self.ronda,
                    "modo" : "Descifrar",
                    "resultado": resultado,
                    "puntaje": self.puntaje})
                
                return
                        
            # uscar caracteres existentes
            for c in intento: 
                if c in pwd_secreto:
                    posicion = pwd_secreto.index(c)
                    
                    progress[posicion] = c
                

            intentos-=1

            print("\n❌ Incorrecto")

        print("\nHas agotado tus intentos")

        print(f"Contraseña correcta: {pwd_secreto}")
        
        cofre = Cofre.abrir_maldito()
        self.puntaje += cofre.puntos
        resultado = f"❌ Falló ({cofre})"
        print(f"Pntaje total: {self.puntaje}")
        
        self.historial.append({
            "ronda": self.ronda,
            "modo":"Descifrar",
            "resultado": resultado,
            "puntaje": self.puntaje})
       
               
    def _generar_pistas(self, secreta, intento):
        posiciones=[]

        correctos=0

        for i in range(len(secreta)):
            if i < len(intento):
                if intento[i]==secreta[i]:
                    posiciones.append(intento[i])

                    correctos +=1

                else:
                    posiciones.append("_")

        return correctos, " ".join(posiciones)
        
   
    def _generar_pistas(self, secreta, intento):
        posiciones=[]

        correctos=0

        for i in range(len(secreta)):
            if i < len(intento):
                if intento[i]==secreta[i]:

                    posiciones.append(intento[i])

                    correctos +=1

                else:
                    posiciones.append("_")

        return correctos, " ".join(posiciones)
        
        
    # ── Menú y vistas secundarias ─────────────────────────
 
    def _mostrar_menu(self):
        """Muestra las opciones del menú principal."""
       
        print("\n  │      MENÚ PRINCIPAL         │")
     
        print("  │  1. Generar contraseña      │")
        print("  │  2. Decifrar contraseña     │")
        print("  │  3. Ver historial           │")
        print("  │  4. Salir del juego         │")
     
 
    def _ver_historial(self):
        """Muestra el historial completo de todas las rondas jugadas."""
        self._separador()
        
        if not self.historial:
            print("\n  No hay rondas jugadas aún.")
            return 
        
        print("\n  HISTORIAL DE RONDAS\n")
        print(f"  {'Ronda':<8} | {'Modo':<15} | {'Resultado de contraseña':<32} | {'Puntaje'}")
        print("  " + "-" * 70)
        
        for h in self.historial:
            ronda = h.get("ronda","-")
            modo = h.get("modo","Generar")
            resultado = h.get("resultado","Sin resultado")
            puntaje = h.get("Puntaje",0)
            
            print(f"  {h['ronda']:<8} | {h['modo']:<15} | {h['resultado']:<32} | {h['puntaje']}")
 
 
 
    def _mostrar_resultado_final(self):
        """Muestra la pantalla de despedida con el puntaje final y una calificación."""
        self._separador()
        print("\n  FIN DEL JUEGO\n")
        print(f"  Rondas jugadas : {self.ronda}")
        print(f"  Puntaje final  : {self.puntaje}")
 
        # Calificación según puntaje final
        if self.puntaje >= 10:
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
            opcion = input("\n  Elige una opción (1/2/3/4): ").strip()
 
            if opcion == "1":
                self._jugar_ronda()
            
            elif opcion == "2":
                self._descifrar_password()
 
            elif opcion == "3":
                self._ver_historial()
 
            elif opcion == "4":
                jugando = False
 
            else:
                print("\n   Opción no válida. Por favor elige 1, 2, 3 o 4.")
 
        self._mostrar_resultado_final()
