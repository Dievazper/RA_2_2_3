# Autor: Diego Vázquez
# Data: 17-10-25

#Descripció del programa o enunciat de l'exercici:
#Demana a l'usuari un nombre enter i calcula la suma de tots els nombres des de 1 fins a aquest nombre.
#Pista: Utilitza range(1, n+1) per generar la seqüència i la funció sum() per obtenir la suma.
#Excepció: Gestiona l'error si l'usuari introdueix un valor que no és un nombre enter positiu.

# Especificacions d'entrada
# Demana a l'usuari que introdueixi un nombre enter positiu
# Especificacions de sortida
# Imprimeix la suma de tots els nombres des de 1 fins al nombre introduït
while True:
    entrada = input("Introdueix un nombre enter POSITIU per sumar fins a ell: ")
    try:
        nombre_suma = int(entrada)
        if nombre_suma <= 0:
            print("❌ Error: Si us plau, introdueix un nombre enter POSITIU.")
            continue
        suma_total = sum(range(1, nombre_suma + 1))
        print(f"✅ La suma de tots els nombres des de 1 fins a {nombre_suma} és: {suma_total}")
        break
    except ValueError:
        print("❌ Error: Has d'introduir un valor que sigui un nombre enter.")
