"""
Ingrese tres números enteros, si son mayores a cero y par, 
entonces súmelos, sino cuéntelos
"""
print("\n")
print("-" * 50)
print("Este programa le pide que ingrese tres números enteros")
print("Sumará los números mayores a cero y pares")
print("Contará a los que no cumplen con la condición anterior")
print("-" * 50)

num1 = int(input("\nIngrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tecer número: "))

suma = 0
cont = 0

if num1 > 0 and num1 % 2 == 0:
    suma = suma + num1
else:
    cont = cont + 1

if num2 > 0 and num2 % 2 == 0:
    suma = suma + num2
else:
    cont = cont + 1

if num3 > 0 and num3 % 2 == 0:
    suma = suma + num1
else:
    cont = cont + 1

print(f"La suma de los números que cumplen con la condición es: {suma}")
print(f"La cantidad de números que no cumplen con la condición es: {cont} ")
print("\n")