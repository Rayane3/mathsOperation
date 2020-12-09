def validateInput(putin) :
    chiffres = ['0' , '1' , '2' , '3' , '4' , '5' ,'6' , '7' , '8' , '9' ]
    for i in range(len(putin)):
        if putin[i] not in chiffres :
            return False
    return True

def askForInput() :
    print ("entrer un nombre")
    rawInput = input()
    if validateInput(rawInput) :
        resulat = square(int(rawInput))
        print("le carre de" , rawInput , "est" , resulat)
    else :
        askForInput()

def square(n) :
    # s = n*n
    return int(n*n)

def main() :
    askForInput()

main()
