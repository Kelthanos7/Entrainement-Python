inscrits = {"Alice", "Bob","Charlie","Diana"}
presents = {"Alice", "Charlie", "Eve"}
absents = inscrits - presents
noninscrits = presents - inscrits
inspres = inscrits and presents
print((absents), "sont absents")
print((noninscrits), "sont présents mais non inscrits")
print((inspres), "sont inscrits et présents.")
