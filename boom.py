def bamboom(n) :
    print ("voilaaaa")
    for boom in range(1,n+1) :
        if (boom % 3 == 0) and (boom % 5 == 0 ) :
            print("bamboom")
        elif boom % 3 == 0 :
            print("bam")
        elif boom % 5 == 0 :
            print("boom")
        else :
            print(boom)
            
def askForInput() :
    print ("un nombre sil vous plait pour jouer")
    n = int(input())
    bamboom(n)
    
def main() :
    askForInput()

main()
