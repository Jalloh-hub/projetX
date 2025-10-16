print("Voici la devinette")

nombre_secret = 23

nombre_utilisateur = int(input("Taper un nombre entre 0 et 100"))

if nombre_utilisateur == nombre_secret:
    print("Gagné")
else:
    print("Perdu. Mais ce n'est pas grave, tu as droit à une deuxieme chance !!")
    nombre_utilisateur = int(input("Dernière chane, chosis ton nombre : "))
    if nombre_utilisateur == nombre_secret :
        print("Gagné")
    else:
        print("Dommage, tu as encore perdu")
print("Fin")