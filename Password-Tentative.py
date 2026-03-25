mdp = "secret"
password = input("Saisissez le mot passe : ")
tentative = 0
while password != mdp:
    print("Incorrect")
    password = input("Saisissez le mot de passe : ")
    tentative = tentative + 1
else:
    print("Vous avez trouvé en", {tentative}, "tentatives")