# Schreiben Sie ein Progrann, das auf 2 mögliche Versionen, die in der Liste aufgeführten Personen begrüßt
# Z.B.: "Hallo, Peter!"
# Version 1: for-Schleife in Hauptprogramm, Ausgabe der Begrüßung in einen Unterprogramm
# Version 2: for-Schleife und Ausgabe der Begrüßung in einen Unterprogramm

namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]

def begruessung(name):
    print("Hallo", name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm!")
    return
    
def begruessung2(namensliste):
    for ein_name in namensliste:
        print("Hallo", ein_name)
        print("Schön dich zu sehen!")
        print("Viel Spaß mit dem Programm!")
    
print("Version 1")
for name in namen:
    begruessung(name)
    
print("Version 1")
begruessung2(namen)
    