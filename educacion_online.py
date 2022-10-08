# librerías
import os

# banderas
menu_flag = False

# contadores
con_cursos_s_cupon = 0
cont_cursos_cupon = 0
total = 0

# valor cursos
programacion = 250000
while not menu_flag:
    flag_cupon = False
    os.system('cls')
    print("\n")
    print("-" * 50)
    print("BIENVENIDO AL SISTEMA DE COMPRA DE CURSOS")
    print("LOS CURSOS DISPONIBLES SON LOS SIGUIENTES:")
    print("-" * 50)
    print("1. PROGRAMACIÓN: $250.000")
    print("2. BASE DE DATOS: $310.000")
    print("3. ROBÓTICA: $280.000")
    print("4. SALIR")
    opt_main_menu = int(input("Ingrese la opción para el curso que desea comprar: "))

    if opt_main_menu == 1:
        os.system('cls')
        print("Comprará el curso de programación por un costo de $250.000")
        print("¿Está de acuerdo?")
        print("1. Si")
        print("2. No")
        opt_submenu = int(input("Seleccione su opción: "))
        if opt_submenu == 1:
            nombre = input("Por favor ingrese su nombre completo: ")
            rut = input("Por ingrese su rut sin puntos y con guión: ")
            os.system('cls')
            print("¿Tiene un cupón de descuento?")
            print("1. Si")
            print("2. No")
            opt_dcto = int(input("Seleccione su opción: "))
            if opt_dcto == 1:
                cupon = input("Ingrese el cupon: ")
                if cupon == "EDUCATE-ONLINE":
                    flag_cupon = True
                    print("Se aplicó un descuento de un 20% por usar el cupón")
                    cont_cursos_cupon += 1
                    total += programacion * 0.8
                else:
                    print("El cupon ingresado no es correcto. No aplica descuento")
            elif opt_dcto == 2:
                print("Se compró su curso por un precio de $250.000")
                con_cursos_s_cupon += 1 
                total = total + programacion
            else: 
                print("Opción incorrecta")
            input("Presione una tecla para continuar...")
            os.system('cls')
        elif opt_submenu == 2:
            os.system('cls')
            print("Presione una tecla para continuar...")
            input()
        else: 
            print("Opción incorrecta. Intente nuevamente")
            input("Presione un tecla para continuar...")


    if opt_main_menu == 4:
        menu_flag = True
        os.system('cls')

# resumen de la compra
print("-" * 50)
print("RESUMEN DE SU COMPRA")
print(f"Total de cursos comprados con descuento: {cont_cursos_cupon}")
print(f"Total de cursos comprados sin descuento: {con_cursos_s_cupon }")
print(f"Total de cursos comprados: {cont_cursos_cupon + con_cursos_s_cupon}")
print(f"Total pagado: ${round(total)}")
print("GRACIAS POR USAR NUESTRO SISTEMA")
print("Ingrese una tecla para continuar ...")
print("-" * 50)
input()
os.system('cls')
