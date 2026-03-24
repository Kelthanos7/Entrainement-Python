note = int(input("Quelle est la note ? "))
if note >= 16:
    print("Mention Très Bien")
elif note >= 14:
    print("Mention Bien")
elif note >= 12:
    print("Mention Assez Bien")
elif note >= 10:
    print("Mention Passable")
else:
    print("Insuffisant")