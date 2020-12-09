def validateInput(putin) :
    chiffres = ['0' , '1' , '2' , '3' , '4' , '5' ,'6' , '7' , '8' , '9' ]
    # ch = "0123456789"
    for i in range(len(putin)):
        if putin[i] not in chiffres :
            return False
    return True

def askForInput() :
    print ("enter an integer")
    rawInput = input()
    if validateInput(rawInput) :
        resulat = sum(int(rawInput))
        print("la somme de tous les entiers jusqu'a" , rawInput , "est" , resulat)
    else :
        askForInput()

def sum(n) :
    s = 0
    for x in range(n+1) :
        s = s+x
    return s

def main() :
    askForInput()

main()
