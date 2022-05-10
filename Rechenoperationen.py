#def summe( summand1, summand2):         # Funktion -> def Funktionsnamer(Parameter1, Parameter, ...):
 #   zwischensumme = summand1 + summand2
  #  return zwischensumme

#Wert1 = summe(23, 24)
#print("Summe: ", Wert1)

#Wert2 = summe (1, -3)
#print("Summe: ", Wert2)

#Wert3 = summe (Wert1, Wert2)
#print("Summe: ", Wert3)

# Schreiben Sie kurzes Python-Programm, das Sie nach der Eingabe von 2 Zahlen fragt
# und danach die Summe, die Differenz, das Produkt und den Outienten der beiden Zahlen
# ausgibt.
#
# schreiben Sie jeweils eine Funktion zur Berechnung von Summe, Diffrenz, Produkt und
# Quotient.
#
#Verhindern Sie, dass mathematisch unmögliche Berechnungen durchgeführt werden.

strZahl1 = input("Zahl 1 eingeben: ")
intZahl1 = int(strZahl1)

strZahl2 = input("Zahl 2 eingeben: ")
intZahl2 = int(strZahl2)

def summe( intZahl1, intZahl2):
    zwischensumme = intZahl1 + intZahl2
    return zwischensumme

Summe1 = summe( intZahl1, intZahl2)
print ("Summe = ", Summe1)

def differenz( intZahl1, intZahl2):
    zwischensumme = intZahl1 - intZahl2
    return zwischensumme

Differenz1 = differenz( intZahl1, intZahl2)
print ("Differenz = ", Differenz1)

def division( intZahl1, intZahl2):
    if intZahl2 == 0:
        print("mathematisch unmöglich")
        return
    zwischensumme = intZahl1 / intZahl2
    return zwischensumme

Division1 = division( intZahl1, intZahl2)
print ("Division = ", Division1)

def multiplikation( intZahl1, intZahl2):
    zwischensumme = intZahl1 * intZahl2
    return zwischensumme

Multiplikation1 = multiplikation( intZahl1, intZahl2)
print ("Multiplikation = ", Multiplikation1)