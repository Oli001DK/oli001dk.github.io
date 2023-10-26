import random
Total_penge = random.randint(1000,2000)

def Deposit():
    while True:
        print("hvor meget vil du gamble? du har " + str(Total_penge))
        gamble = input()
        if gamble.isdigit():
            gamble = int(gamble)
            if gamble > 0:
                break
            else:
                print("det kan ikke vaere 0") 
        else:
            print("det kan være et nummer")
    return gamble

Deposit()
