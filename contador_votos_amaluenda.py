'''
Contador de votos 
Cuenta los votos de dos partidos: republicanos y demócratas, muestra los resultados en pantalla
octubre de 2022
'''

def pantalla():
   '''
   Limpia la salida de la terminal de Python. 
   Este método funciona solo para MacOS
   ''' 
   import os
   return os.system("clear") 

def republicano():
   '''
   Cuenta los votos del partido republicano 
   ''' 
   global repu
   pantalla()
   repu = repu + 1

def democrata():
   '''
   Cuenta los votos del partido democráta
   ''' 
   global demo
   pantalla()
   demo = demo + 1

def total(repu, demo):
   '''
   Muestra en pantalla el conteo de votos
   ''' 
   print(f"El total de votos republicanos a la fecha es : {repu}")
   print(f"El total de votos demócratas a la fecha es : {demo}")

def salir():
   '''
   Sale del menú principal y cierra el programa
   ''' 
   global flag
   pantalla()
   flag = True

# Programa principal

pantalla()
flag = False
repu = 0
demo = 0


while not flag:
    print(" *** MENU ***")
    print("=============================")
    print("[1] -> Partido Republicano")
    print("[2] -> Partido Demócrata")
    print("[3] -> Total de votos")
    print("[4] -> Salir del sistema")
    print("=============================")
    print("")

    opt = int(input("Ingrese una opción : "))

    if opt == 1: #Invoca función que permite contar un voto republicano
        republicano()

    elif opt == 2: #Invoca función que permite contar un voto republicano
        democrata()

    elif opt == 3: #Invoca función que muestra en pantalla el conteo (NOTA: Se puede seguir con el conteo / No borra los datos)
        total(repu, demo)

    else: #Invoca función que permite salir del programa
        salir()