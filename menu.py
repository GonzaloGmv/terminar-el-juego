def nivel():
    print("1 - Nivel simple")
    print("2 - Nivel intermedio")
    print("3 - Nivel avanzado")
    print("4 - Nivel experto")
    while True:
        lvl = input("Elija el nivel deseado: ")
        try:
            lvl = int(lvl)
        except:
            pass
        else:
            if 1 <= lvl <= 4:
                break
    return lvl