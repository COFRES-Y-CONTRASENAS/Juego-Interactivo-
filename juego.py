#----------------------------------------------------
# ARCHIVO: juego.py 
# Este módulo controla el flujo del juego. 
# Administra los modos de juego, las rondas jugadas, asigna el puntaje del jugador, 
# guarda el historial de rondas y permite al usuario jugar tantas rondas como lo desee. 
#----------------------------------------------------

# Importaciones de las clases y metodos de los archivos password.py, cofre.py 
# y las excepciones personalizadas del archivo exceptions.py.
from password import Password
from cofre import Cofre
from exceptions import (LongitudInvalidaError,TipoDatoInvalidoError,
                        PasswordInvalidoError)

# Esta clase principal representa al jugador y su progreso.
class Juego_Cazador:
    
    # Anuncio de bienvenida al jugador.
    BANNER = """
     
    CAZADOR DE CONTRASEÑAS
                 
El juego consiste en generar y descifrar contraseñas, abrir 
cofres y acumular puntos. Si cometes un error perderas tus puntos.


¡Vamos a jugar!
    
    """  
    # Constructor que inicialia las variales de puntaje, ronda y el historial de juego.
    def __init__(self):
        
        self.puntaje = 0
        self.ronda = 0
        self.historial = []  # Lista donde se almacenan las rondas jugadas.
    
    # El metodo separado genera una linea docorativa.
    def _separador(self):
        print("\n" + "─" * 84)
    
    # El metodo mostrar_estado muestra la información del jugador, 
    # la ronda actual y los puntos acumulados.
    def _mostrar_estado(self):
         print(f"\n  Ronda: {self.ronda}  | Puntaje acumulado: {self.puntaje}")
         
     # Este metodo solicita al usuario la longitud de la contraseña.
    def _pedir_longitud(self) -> int:
        
        # Variable que recibirá la cantidad suministrada por el usuario.
        entrada = input("\n Ingresa la cantidad de caracteres de la contraseña (mínimo 8): ").strip()
        
        # Validar que sea un entero positivo.
        if not entrada.isdigit():
            raise TipoDatoInvalidoError( f"'{entrada}' no es un número válido. "
                "Debes ingresar un entero positivo.")

        # Asigna el valor suministrado por el usuario a la variable longitud.
        longitud = int(entrada)
        
        # Validar longitud mínima de 8
        if longitud < 8:
            raise LongitudInvalidaError(f"La longitud mínima permitida es 8. Ingresaste: {longitud}.")

        return longitud
    
    # Este metodo ejecuta el modo de juego generar contraseña
    def _jugar_ronda(self):
        
        # Se incrementa la ronda.
        self.ronda += 1
        self._separador() 
        print(" GENERA CONTRASEÑAS Y GANA PUNTOS ")
        self._mostrar_estado()

        resultado=""
        try:
            longitud = self._pedir_longitud()
            
            # Se solicita la contraseña al usuario.
            pwd = input("\nEscribe tu contraseña: ")
            
            # se crea un objeto de la clase Password.
            password = Password( longitud,pwd)
            password.validar()

            # Determinar tipo de cofre según longitud suministrada por el usuario.
            if 8 <= longitud < 12:
                cofre = Cofre("Común")

            elif 12 <= longitud < 14:
                cofre = Cofre("Raro")

            else: 
                cofre = Cofre("Legendario")
                
            # Se actualizan los puntos 
            self.puntaje += cofre.puntos

            resultado = f"✅ Correcta → {cofre}"

            print("\n✅ Contraseña válida")
            print(cofre)
        
        # Se guarda el error en la variable e.
        except (TipoDatoInvalidoError,LongitudInvalidaError,
                PasswordInvalidoError) as e:
            
            # Se muestra el error específico que cometió el usuario.
            print(f"\n❌ {e}")

            # Se llama al metodo abrir_maldito para restar los puntos.
            cofre = Cofre.abrir_maldito()

            self.puntaje += cofre.puntos

            resultado = f"❌ Inválida → {cofre}"
            print(cofre)

        # Se guarda la información en el historial.
        self.historial.append({
            "ronda":self.ronda,
            "modo": "Generar",
            "resultado":resultado,
            "puntaje":self.puntaje
            })

        print(f"\nPuntaje actual: {self.puntaje}")
        
    # Este metodo se encarga del modo de juego descifrar contraseña.
    def _descifrar_password(self):
        
        self._separador()
        print("""\nDESCIFRAR CONTRASEÑA""")
        
        # longitud de la contraseña estalecido. Este valor no cambia.
        longitud = 8
               
        password = Password(longitud)
        pwd_secreto=password.generar()
        
        # Cantidad de intentos permitidos por el sistema.
        intentos=7
        # Variable que guardará la contraseña generada por el usuario.
        resultado = ""
        
        self.ronda += 1
        # Estado visible tipo ahorcado.
        progress = ["_"] * longitud
        
        print(f"\nPista inicial:")
        print(f"✓ Longitud: {longitud}")
        print("✓ Tiene mayúsculas")
        print("✓ Tiene minúsculas")
        print("✓ Tiene números")
        print("✓ Tiene caracteres especiales '¿¡?=)(/*+-%&$#!' ")

        # Creamos un bucle while que nos permitirá validar la cantidad 
        # de intentos permitidos para descifrar la contraseña.
        while intentos > 0:
            
            print(f"\nPista actual: ")
            print(" ".join(progress))
            
            print(f"\nIntentos restantes: {intentos}")
            intento=input("\nAdivina la contraseña: ")

            # Se verifica si el intento ingresado por el usuario coincide 
            # con la contraseña secreta generada por el sistema.
            if intento == pwd_secreto:
                
                puntos_ganados = 50
                # Se suman los puntos obtenidos al puntaje total del jugador.
                self.puntaje += puntos_ganados
                resultado = f"✅ Descifrada (+{puntos_ganados})"
                print("\n🎉 ¡Correcto!")
                print("✅ Has descifrado la contraseña")
                print(f"\nGanaste {puntos_ganados} puntos.")
                print(f"Puntaje actual: {self.puntaje}")
                
                # Se guarda el resultado en el historial. 
                self.historial.append({
                    "ronda" : self.ronda,
                    "modo" : "Descifrar",
                    "resultado": resultado,
                    "puntaje": self.puntaje})
                
                return
                        
            # Buscar caracteres existentes
            for c in intento: 
                if c in pwd_secreto:
                    posicion = pwd_secreto.index(c)
                    
                    progress[posicion] = c
                
            # Resta los intentos permitidos.
            intentos-=1

            print("\n❌ Incorrecto")

        print("\nHas agotado tus intentos")

        print(f"Contraseña correcta: {pwd_secreto}")
        
        cofre = Cofre.abrir_maldito()
        self.puntaje += cofre.puntos
        resultado = f"❌ Falló ({cofre})"
        print(f"Puntaje total: {self.puntaje}")
        
        self.historial.append({
            "ronda": self.ronda,
            "modo":"Descifrar",
            "resultado": resultado,
            "puntaje": self.puntaje})
               
    # Este método genera pistas comparando el intento del jugador con la contraseña secreta.
    def _generar_pistas(self, secreta, intento):
        
        # Lista que almacenará las letras correctas 
        posiciones=[]
        # Contador de caracteres acertados.
        correctos=0
        
        # Se recorre cada posición de la contraseña secreta.
        for i in range(len(secreta)):
            if i < len(intento):
                if intento[i]==secreta[i]:

                    posiciones.append(intento[i])

                    correctos +=1

                else:
                    posiciones.append("_")
        # devuelve la cantidad de aciertos y la pista construida.
        return correctos, " ".join(posiciones)
    
    # Este método muestra las opciones del menú principal.
    def _mostrar_menu(self):
       
        print("\n  │      MENÚ PRINCIPAL         │")
     
        print("  │  1. Generar contraseña      │")
        print("  │  2. Decifrar contraseña     │")
        print("  │  3. Ver historial           │")
        print("  │  4. Salir del juego         │")
     
    # El método ver_historial muestra el historial de todas las rondas jugadas
    def _ver_historial(self):
        """Muestra el historial completo de todas las rondas jugadas."""
        self._separador()
        # Se valida si el historial esta vacio 
        if not self.historial:
            print("\n  No hay rondas jugadas aún.")
            return 
        
        print("\n  HISTORIAL DE RONDAS\n")
        print(f"  {'RONDA':<8} | {'MODO':<15} | {'RESULTADO ':<42}  | {'PUNTAJE'}")
        print(" " + "-" * 84)
        
        for h in self.historial:
                      
            print(f"  {h['ronda']:<8} | {h['modo']:<15} | {h['resultado']:<42} | {h['puntaje']}")
 
 
    # Este método muestra por sonsola el mensaje de despedida con el puntaje final y 
    def _mostrar_resultado_final(self):
        
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
 
    # Metodo principal que lanza el juego y controla el bucle central.
    # Muestra el mensaje inicial del juego y el menú de opciones a elegir.    
    def iniciar(self):
        # Imprime en consola el mensaje inicial.
        print(self.BANNER)
        
        # Se crea la variabel jugando con el valor de verdadero. 
        jugando = True
        
        # Se crea aun ciclo while para que el usuario permanezca en el menú principal 
        # mientras que la variable jugando sea igual a True, si se le asigna el valor de False
        # sale del ciclo y se imprime el mensaje de despedida.
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
