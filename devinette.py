print("Voici la devinette")

nombre_secret = 23

while True:
    nombre_utilisateur = int(input("Tape un nombre entre 0 et 100: "))

    if nombre_utilisateur == nombre_secret:
        print("Gagné")
        break  # Si l'utilisateur devine le bon nombre, on sort de la boucle
    else:
        print("Perdu, essaie encore")


