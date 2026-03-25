saisie = input("Saisissez quelque chose : ")
if saisie.isalpha():
    print("il ne contient que des lettres.")
elif saisie.isdigit():
    print("il ne contient que des chiffres.")
elif saisie.isalnum():
    print("il contient à la fois des chiffres et des lettres.")