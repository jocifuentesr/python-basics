print("\n")
num = int(input("Ingrese un número de 1 a 999: "))

if num >=1 and num < 10:
    print("El número ingresado es de un dígito")
elif num >=10 and num < 100:
    print("El número ingresado es de dos dígitos")
else: 
    print("El número ingresado es de tres dígitos")
print("\n")