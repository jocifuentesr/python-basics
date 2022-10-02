# TIPO DE CLIENTE
print("SISTEMA DE VENTAS")
print("-" * 40)
print("PREGUNTE AL CLIENTE SI ES PREFERENCIAL")
print("-" * 40)
print("1. Cliente preferencial")
print("2. Cliente no preferencial")
opcion = int(input("Seleccione una opción: "))
preferente = False
if opcion == 1:
    preferente = True
    print("Cliente registrado como preferente. Aplica descuento")
else:
    print("Cliente no es preferente")


# TIPO Y CANTIDAD DE ENTRADAS
print("-" * 40)
print("TIPO DE ENTRADA")
print("-" * 40)
print("1. Estreno")
print("2. Normal")
opcion = int(input("Seleccione una opción: "))
estreno = False
if opcion == 1:
    estreno = True
    print("Cliente compra entradas para estreno")
else:
    print("Cliente compra entradas para función normal")

precio_estreno = 9500
precio_normal = 5300

cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))
if estreno:
    costo_entradas = cantidad_entradas * precio_estreno
else:
    costo_entradas = cantidad_entradas * precio_normal

if preferente:
    precio_pago = costo_entradas * 0.7
    print(f"El valor a pagar por {cantidad_entradas} entradas es: {round(precio_pago)}. Descuento aplicado")
else:
    precio_pago = costo_entradas
    print(f"El valor a pagar por {cantidad_entradas} entradas es: {round(precio_pago)}")


# PALOMITAS
print("-" * 40)
print("AGREGUE PALOMITAS AL PEDIDO")
print("-" * 40)
print("¿El cliente desea palomitas?")
print("1. chicas")
print("2. medianas")
print("3. grandes")
print("4. No desea palomitas")
opcion = int(input("Ingrese su opción: "))
if opcion == 1:
    chicas = 3700
    print("Ingrese la cantidad de palomitas chicas: ")
    cantidad = int(input())
    precio_palomitas = cantidad * chicas
    print(f"El precio a pagar es: {precio_palomitas}")
elif opcion == 2:
    medianas = 4800
    print("Ingrese la cantidad de palomitas medianas: ")
    cantidad = int(input())
    precio_palomitas = cantidad * medianas
    print(f"El precio a pagar es: {precio_palomitas}")
elif opcion == 3:
    grandes = 8200
    print("Ingrese la cantidad de palomitas grandes: ")
    cantidad = int(input())
    precio_palomitas = cantidad * grandes
    print(f"El precio a pagar es: {precio_palomitas}")
else:
    print("No desea palomitas")
    precio_palomitas = 0


# BEBIDAS
print("-" * 40)
print("AGREGUE BEBIDAS AL PEDIDO")
print("-" * 40)
print("¿El cliente desea bebidas?")
print("1. chicas")
print("2. medianas")
print("3. grandes")
print("4. No desea bebidas")
opcion = int(input("Ingrese su opción: "))
if opcion == 1:
    chicas = 2500
    print("Ingrese la cantidad de bebidas chicas: ")
    cantidad = int(input())
    precio_bebidas = cantidad * chicas
    print(f"El precio a pagar es: {precio_bebidas}")
elif opcion == 2:
    medianas = 4000
    print("Ingrese la cantidad de bebidas medianas: ")
    cantidad = int(input())
    precio_bebidas = cantidad * medianas
    print(f"El precio a pagar es: {precio_bebidas}")
elif opcion == 3:
    grandes = 6000
    print("Ingrese la cantidad de bebidas grandes: ")
    cantidad = int(input())
    precio_bebidas = cantidad * grandes
    print(f"El precio a pagar es: {precio_bebidas}")
else:
    print("No desea palomitas")
    precio_bebidas = 0


# RESUMEN DE PRODUCTOS
print("-" * 40)
print("DETALLE DE LA COMPRA")
print("-" * 40)
print(f"El precio a pagar por las entradas es: {precio_pago}")
print(f"El precio a pagar por las palomitas es: {precio_palomitas}")
print(f"El precio a pagar por las bebidas es: {precio_bebidas}")
print(f"PRECIO TOTAL: ${precio_pago + precio_palomitas + precio_bebidas}")
