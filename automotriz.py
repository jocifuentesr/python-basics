"""
Código que pide al cliente aceptar diferentes servicios de mantenimiento automotriz.
Finalmente, muestra el tiempo de espera total para el cliente.
"""

# tiempos de servicio
# tiempo total 4.7 horas
ta = 2 # rev km
tb = 1 # aceite
tc = 0.5 # frenos
td = 0.5 # correas
te = 0.2 # luces
tf = 0.5 # dirección 
tg = 0.5  # lavado (opcional)

print("\n"+"-" * 40)
print("Gracias por preferir nuestro servicio")
print("-" * 40)
nombre = input("Ingrese su nombre: ")
rut = input("Ingrese rut: ")
marca = input("Ingrese marca de su auto: ")
modelo = input("Ingrese modelo de su auto: ")
print("\n"+"-" * 30)
print("Elección de servicios")
print("-" * 30)
#rev1000km
print("¿Viene por servicio de revisión de 1000 km?")
print("1 = Sí" )
print("2 = No")
a = int(input("Indique su preferencia: "))

#aceite
print("\n¿Agrega cambio de aceite?")
print("1 = Sí" )
print("2 = No")
b = int(input("Indique su preferencia: "))

#frenos
print("\n¿Agrega revisión de frenos?")
print("1 = Sí" )
print("2 = No")
c = int(input("Indique su preferencia: "))

#correas
print("\n¿Agrega cambio de correas?")
print("1 = Sí" )
print("2 = No")
d = int(input("Indique su preferencia: "))

#luces
print("\n¿Agrega revisión de luces?")
print("1 = Sí" )
print("2 = No")
e = int(input("Indique su preferencia: "))

#luces
print("\n¿Agrega revisión de la dirección?")
print("1 = Sí" )
print("2 = No")
f = int(input("Indique su preferencia: "))


tt = 0 # tiempo total
servicios = "Servicios: "
cantidad = 0

if a == 1: 
    tt = tt + ta
    servicios = servicios + "Rev KM, "
    cantidad = cantidad + 1
if b == 1: 
    tt = tt + tb
    servicios = servicios + "Cambio aceite, "
    cantidad = cantidad + 1

if c == 1: 
    tt = tt + tc
    servicios = servicios + "Frenos, "
    cantidad = cantidad + 1
if d == 1: 
    tt = tt + td
    servicios = servicios + "Correas, "
    cantidad = cantidad + 1

if e == 1: 
    tt = tt + te
    servicios = servicios + "Luces, "
    cantidad = cantidad + 1

if f == 1: 
    tt = tt + tf
    servicios = servicios + "Dirección, "
    cantidad = cantidad + 1

print("\n¿Desea la lavar su vehículo gratis?")
print("Este servicio aumentará su tiempo de espera actual en 30 minutos")
print(f"Tiempo de espera con lavado: {tt + 0.5} horas")
print("1 = Sí" )
print("2 = No")
g = int(input("Indique su preferencia: "))

if g == 1: 
    tt = tt + tg
    servicios = servicios + "Lavado gratis "
    cantidad = cantidad + 1

# Salida
print("\n"+"-" * 30)
print("Resumen de su solicitud")
print(""+"-" * 30)
print(f"Cliente: {nombre}")
print(f"Servicios: {servicios}")
print(f"Cantidad: {cantidad}")
print(f"Tiempo de espera: {tt} horas")
print(f"Estado: Terminado")
print(f"Muchas gracias {nombre}. Esperamos verlo pronto\n")