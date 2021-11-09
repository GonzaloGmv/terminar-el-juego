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

def 
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
    
elif nivel == 2:

elif nivel == 3:
    
elif nivel == 4: