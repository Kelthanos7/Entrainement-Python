a = [1,2,2,3,4,4,4,5]
nb2 = a.count(2)
nb4 = a.count(4)
liste2 = []
for i in a:
    if a.count(i) > 1 and i not in liste2:
        liste2.append(i)
        print(liste2)