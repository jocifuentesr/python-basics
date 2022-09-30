# productos
agua = 600
azucar = 1200
aceite = 1500
arroz = 1250
fideos = 790
bebida = 1780
chocolate = 2500
pan_molde = 1340

suma = 0
cont = 0
flag = False

print("\n")
print("Por favor indique los productos que necesita")

print("\n¿Desea llevar agua?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + agua
    suma = suma + agua

print("\n¿Desea llevar azucar?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + azucar
    suma = suma + azucar

print("\n¿Desea llevar aceite?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + aceite
    suma = suma + aceite

print("\n¿Desea llevar arroz?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + arroz
    suma = suma + arroz

print("\n¿Desea llevar fideos?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + fideos
    suma = suma + fideos

print("\n¿Desea llevar bebida?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + bebida
    suma = suma + bebida

print("\n¿Desea llevar chocolate?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + chocolate
    suma = suma + chocolate

print("\n¿Desea llevar pan molde?")
print("1: Sí")
print("2: No")
pedido = int(input("ingrese su opción: "))
if pedido == 1:
    cont = cont + pan_molde
    suma = suma + pan_molde

print("\n¿Es cliente preferencial?")
print("1: Sí")
print("2: No")
preferencial = int(input("ingrese su opción: "))
if preferencial == 1:
    total = suma * 0.85
    print(f"El total a pagar con un descuento de un 25% es: {round(total)} ")
    efectivo = int(input("Ingrese el efectivo disponible para el pago: "))
    if efectivo > total:
        print("¡Muchas gracias por su compra!")
        print(f"Su vuelto es: ${round(efectivo - total)}")
    else: 
        print("Dinero insuficiente")
else:
    print(f"El total a pagar es suma: {round(suma)}")
    efectivo = int(input("Ingrese el efectivo disponible para el pago: "))
    if efectivo > suma:
        print("¡Muchas gracias por su compra!")
        print(f"Su vuelto es: ${round(efectivo - suma)}")
    else: 
        print("Dinero insuficiente")
