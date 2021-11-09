import random
def pedir_numero(MIN,MAX):
    while True:
        respuesta = input("Escriba un numero entre " + str(MIN) + " y " + str(MAX))
        try:
            respuesta = int(respuesta)
        except:
            pass
        else:
            if MIN <= respuesta <= MAX:
                break
    return respuesta

def adivinar(MIN, MAX, NUM):
    while True:
        intento = pedir_numero(MIN, MAX)
        if intento < NUM:
            print("Te has quedado corto")
        elif intento > NUM:
            print("Te has pasado")
        else:
            print("Has acertado")
            break
    return intento

print("1 - Nivel simple")
print("2 - Nivel intermedio")
print("3 - Nivel avanzado")
print("4 - Nivel experto")
while True:
    nivel = input("Elija el nivel deseado: ")
    try:
        nivel = int(nivel)
    except:
        pass
    else:
        if 1 <= nivel <= 4:
            break

if nivel == 1:
    intent1 = adivinar(0, 100, random.randrange(0, 101))
elif nivel == 2:
    intent2 = adivinar(0, 1000, random.randrange(0, 1001))
elif nivel == 3:
    intent3 = adivinar(0, 1000000, random.randrange(0, 1000001))
elif nivel == 4:
    intent4 = adivinar(0, 1000000000000, random.randrange(0, 1000000000001))