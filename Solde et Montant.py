Solde = int(input("Quelle est votre solde ? "))
Montant = int(input("Quel montant souhaitez vous retirer ? "))
if Solde > Montant:
    print("Retrait effctué")
else:
    print("Solde insuffisant")