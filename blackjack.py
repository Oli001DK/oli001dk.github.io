import random
Total_penge = random.randint(1000,2000)

print(Total_penge)

def gamble():
    while True:
        gamble = input("hvor meget vil du gamble? du har " +  str(Total_penge ))
        if gamble.isdigit():
            gamble = int(gamble)
            if gamble > 0:
                break
            else:
                print("det kan ikke vaere 0") 
        else:
            print("det kan være et nummer")
    return gamble

gamble()