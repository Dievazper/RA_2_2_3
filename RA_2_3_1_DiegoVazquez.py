# Autor: Diego Vázquez
# Data: 17-10-25

# Descripció del programa o enunciat de l'exercici:
#Utilitzant el range(),  escriu un programa que generi una seqüència de nombres des de 0 fins a un nombre introduït per l'usuari. 
#Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter
# Especificacions de sortida
# Imprimeix la seqüència de nombres des de 0 fins al nombre introduït
while True:
    entrada = input("Introdueix un nombre enter per al final de la seqüència: ")
    try:
        nombre_final = int(entrada)
        sequencia = list(range(nombre_final))
        print(f"✅ La seqüència de 0 fins a {nombre_final-1} és: {sequencia}")
        break
    except ValueError:
        print("❌ Error: Has d'introduir un valor que sigui un nombre enter.")
        