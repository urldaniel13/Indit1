#Schreiben Sie ein Programm, das nach Eingabe der Radius in einer Funktion den Kreisumfang berechnet.
#Verwenden Sie dazu die Konstante pi aus dem math-Paket.
#Die Eingabe soll in einer eigenen Funktion erfolgen, in der sichergestellt wird, dass es sich dabei
#a) jedenfalls un eine Zahl
#b) eine, positive Zahl handelt

import math

def eingabe():
    correct = False
    while correct == False:
        r_str = input( "Radius: ")
        try:
            r = float(r_str)
            if r > 0:
                correct = True
            else:
                print("keine gültige Eingabe (r <= 0)")
        except ValueError:
            print("keine gültige Eingabe (keine Zahl)")
    return r

def kreisunfang ( radius):
    unfang=2*radius*3.14159265
    return unfang

kreisradius = eingabe()
print("eingegebener Radius:",kreisradius)

umfang = kreisunfang (kreisradius)
print("Kreisunfang: ", umfang)