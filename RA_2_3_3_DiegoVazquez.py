# Autor: Diego Vázquez
# Data: 17-10-25

#Descripció del programa o enunciat de l'exercici:
#Utilitzant el range() escriu un programa que mostri la taula de multiplicar d'un número introduït per l'usuari.
#Pista: Utilitza range(1, 11) per generar els multiplicadors del 1 al 10.​
#Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter
# Especificacions de sortida
# Imprimeix la taula de multiplicar del nombre introduï
#while True:
entrada = input("Introdueix un nombre enter per veure la seva taula de multiplicar: ")
try:
    factor = int(entrada)
    print(f"Taula de multiplicar del {factor}:")
    for i in range(1, 11):
            resultat = factor * i
            print(f"{factor} x {i:2} = {resultat}")
#break
except ValueError:
        print("❌ Error: Has d'introduir un valor que sigui un nombre enter.")