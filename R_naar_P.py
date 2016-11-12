import math
import sys

def main():
    r= float(input("Hier je r: "))

    samplesize= float(input("Hier je sample size: "))

    r2= r*r 
    boven= samplesize -2
    onder = 1- r2
    wortel = boven/onder
    wortelresultaat = math.sqrt(wortel)
    resultaat = wortelresultaat * r
    print("t = " + str(resultaat))
    tcrit= 1.987
    if tcrit > resultaat:
        print ("Het is niet statistically significant aangezien het lager is dan tcrit = 1.987 (df=88)")
        print ("Schrijf het op als: r= " + str(r) + ",n= " + str(samplesize) + ", p >.05, two-tails")
    else:
        print ("Het is  statistically significant aangezien het hoger is dan tcrit = 1.987 (df=88)")
        print ("Schrijf het op als: r= " + str(r) + ",n= " + str(samplesize) + ", p <.05, two-tails") 
    nogeenkeer()
    
        
def nogeenkeer():
    s = str(input("Wil je nog een keer iets invullen?: Ja of Nee?"))
    s2= s.lower()
    if s2 == "ja":
        main()
    elif s2 == "nee":
        sys.exit(0)
    else:
        print("Vul ja of nee in graag.")
        nogeenkeer()

main()