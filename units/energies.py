from time import *
from base import *

def convert():
    print("\n"+f"""\
        {CRed}Valeur à convertir{CEnd}
        """)
    energies = float(input(cmdline))
    energiesChoices(energies)

def energiesChoices(quantity):
    print("\n"+f"""\
        {CRed}Unité de vitesses de base
        \n
        {CBlue}[1]{CEnd} {CBeige}Joules{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Calories{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Watt-heures{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Kilowatt-heures{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)
    reponse1 = input(cmdline)

    if reponse1 == "e":
        cls()
        exit()

    print("\n"+f"""\
        {CRed}Unité de vitesses à obtenir
        \n
        {CBlue}[1]{CEnd} {CBeige}Joules{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Calories{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Watt-heures{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Kilowatt-heures{CEnd}

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
        print(f"{CBlue}{quantity/4.182}{CBeige}Calories{CEnd}")
    elif reponse1 == "1" and reponse2 == "3":
        print(f"{CBlue}{quantity/3600}{CBeige}Watt-heures{CEnd}")
    elif reponse1 == "1" and reponse2 == "4":
        print(f"{CBlue}{quantity/3.6e+6}{CBeige}Kilowatt-heures{CEnd}")

    elif reponse1 == "2" and reponse2 == "1":
        print(f"{CBlue}{quantity*4.182}{CBeige}Joules{CEnd}")
    elif reponse1 == "2" and reponse2 == "3":
        print(f"{CBlue}{quantity/860}{CBeige}Watt-heures{CEnd}")
    elif reponse1 == "2" and reponse2 == "4":
        print(f"{CBlue}{quantity/860421}{CBeige}Kilowatt-heures{CEnd}")

    elif reponse1 == "3" and reponse2 == "1":
        print(f"{CBlue}{quantity*3600}{CBeige}Joules{CEnd}")
    elif reponse1 == "3" and reponse2 == "2":
        print(f"{CBlue}{quantity*860}{CBeige}Calories{CEnd}")
    elif reponse1 == "3" and reponse2 == "4":
        print(f"{CBlue}{quantity/1000}{CBeige}Kilowatt-heures{CEnd}")

    elif reponse1 == "4" and reponse2 == "1":
        print(f"{CBlue}{quantity*3.6e+6}{CBeige}Joules{CEnd}")
    elif reponse1 == "4" and reponse2 == "2":
        print(f"{CBlue}{quantity*860421}{CBeige}Calories{CEnd}")
    elif reponse1 == "4" and reponse2 == "3":
        print(f"{CBlue}{quantity*1000}{CBeige}Watt-heures{CEnd}")