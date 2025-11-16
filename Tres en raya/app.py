from ttt_core import *

def main():
    jugando=True
    while jugando==True:
        print("--- MODOS DE JUEGO ---")
        print("1. JUGADOR VS JUGADOR")
        print("2. JUGADOR VS CPU")
        opcion=input("¿A que quieres jugar?: ")
        if opcion=="1":
            jugador_vs_jugador()
        elif opcion=="2":
            jugador_vs_cpu()
        else:
            print("Opción inválida.")
        otra=input("¿Quieres echarte otra partiduki? (s/n): ").lower()
        if otra != "s":
            jugando=False
    print("¡Nos vemos!")

main()