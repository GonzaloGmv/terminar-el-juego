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
    ganar = False
    while True:
        ayuda = input("Si desea ayuda para adivinar el numero escriba SI, si no la desea escriba NO: ")
        try:
           ayuda = str(ayuda)
        except:
            pass
        else :
            if ayuda == "SI" or ayuda == "NO":
                if ayuda == "SI":
                    while not ganar:
                        intento = pedir_numero(MIN, MAX)
                        if intento < NUM:
                            print("Te has quedado corto")
                        elif intento > NUM:
                            print("Te has pasado")
                        else:
                            print("Has acertado")
                            ganar = True
                elif ayuda == "NO":
                    while not ganar:
                        intento = pedir_numero(MIN, MAX)
                        if intento == NUM:
                            print("Has acertado")
                            ganar = True
                break  