MAX_LINE = 3
def deposit():
    while True:

        penge = input("hvor meget vil du deposit?" )
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

deposit()
lines()
