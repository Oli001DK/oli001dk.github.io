MAX_LINE = 3
def deposit():
    while True:

        penge = input("hvor manget vil du deposit?" )
        if penge.isdigit():
            penge = int(penge)
            if penge > 0:
                break
            else:
                print("det kan ikke vaere 0") 
        else:
            print("det kan være et nummer")
    return penge
deposit()
