from time import *
from base import *

def convert():
    print("\n"+f"""\
        {CRed}Valeur à convertir{CEnd}
        """)
    mesure = float(input(cmdline))
    distancesChoice(mesure)

def distancesChoice(distance):
    print("\n"+f"""\
        {CRed}Unité de distances de base
        \n
        {CBlue}[1]{CEnd} {CBeige}Centimètres{CEnd}     {CBlue}[5]{CEnd} {CBeige}Pieds{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Mètres{CEnd}          {CBlue}[6]{CEnd} {CBeige}Mile{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Kilomètres{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Pouces{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)
    reponse1 = input(cmdline)

    if reponse1 == "e":
        cls
        exit()

    print("\n"+f"""\
        {CRed}Unité de distances à obtenir
        \n
        {CBlue}[1]{CEnd} {CBeige}Centimètres{CEnd}     {CBlue}[5]{CEnd} {CBeige}Pieds{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Mètres{CEnd}          {CBlue}[6]{CEnd} {CBeige}Mile{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Kilomètres{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Pouce{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)

    reponse2 = input(cmdline)
    if reponse2 == "e":
        cls()
        exit()

    elif reponse1 == reponse2:
        print("Il est impossible de convertir une unité par elle même !")
        sleep(1)
        cls()
        distancesChoice()
    elif reponse1 == "1" and reponse2 == "2":
        print(f"{CBlue}{distance/100}{CBeige}m{CEnd}")
    elif reponse1 == "1" and reponse2 == "3":
        print(f"{CBlue}{distance/100000}{CBeige}Km{CEnd}")
    elif reponse1 == "1" and reponse2 == "4":
        print(f"{CBlue}{distance/2.54} {CBeige}Pouces{CEnd}")
    elif reponse1 == "1" and reponse2 == "5":
        print(f"{CBlue}{distance/30.48} {CBeige}Pieds{CEnd}")
    elif reponse1 == "1" and reponse2 == "6":
        print(f"{CBlue}{distance/160934} {CBeige}Miles{CEnd}")
    elif reponse1 == "2" and reponse2 == "1":
        print(f"{CBlue}{distance*100}{CBeige}cm{CEnd}")
    elif reponse1 == "2" and reponse2 == "3":
        print(f"{CBlue}{distance/1000}{CBeige}Km{CEnd}")
    elif reponse1 == "2" and reponse2 == "4":
        print(f"{CBlue}{distance*38.598} {CBeige}Pouces{CEnd}")
    elif reponse1 == "2" and reponse2 == "5":
        print(f"{CBlue}{distance*3.28084} {CBeige}Pieds{CEnd}")
    elif reponse1 == "2" and reponse2 == "6":
        print(f"{CBlue}{distance*1609} {CBeige}Miles{CEnd}")
    elif reponse1 == "3" and reponse2 == "1":
        print(f"{CBlue}{distance*100000}{CBeige}cm{CEnd}")
    elif reponse1 == "3" and reponse2 == "2":
        print(f"{CBlue}{distance*100}{CBeige}cm{CEnd}")
    elif reponse1 == "3" and reponse2 == "4":
        print(f"{CBlue}{distance*39370}{CBeige}cm{CEnd}")
    elif reponse1 == "3" and reponse2 == "5":
        print(f"{CBlue}{distance*3281}{CBeige}cm{CEnd}")
    elif reponse1 == "3" and reponse2 == "6":
        print(f"{CBlue}{distance/1.609}{CBeige}cm{CEnd}")
    elif reponse1 == "4" and reponse2 == "1":
        print(f"{CBlue}{distance*2,54}{CBeige}cm{CEnd}")
    elif reponse1 == "4" and reponse2 == "2":
        print(f"{CBlue}{distance/39.37}{CBeige}m{CEnd}")
    elif reponse1 == "4" and reponse2 == "3":
        print(f"{CBlue}{distance/39370}{CBeige}Km{CEnd}")
    elif reponse1 == "4" and reponse2 == "5":
        print(f"{CBlue}{distance/12} {CBeige}Pieds{CEnd}")
    elif reponse1 == "4" and reponse2 == "6":
        print(f"{CBlue}{distance/ 63360} {CBeige}Miles{CEnd}")
    elif reponse1 == "5" and reponse2 == "1":
        print(f"{CBlue}{distance*30.48}{CBeige}cm{CEnd}")
    elif reponse1 == "5" and reponse2 == "2":
        print(f"{CBlue}{distance/3.281}{CBeige}m{CEnd}")
    elif reponse1 == "5" and reponse2 == "3":
        print(f"{CBlue}{distance/3281}{CBeige}Km{CEnd}")
    elif reponse1 == "5" and reponse2 == "4":
        print(f"{CBlue}{distance*12} {CBeige}Pouces{CEnd}")
    elif reponse1 == "5" and reponse2 == "6":
        print(f"{CBlue}{distance/5280} {CBeige}Miles{CEnd}")
    elif reponse1 == "6" and reponse2 == "1":
        print(f"{CBlue}{distance*160934}{CBeige}cm{CEnd}")
    elif reponse1 == "6" and reponse2 == "2":
        print(f"{CBlue}{distance*1609.34}{CBeige}m{CEnd}")
    elif reponse1 == "6" and reponse2 == "3":
        print(f"{CBlue}{distance*1,60934}{CBeige}Km{CEnd}")
    elif reponse1 == "6" and reponse2 == "4":
        print(f"{CBlue}{distance*63360} {CBeige}Pouces{CEnd}")
    elif reponse1 == "6" and reponse2 == "5":
        print(f"{CBlue}{distance*5280} {CBeige}Pieds{CEnd}")