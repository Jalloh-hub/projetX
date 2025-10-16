print("Voici la devinette")

nombre_secret = 23

while True:
    nombre_utilisateur = int(input("Taper un nombre entre 0 et 100"))
    if nombre_secret == nombre_utilisateur:
        print("Gagné")
        break
    else: 
        print("Perdu. Rentente ta chance :")
print("Fin")