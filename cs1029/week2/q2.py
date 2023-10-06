john = {"age":17, "money":20}

james = {"age":18, "money":16}

if john["age"] >= 18 and john["money"] >= 20:
    print("John can buy the £20 red wine")
else:
    if not(john["age"] >= 18):
        print("John can not buy the £20 red wine since he is not old enough.")
    if not(john["money"] >= 20):
        print("John can not buy the £20 red wine since he is does not have enough money.")

if james["age"] >= 18 and james["money"] >= 18:
    print("James can buy the £18 red wine")
else:
    if not(james["age"] >= 18):
        print("James can not buy the £18 red wine since he is not old enough.")
    if not(james["money"] >= 18):
        print("James can not buy the £18 red wine since he is does not have enough money.")
