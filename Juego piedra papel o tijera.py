from random import choice

eleccion = input("Que elijes? (piedra, papel o tijeras)")
juego = ["piedra", "papel", "tijeras"]
respuesta = choice(juego)

print(f"Tú elegiste: {eleccion}")
print(f"La computadora eligió: {respuesta}")

if eleccion == "piedra" and respuesta == "papel":
    print('Perdiste')
elif eleccion == "piedra" and respuesta == "tijeras":
    print('Ganaste')
elif eleccion == "papel" and respuesta == "tijeras":
    print('Perdiste')
elif eleccion == "papel" and respuesta == "piedra":
    print('Ganaste')
elif eleccion == "tijeras" and respuesta == "piedra":
    print('Perdiste')
elif eleccion == "tijeras" and respuesta == "papel":
    print('Ganaste')
elif eleccion == respuesta:
    print("intentalo de nuevo")
else:
    print("Rango desconocido")