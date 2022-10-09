import os 

menu_flag = False 
frenos_flag = False 
aceite_flag = False
motor_flag  = False
luces_flag = False

total = 0

# precio servicios
frenos = 1500
aceite = 1000
motor = 2000
luces = 3000

while not menu_flag:
    os.system('cls')
    print("Servicios de mantenimiento automotriz")
    print("1. Frenos $1.500")
    print("2. Aceite $1.000")
    print("3. Motor $2.000")
    print("4. Luces $3.000")
    print("5. Salir")
    opt_menu = int(input("Ingrese su opción: "))
    if opt_menu == 1:
        if frenos_flag == False:
            print("Acaba de contratar un servicio de revisión de frenos por $1.500")
            input("Presione una tecla para continuar...")
            total += frenos
            frenos_flag = True
        else: 
            print("Este servicio ya fue contratado anteriormente")
            input("Presione una tecla para continuar...")

    if opt_menu == 2:
        if aceite_flag == False:
            print("Acaba de contratar un servicio de revisión de aceite $1.000")
            input("Presione una tecla para continuar...")
            total += aceite
            aceite_flag = True
        else: 
            print("Este servicio ya fue contratado anteriormente")
            input("Presione una tecla para continuar...")

    if opt_menu == 3:
        if motor_flag == False:
            print("Acaba de contratar un servicio de revisión de motor por $2.000")
            input("Presione una tecla para continuar...")
            total += motor
            motor_flag = True
        else: 
            print("Este servicio ya fue contratado anteriormente")
            input("Presione una tecla para continuar...")

    if opt_menu == 4:
        if luces_flag == False:
            print("Acaba de contratar un servicio de revisión de luces por $3.000")
            input("Presione una tecla para continuar...")
            total += luces
            luces_flag = True
        else: 
            print("Este servicio ya fue contratado anteriormente")
            input("Presione una tecla para continuar...")
    elif opt_menu == 5:
        print("A continuación podrá ver el detalle de su compra")
        input("Presione una tecla para continuar...")
        menu_flag = True
    else: 
        print("La opción ingresada no es correcta")

# Resumen de la compra
os.system('cls')
print(f"El total a pagar por los servicios contratados es: ${total}")
print("¿El auto ingresado es de la marca Mazda o Toyota?")
print("1. Sí")
print("2. No")
opt_marca = int(input("Seleccione una opción: "))

if opt_marca == 1:
    print(f"Se aplicó un descuento de un 10%. Total a pagar: ${round(total * 0.9)}") 
    print("Muchas gracias por usar nuestros servicios")
else: 
    print("Muchas gracias por usar nuestros servicios")