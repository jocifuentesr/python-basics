cont = 0

# primer número
num1 = int(input("Ingrese primer número: "))
if num1 % 2 == 0:
    cont = cont + 1
# segundo número
num2 = int(input("Ingrese segundo número: "))
if num2 % 2 == 0:
    cont = cont + 1

# tercer número
num3 = int(input("Ingrese tercer número: "))
if num3 % 2 == 0:
    cont = cont + 1

print(f"La cantidad de números pares es: {cont}")