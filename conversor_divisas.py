print("Conversor de divisas")
flag = False
cont = 0
dolar = 801.6
euro = 875.4
uf = 28993.7
while not flag:
    print("\nIndique la divisa de origen")
    print("1. Dólares")
    print("2. Euro")
    print("3. UF")
    print("4. Salir")
    opcion = int(input("seleccione su opción: "))

    if opcion == 1:
        print("\nIndique la conversión que desea realizar")
        print("1. Dólares a Euro")
        print("2. Dólares a UF")
        opcion = int(input("Selecciones su opción: "))
        if opcion == 1:
            dolares = float(input("Indique la cantidad de dólares que quiere convertir: "))
            print(f"{dolares} dolares en euros son: {round(dolares * 0.9156956819739548, 2)} ")
        elif opcion == 2:
            dolares = float(input("Indique la cantidad de dólares que quiere convertir: "))
            print(f"{dolares} dolares en UF son: {round((dolares * dolar) / uf), 2} ")
        else:
            print("La opción ingresada no es correcta")
        cont = cont + 1
        if cont == 4:
            print("Superó la cantidad máxima de uso")
            break

    if opcion == 4:
        flag = True
