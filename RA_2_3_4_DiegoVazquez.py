# Autor: Diego Vázquez
# Data: 17-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari un nombre enter i imprimeix tots els nombres parells des de 0 fins a aquest nombre.
#Pista: Utilitza range(0, n+1, 2) per generar nombres parells.​
#Excepció:  Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter positiu.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter positiu
# Especificacions de sortida
# Imprimeix tots els nombres parells des de 0 fins al nombre introduït

try:
    num=int(input("Introdueix un numero enter:"))
    for i in range(0, num + 1, 2):
        print(i)
except ValueError:
    print("Error: Si us plau, introdueix un nombre enter vàlid.")
