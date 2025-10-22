# Autor: Diego Vázquez
# Data: 17-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest nombre.​
#Pista:  Implementa una funció que comprovi si un nombre és primer i utilitza range(2, n+1) per iterar.​
#Excepció:  Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter positiu.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter positiu
# Especificacions de sortida
# Imprimeix tots els nombres primers des de 2 fins al nombre introduït

try:
    num=int(input("Introudeix un numero enter: "))
    for i in range(2, num +1):
        es_primer = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                es_primer = False
                break
        if es_primer:
            print(i)
except ValueError:
    print("Si us plau, introdueix un nombre enter positiu vàlid.")
