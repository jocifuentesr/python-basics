import os

# precios 
chica = 3500
mediana = 4500
grande = 5500

cont = 0
total = 0
menu_flag = False

while not menu_flag:
    os.system('cls')
    print("Sistema de venta de indentificadores de mascotas")
    print("1. Comprar un identificador")
    print("2. Salir")
    opt_menu = int(input("Ingrese su opción: "))
    if opt_menu == 1:
        os.system('cls')
        print("Indique la placa que necesita comprar")
        print("1. Chica $3.500 ")
        print("2. Mediana $4.500")
        print("3. Grande $5.500")
        opt_submenu = int(input("Seleccione su opción: "))

        if opt_submenu == 1:
            total += chica
            cont += 1
            input("Ingrese el nombre de su mascota: ") # no se guarda el nombre 
            os.system('cls')
        elif opt_submenu == 2:
            total += mediana
            cont += 1
            input("Ingrese el nombre de su mascota: ") # no se guarda el nombre 
            os.system('cls')
        elif opt_submenu == 3:
            total += grande
            cont += 1
            input("Ingrese el nombre de su mascota: ") # no se guarda el nombre 
            os.system('cls')
        else:
            print("La opción no es correcta")
            os.system('cls')
    else: 
        menu_flag = True
        os.system('cls')

# resumen de la compra
print("Gracias por su compra")
print(f"Compró {cont} identificadores")
print(f"El total de su compra es: ${total}")
if total >= 10000:
    print("Su compra tiene despacho gratuito")
else: 
    print("Su compra tiene un cargo por despacho de $2.000")
    print(f"El monto total a pagar es ${total + 2000}")