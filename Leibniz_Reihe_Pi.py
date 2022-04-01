# Hausuebung: Leibniz-Reihe (Zahl Pi)

from math import pi
intZaehler = 1
intNaenner1 = 1
intNaenner2 = 3
intReihensumme1 = 0
intReihensumme2 = 0

strTerme = input("Wie viele Terme sollen herangezogen werden? ")
intTerme = int(strTerme)
print ("Terme =", intTerme)
inthoechsterNaenner = (intTerme*2-1)
print ("hoechster Naenner =", inthoechsterNaenner)

while intNaenner1 <= inthoechsterNaenner:
    intDivision1 = (intZaehler/intNaenner1)
    intNaenner1 +=4
    intReihensumme1 += intDivision1
    
while intNaenner2 <= inthoechsterNaenner:
    intDivision2 = (intZaehler/intNaenner2)
    intNaenner2 +=4
    intReihensumme2 += intDivision2
    
    
print("Pi ist ungefähr:", (intReihensumme1-intReihensumme2)*4)
print("Pi für Vergleich:", pi)
