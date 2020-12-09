def validateInput(putin) :
    chiffres = ['0' , '1' , '2' , '3' , '4' , '5' ,'6' , '7' , '8' , '9' ]
    for i in range(len(putin)):
        if putin[i] not in chiffres :
            return False
    return True

def askForInput() :
    print ("enter an integer")
    rawInput = input()
    if validateInput(rawInput) :
        computeParity(rawInput)
    else :
        askForInput()
        
def computeParity(number) :
    inputNumber = int(number)
    isEven = False
    parite = "impair" 
    if (inputNumber % 2) == 0:
        isEven = True
        parite = "pair"
    print ("le nombre " + str(inputNumber) + " est " + parite )
    
def main() :
    askForInput()
    
main()