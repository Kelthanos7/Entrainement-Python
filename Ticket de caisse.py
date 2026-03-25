Montant = int(input("Donnez le montant : "))
if Montant > 50 and Montant <100:
    print ("Vous avez une remise de 5%", "Votre total est de : ", Montant - (Montant * 0.05))
if Montant > 100:
    print ("Vous avez une remise de 10%", "Votre total est de : ", Montant - (Montant * 0.1))
else:
    print ("Aucune remise")