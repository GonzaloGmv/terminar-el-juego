def pedir_numero(MIN,MAX):
    while True:
        respuesta = input("Escriba un numero entre " + str(MIN) + " y " + str(MAX) + ": ")
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
        ayuda = input("Si desea ayuda para adivinar el numero escriba SI, si no la desea escriba NO: ")
        try:
           ayuda = str(ayuda)
        except:
            pass
        else:
            if ayuda == "SI":
                while True:
                    intento = pedir_numero(MIN, MAX)
                    if intento < NUM:
                        print("Te has quedado corto")
                    elif intento > NUM:
                        print("Te has pasado")
                    else:
                        break
            elif ayuda == "NO":
                while True:
                    intento = pedir_numero(MIN, MAX)
                    if intento == NUM:
                        break
            print("Has acertado")
            break