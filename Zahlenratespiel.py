import random

geheim = random.randint(1, 100)
tipp = 0
versuche = 0

while tipp != geheim and versuche < 7:
    tipp = int(input("Gib eine Zahl zwischen 1 und 100 ein: "))
    versuche += 1

    if tipp < geheim:
        print("zu niedrig")
    elif tipp > geheim:
        print("zu hoch")


    if tipp == geheim:
        print(f"Erraten! Du hast {versuche} Versuche gebraucht.\nEs sind noch {7 - versuche} Versuche übrig.")
    elif versuche == 7:
        print(f"Leider nicht geschafft.\nDie gesuchte Zahl war {geheim}.\nViel Glück beim nächsten Mal!")
    
