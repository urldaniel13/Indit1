#Wörterbuch
wb = {"apple":"Apfel", "pear":"Birne", "cherry":"Kirsche", "melon":"Melone", "apricot":"Marille", "peach":"Pfirsich"}

print("[Ü] für Übersetzen eingeben")
print("[N] um neues Wort hinzuzufügen")
    

    
correct = False
    
while correct == False:        #solange bis korrekte Eingabe
    eingabe = input("[Ü] oder [N] eingeben: ")    
    
    if eingabe == "Ü":
        #correct = True #korrekte Eingabe
        word=input("Bitte Wort eingeben: ") #Auslesen
        if word in wb:
            print("Übersetzung: ",wb[word]) #Übersetzung
        else:
            print('not found')
    elif eingabe == "N":
        #correct = True #korrekte Eingabe
        wb[input('Deutsches Wort:')] = input('Englische Übersetzung:') 
        #warum wird es nicht gespeichert?
        
    else:
        print("Unbekannte Antwort")
        
