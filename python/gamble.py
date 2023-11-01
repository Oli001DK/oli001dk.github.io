import random
Total_penge = random.randint(1000,2000)
MAX_LINE = 3
def deposit():
    while True:
        penge = input("Hvor meget vil du gamble? du har " + str(Total_penge) + "? ")
        if penge.isdigit():
            penge = int(penge)
            if penge > 0:
                break
            else:
                print("det kan ikke vaere 0") 
        else:
            print("det kan være et nummer")
    return penge

def lines():
    while True:
        lines = input("hvor mange liner vil du spille på? (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("det kan ikke vaere 0") 
        else:
            print("det skal være et nummer")
    return lines

def gamble():
    nummer1 = random.randint(1,9)
    print(nummer1)
    if nummer1 == 1 or 2:
        deposit_gange = 0
    if nummer1 == 4 or 5 or 6:
        deposit_gange = 1
    if nummer1 == 3 or 7 or 8:
        deposit_gange = 2
    if nummer1 == 9:
        deposit_gange = 3
    return deposit_gange

deposit()
lines()
gamble()