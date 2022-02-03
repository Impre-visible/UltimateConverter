from time import *
from base import *

def convert():
    print("\n"+f"""\
        {CRed}Valeur à convertir{CEnd}
        """)
    masses = float(input(cmdline))
    massesChoices(masses)

def massesChoices(quantity):
    print("\n"+f"""\
        {CRed}Unité de masses de base
        \n
        {CBlue}[1]{CEnd} {CBeige}{CBeige}g{CEnd}
        {CBlue}[2]{CEnd} {CBeige}{CBeige}Kg{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Tonnes{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Livre{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)
    reponse1 = input(cmdline)

    if reponse1 == "e":
        cls()
        exit()

    print("\n"+f"""\
        {CRed}Unité de masses à obtenir
        \n
        {CBlue}[1]{CEnd} {CBeige}{CBeige}g{CEnd}
        {CBlue}[2]{CEnd} {CBeige}{CBeige}Kg{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Tonnes{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Livre{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)

    reponse2 = input(cmdline)
    if reponse2 == "e":
        exit()

    elif reponse1 == reponse2:
        print("Il est impossible de convertir une unité par elle même !")
        sleep(1)
        cls()
    elif reponse1 == "1" and reponse2 == "2":
        print(f"{CBlue}{quantity/1000}{CBeige}Kg{CEnd}")
    elif reponse1 == "1" and reponse2 == "3":
        print(f"{CBlue}{quantity/1e+6} {CBeige}Tonnes{CEnd}")
    elif reponse1 == "1" and reponse2 == "4":
        print(f"{CBlue}{quantity/454} {CBeige}Livres{CEnd}")

    elif reponse1 == "2" and reponse2 == "1":
        print(f"{CBlue}{quantity*1000}{CBeige}g{CEnd}")
    elif reponse1 == "2" and reponse2 == "3":
        print(f"{CBlue}{quantity/1000} {CBeige}Tonnes{CEnd}")
    elif reponse1 == "2" and reponse2 == "4":
        print(f"{CBlue}{quantity*2.2046} {CBeige}Livres{CEnd}")

    elif reponse1 == "3" and reponse2 == "1":
        print(f"{CBlue}{quantity*1e+6}{CBeige}g{CEnd}")
    elif reponse1 == "3" and reponse2 == "2":
        print(f"{CBlue}{quantity*1000}{CBeige}Kg{CEnd}")
    elif reponse1 == "3" and reponse2 == "4":
        print(f"{CBlue}{quantity*2204.6} {CBeige}Livres{CEnd}")

    elif reponse1 == "4" and reponse2 == "1":
        print(f"{CBlue}{quantity*454}{CBeige}g{CEnd}")
    elif reponse1 == "4" and reponse2 == "2":
        print(f"{CBlue}{quantity/2.2046}{CBeige}Kg{CEnd}")
    elif reponse1 == "4" and reponse2 == "3":
        print(f"{CBlue}{quantity/2204.6} {CBeige}Tonnes{CEnd}")