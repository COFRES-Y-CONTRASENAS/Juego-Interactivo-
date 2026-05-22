#----------------------------------------------------
# ARCHIVO: main.py 
# Archivo principal del juego cazador de contraseñas.
#----------------------------------------------------
import random
from password import Password
from cofre import Cofre
from cazador import Cazador
from exceptions import LongitudInvalidaError, TipoDatoInvalidoError

def main():
    print("BIENVENIDO AL CAZADOR DE CONTRASEÑAS\n")
    
    nombre = input("¿Cómo te llamas, cazador? ").strip()
    if not nombre:
        nombre = "Cazador"
    
    cazador = Cazador(nombre)

    print(f"\n¡Bienvenido, {cazador.nombre}!\n")

    while True:
        try:
            print("\n" + "-"*55)
            print("1. Generar contraseña y abrir cofre")
            print("2. Ver mis estadísticas")
            print("3. Salir del juego")
            print("-"*55)
            
            opcion = input("\nSelecciona una opción: ").strip()

            if opcion == "1":
                # Pedir longitud
                longitud_input = input("\nIngresa la longitud de la contraseña (mínimo 8): ").strip()
                
                if not longitud_input.isdigit():
                    raise TipoDatoInvalidoError()
                
                longitud = int(longitud_input)
                
                # Crear y generar contraseña
                pwd = Password(longitud)
                pwd.generar()
                
                print(f"\nContraseña generada: {pwd.valor}")
                
                es_valida, mensaje = pwd.validar()
                
                # Decidir tipo de cofre
                if es_valida:
                    prob = random.random()
                    if prob < 0.5:
                        cofre = Cofre("Común")
                    elif prob < 0.85:
                        cofre = Cofre("Raro")
                    else:
                        cofre = Cofre("Legendario")
                else:
                    cofre = Cofre("Maldito")
                    print(f"{mensaje}")

                cazador.abrir_cofre(cofre)

            elif opcion == "2":
                cazador.mostrar_estado()

            elif opcion == "3":
                print(f"\n¡Gracias por jugar, {cazador.nombre}!")
                cazador.mostrar_estado()
                break

            else:
                print("Opción no válida. Intenta de nuevo.")

        except (LongitudInvalidaError, TipoDatoInvalidoError) as e:
            print(f"\n {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()