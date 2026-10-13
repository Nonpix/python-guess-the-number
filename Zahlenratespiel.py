import random

geheim = random.randint(1, 100)
tipp = 0
versuche = 0
max_versuche = 7

while tipp != geheim and versuche < 7:
    tipp = int(input("Gib eine Zahl zwischen 1 und 100 ein: "))
    versuche += 1

    if tipp < geheim:
        print(f"Zu niedrig.\nEs sind noch {max_versuche - versuche} Versuche übrig.")
    elif tipp > geheim:
        print(f"Zu hoch.\nEs sind noch {max_versuche - versuche} Versuche übrig.")


    if tipp == geheim:
        print(f"Erraten! Du hast {versuche} Versuche gebraucht.")
    elif versuche == 7:
        print(f"Leider nicht geschafft.\nDie gesuchte Zahl war {geheim}.\nViel Glück beim nächsten Mal!")
    
