mot = input("Saississez un mot ")
a = "a"
compteur = 0
for lettre in mot:
    if lettre in a:
        compteur = compteur + 1
print(f"Le mot '{mot}' contient {compteur} a)")