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
    minim = MIN
    maxim = MAX
    n_intentos = 0
    ganar = False
    while True:
        oportunidades = input("Escriba el numero maximo de intentos que desea: ")
        try: oportunidades = int(oportunidades)
        except:
            pass
        else:
            if oportunidades > 0:
                break
    while True:
        ayuda = input("Si desea ayuda para adivinar el numero escriba SI, si no la desea escriba NO: ")
        try:
           ayuda = str(ayuda)
        except:
            pass
        else :
            if ayuda == "SI" or ayuda == "NO":
                if ayuda == "SI":
                    while not ganar and n_intentos < oportunidades:
                        intento = pedir_numero(MIN, MAX)
                        n_intentos = n_intentos + 1
                        if intento < NUM:
                            if intento > minim:
                                minim = intento
                            print("El numero esta entre ", minim, " y ", maxim)
                        elif intento > NUM:
                            if intento < maxim:
                                maxim = intento
                            print("El numero esta entre ", minim, " y ", maxim)
                        else:
                            print("Has acertado en ", n_intentos, " intentos")
                            ganar = True
                    if not ganar:
                        print("Has superado el numero maximo de intentos")
                elif ayuda == "NO":
                    while not ganar and n_intentos < oportunidades:
                        intento = pedir_numero(MIN, MAX)
                        n_intentos = n_intentos + 1
                        if intento < NUM:
                            print("Te has quedado corto")
                        elif intento > NUM:
                            print("Te has pasado")
                        else:
                            print("Has acertado en ", n_intentos, " intentos")
                            ganar = True
                    if not ganar:
                        print("Has superado el numero maximo de intentos")
                break  