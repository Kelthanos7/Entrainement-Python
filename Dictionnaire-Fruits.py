fruits = {"pomme": 10, "banane": 5, "orange": 8}
print("il y a",(fruits)["pomme"], "pommes")
fruits["orange"] = 11
fruits["kiwi"] = 4
for k,v in fruits.items():
    if v > 6:
        print(f"{k}: {v}")