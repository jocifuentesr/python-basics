salir = False
while not salir:
    print(" Calculadora")
    print("=" * 20)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("=" * 20)
    opcion = int(input("Ingrese la operación: "))
    if opcion == 1:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        resultado = n1 + n2
        print(f"El resultado de sumar {n1} y {n2} es: {resultado}")
        print("Presione Enter para continuar ...")
        continue

    if opcion == 2:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        resultado = n1 - n2
        print(f"El resultado de restar {n1} y {n2} es: {resultado}")
        print("Presione Enter para continuar ...")
        continue

    if opcion == 3:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        resultado = n1 * n2
        print(f"El resultado de multiplicar {n1} y {n2} es: {resultado}")
        print("Presione Enter para continuar ...")
        continue

    if opcion == 4:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        while n2 == 0:
            print("El divisor no puede ser igual a cero")
            n2 = float(input("Ingrese el divisor nuevamente: "))
        resultado = n1 / n2
        print(f"El resultado de dividir {n1} y {n2} es: {resultado}")
        print("Presione Enter para continuar ...")
        continue

    if opcion == 5:
        salir = True
    else:
        print("Opción no válida. Intente nuevamente")
        print("Presione Enter para continuar")
