import math
import sys

def rnaarp():
    r= float(input("Hier uw r: "))

    samplesize= float(input("Hier uw sample size: "))
	tcrit= float(input("Hier uw tcrit: "))
	df= float(input("Hier uw df: "))
    boven= samplesize -2
    onder = 1- r*r
    wortel = boven/onder
    resultaat = math.sqrt(wortel) *r
    print("t = " + str(resultaat))
    	
    if tcrit > resultaat:
        print ("Het is niet statistically significant aangezien het lager is dan tcrit = " + str(tcrit) + " (df=??)")
        print ("Schrijf het op als: r= " + str(r) + ",n= " + str(samplesize) + ", p >.05, two-tails")
    else:
        print ("Het is  statistically significant aangezien het hoger is dan tcrit = " + str(tcrit) + " (df=??)")
        print ("Schrijf het op als: r= " + str(r) + ",n= " + str(samplesize) + ", p <.05, two-tails") 
    doorgaan()
    
        
def doorgaan():
    s = str(input("Wilt u nog een keer iets invullen?: Ja of Nee?"))
    s2= s.lower()
    if s2 == "ja":
        rnaarp()
    elif s2 == "nee":
        sys.exit(0)
    else:
        print("Vul ja of nee in graag.")
        doorgaan()

rnaarp()