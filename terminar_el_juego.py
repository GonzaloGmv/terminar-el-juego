import random, juego, menu

print("1 - Nivel simple")
print("2 - Nivel intermedio")
print("3 - Nivel avanzado")
print("4 - Nivel experto")

nivel = menu.nivel()

if nivel == 1:
    intent1 = juego.adivinar(0, 100, random.randrange(0, 101), 10)
elif nivel == 2:
    intent2 = juego.adivinar(0, 1000, random.randrange(0, 1001), 20)
elif nivel == 3:
    intent3 = juego.adivinar(0, 1000000, random.randrange(0, 1000001), 30)
elif nivel == 4:
    intent4 = juego.adivinar(0, 1000000000000, random.randrange(0, 1000000000001), 40)