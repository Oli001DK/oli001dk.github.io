import random
KORT = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11]

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
hand1 = random.randint(2,11)
hand2 = random.randint(2,11)
if hand1 and hand2 == 22:
    print("Du har tabt")
    Deposit()
hand = hand1 + hand2    

dealerhand1 = random.randint(2,11)
dealerhand2 = random.randint(2,11)
if dealerhand1 and dealerhand2 == 22:
    print("Dealer har tabt")
    Deposit()
dealerhand = dealerhand1 + dealerhand2
print("du har " + str(hand))
print("dealer har " + str(dealerhand1))
print(dealerhand)
print("Vil du har ")
