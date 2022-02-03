from time import *
from base import *

def convert():
    print("\n"+f"""\
        {CRed}Valeur à convertir{CEnd}
        """)
    volumes = float(input(cmdline))
    volumesChoices(volumes)

def volumesChoices(quantity):
    print("\n"+f"""\
        {CRed}Unité de volumes de base
        \n
        {CBlue}[1]{CEnd} {CBeige}Centimètres³{CEnd}     {CBlue}[5]{CEnd} {CBeige}Litres{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Mètres³{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Kilomètres³{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Centilitres{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)
    reponse1 = input(cmdline)

    if reponse1 == "e":
        cls()
        exit()

    print("\n"+f"""\
        {CRed}Unité de volumes à obtenir
        \n
        {CBlue}[1]{CEnd} {CBeige}Centimètres³{CEnd}     {CBlue}[5]{CEnd} {CBeige}Litres{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Mètres³{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Kilomètres³{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Centilitres{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)

    reponse2 = input(cmdline)
    if reponse2 == "e":
        exit()

    elif reponse1 == reponse2:
        print("Il est impossible de convertir une unité par elle même !")
        sleep(1)
        cls()
        volumesChoices()
    elif reponse1 == "1" and reponse2 == "2":
        print(f"{CBlue}{quantity/1e+6}{CBeige}m³{CEnd}")
    elif reponse1 == "1" and reponse2 == "3":
        print(f"{CBlue}{quantity/1e+15}{CBeige}Km³{CEnd}")
    elif reponse1 == "1" and reponse2 == "4":
        print(f"{CBlue}{quantity/10}{CBeige}cL{CEnd}")
    elif reponse1 == "1" and reponse2 == "5":
        print(f"{CBlue}{quantity/1000}{CBeige}L{CEnd}")

    elif reponse1 == "2" and reponse2 == "1":
        print(f"{CBlue}{quantity*1e+6}{CBeige}cm³{CEnd}")
    elif reponse1 == "2" and reponse2 == "3":
        print(f"{CBlue}{quantity/1e+9}{CBeige}Km³{CEnd}")
    elif reponse1 == "2" and reponse2 == "4":
        print(f"{CBlue}{quantity/100000}{CBeige}cL{CEnd}")
    elif reponse1 == "2" and reponse2 == "5":
        print(f"{CBlue}{quantity*1000}{CBeige}L{CEnd}")

    elif reponse1 == "3" and reponse2 == "1":
        print(f"{CBlue}{quantity*1e+15}{CBeige}cm³{CEnd}")
    elif reponse1 == "3" and reponse2 == "2":
        print(f"{CBlue}{quantity*1e+9}{CBeige}m³{CEnd}")
    elif reponse1 == "3" and reponse2 == "4":
        print(f"{CBlue}{quantity*1e+14}{CBeige}cL{CEnd}")
    elif reponse1 == "3" and reponse2 == "5":
        print(f"{CBlue}{quantity*1e+12}{CBeige}L{CEnd}")

    elif reponse1 == "4" and reponse2 == "1":
        print(f"{CBlue}{quantity*10}{CBeige}cm³{CEnd}")
    elif reponse1 == "4" and reponse2 == "2":
        print(f"{CBlue}{quantity*100000}{CBeige}m³{CEnd}")
    elif reponse1 == "4" and reponse2 == "3":
        print(f"{CBlue}{quantity/1e+14}{CBeige}km³{CEnd}")
    elif reponse1 == "4" and reponse2 == "5":
        print(f"{CBlue}{quantity/100}{CBeige}L{CEnd}")

    elif reponse1 == "5" and reponse2 == "1":
        print(f"{CBlue}{quantity*1000}{CBeige}cm³{CEnd}")
    elif reponse1 == "5" and reponse2 == "2":
        print(f"{CBlue}{quantity/1000}{CBeige}m³{CEnd}")
    elif reponse1 == "5" and reponse2 == "3":
        print(f"{CBlue}{quantity/1e+12}{CBeige}km³{CEnd}")
    elif reponse1 == "5" and reponse2 == "4":
        print(f"{CBlue}{quantity*100}{CBeige}cL{CEnd}")