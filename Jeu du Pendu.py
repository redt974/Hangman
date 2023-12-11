def pendu(mot_mystere) :
    trou = ""
    for i in range(len(mot_mystere)):
        trou += "_"
    print("{} ({} lettres)".format(trou, len(trou)))
    mot = []
    for i in range(len(mot_mystere)):
        mot.append("_")
    vie = 8
    while vie != 0 :
        if trou != mot_mystere :
            copie_mot = []
            lettre = str(input("Quelle lettre proposez-vous ?"))
            if lettre in mot_mystere :
                for i in range(len(mot_mystere)):
                    if mot_mystere[i] == lettre:
                        mot[i] = lettre
                copie_mot.extend(mot)
                trou = ""
                while mot != []:
                    trou += mot.pop(0)
                mot.extend(copie_mot)
                print("{} ({} lettres)".format(trou, len(trou)))
            else :
                vie -= 1
                if vie == 7 :
                    potence1 = '__________\n\t'+ " " + "|"
                    print(potence1)
                elif vie == 6 :
                    potence1 += "\n\t |"
                    print(potence1)
                elif vie == 5 :
                    potence2 = "\n\t O"
                    print(potence1 + potence2)
                elif vie == 4 :
                    potence2 += "\n\t/"
                    print(potence1 + potence2)
                elif vie == 3 :
                    potence2 += "|"
                    print(potence1 + potence2)
                elif vie == 2 :
                    potence2 += "\\"
                    print(potence1 + potence2)
                elif vie == 1 :
                    potence3 = "\n\t/"
                    print(potence1 + potence2 + potence3)
                else :
                    potence3 += " \\"
                    print(potence1 + potence2 + potence3)
                print("{} ({} lettres)".format(trou, len(trou)))
        else :
            return "Gagné ! Tu as trouvé le mot : {}".format(mot_mystere)
    return "Pendu ! Le mot était {}".format(mot_mystere)

# print(pendu("animaux"))

from random import *

def bonus():
    level = int(input("Choissisez votre niveau : (entre 1 et 3)"))
    theme = str(input("Choissisez votre thème entre Halloween (H), Fruit (F), Pirates (P) :" ))
    liste_mot = []
    mot_mystere = ""
    if level == 1 :
        if theme == "H" :
            liste_mot.extend(["sort","chaudron","bonbon"])
            mot_mystere = choice(liste_mot)
        elif theme == "F" :
            liste_mot.extend(["pomme","banane","kiwi"])
            mot_mystere = choice(liste_mot)
        else :
            liste_mot.extend(["tresor","navire","carte"])
            mot_mystere = choice(liste_mot)
    elif level == 2 :
        if theme == "H" :
            liste_mot.extend(["sorcière","fantome","vampire"])
            mot_mystere = choice(liste_mot)
        elif theme == "F" :
            liste_mot.extend(["raisin","citron","papaye"])
            mot_mystere = choice(liste_mot)
        else :
            liste_mot.extend(["capitaine","matelot","bataille"])
            mot_mystere = choice(liste_mot)
    else :
        if theme == "H" :
            liste_mot.extend(["deguisement","épouvantail","citrouille"])
            mot_mystere = choice(liste_mot)
        elif theme == "F" :
            liste_mot.extend(["datte","pamplemousse","pasteque"])
            mot_mystere = choice(liste_mot)
        else :
            liste_mot.extend(["abordage","pillage","gouvernail"])
            mot_mystere = choice(liste_mot)
    return pendu(mot_mystere)

print(bonus()) 
