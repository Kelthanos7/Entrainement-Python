année = int(input("Saisissez une année : "))
if année % 4 == 0 and année % 100 != 0 or année % 400 ==0:
    print("L'année est bissextile ")
else:
    print("L'anée n'est pas bissextile ")