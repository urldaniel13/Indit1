# Wetterabfrage -> sonnig oder regnerisch
# wenn sonnig -> Gartenparty
# wenn regnersich -> Kellerparty
# wenn gar nix -> Fehlermeldung

wetter = input("Wie ist das Wetter heute - `sonnig´ oder `regnerisch´? ")

if wetter.upper() == "SONNE" or wetter.upper() == "SONNIG":
    print("Heute machen wir eine Gartenparty!")
    print("Jawoll - Sonne genießen!")
elif wetter.lower() == "regen" or wetter.lower() == "regnerisch":
    print("Heute machen wir eine Kellerparty!")
    print("Leider kein Vitamin D :(")
else:
    print("Eingabe wiederholen - bitte `sonnig´ oder `regnersich´ angeben. Sonst leider keine Party!")
