import random

print("🎮 PIEDRA, PAPEL O TIJERA 🎮")

opciones = ["piedra", "papel", "tijera"]

victorias = 0
derrotas = 0

while True:
    jugador = input("\nElige piedra, papel o tijera: ").lower()

    if jugador not in opciones:
        print("❌ Opción no válida.")
        continue

    computadora = random.choice(opciones)

    print(f"🤖 La computadora eligió: {computadora}")

    if jugador == computadora:
        print("🤝 ¡Empate!")

    elif (
        (jugador == "piedra" and computadora == "tijera")
        or (jugador == "papel" and computadora == "piedra")
        or (jugador == "tijera" and computadora == "papel")
    ):
        print("🎉 ¡Ganaste!")
        victorias += 1

    else:
        print("😢 ¡Perdiste!")
        derrotas += 1

    print(f"🏆 Victorias: {victorias} | Derrotas: {derrotas}")

    continuar = input("\n¿Quieres jugar otra vez? (si/no): ").lower()

    if continuar != "si":
        print("👋 ¡Gracias por jugar!")
        break