# ejemplo while
# numero = int(input("Ingrese un número positivo: "))
# while numero < 0:
#     print("El número es negativo. Intente de nuevo")
#     numero = int(input("Ingrese un número positivo :"))

# identificar una persona
# nombre = input("Ingrese su nombre: ")
# while nombre != "Juan":
#     print("No es la persona que busco. Intente de nuevo")
#     nombre = input("Ingrese su nombre: ")

# muestra una secuencia de los primeros 10 números naturales
inicio = 0
fin = 20
while (inicio < fin):
    print(inicio)
    if inicio == 10:
        print("romper la secuencia en la iteración 10")
        break
    inicio = inicio + 1