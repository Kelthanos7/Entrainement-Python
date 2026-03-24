température = int(input("Quelle est la température ? "))
if température < 0:
    print("Gel")
elif température >= 0 and température <= 15:
        print("Froid")
elif température >= 15 and température <= 25:
            print("agréable")
elif température > 25:
                print("Chaud")