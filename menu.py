def nivel():
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