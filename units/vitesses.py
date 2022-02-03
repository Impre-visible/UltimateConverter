from time import *
from base import *

def convert():
    print("\n"+f"""\
        {CRed}Valeur à convertir{CEnd}
        """)
    vitesses = float(input(cmdline))
    vitessesChoices(vitesses)

def vitessesChoices(quantity):
    print("\n"+f"""\
        {CRed}Unité de vitesses de base
        \n
        {CBlue}[1]{CEnd} {CBeige}m/s{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Km/h{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Mille/heure (mph){CEnd}
        {CBlue}[4]{CEnd} {CBeige}Noeud{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)
    reponse1 = input(cmdline)

    if reponse1 == "e":
        cls()
        exit()

    print("\n"+f"""\
        {CRed}Unité de vitesses à obtenir
        \n
        {CBlue}[1]{CEnd} {CBeige}m/s{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Km/h{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Mile/heure (mph){CEnd}
        {CBlue}[4]{CEnd} {CBeige}Noeud{CEnd}

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
        print(f"{CBlue}{quantity*3.6}{CBeige}Km/h{CEnd}")
    elif reponse1 == "1" and reponse2 == "3":
        print(f"{CBlue}{quantity*2.237}{CBeige}mph{CEnd}")
    elif reponse1 == "1" and reponse2 == "4":
        print(f"{CBlue}{quantity*1.94384} {CBeige}Noeuds{CEnd}")
        
    elif reponse1 == "2" and reponse2 == "1":
        print(f"{CBlue}{quantity/3.6}{CBeige}m/s{CEnd}")
    elif reponse1 == "2" and reponse2 == "3":
        print(f"{CBlue}{quantity/1.609}{CBeige}mph{CEnd}")
    elif reponse1 == "2" and reponse2 == "4":
        print(f"{CBlue}{quantity/1.852} {CBeige}Noeuds{CEnd}")
        
    elif reponse1 == "3" and reponse2 == "1":
        print(f"{CBlue}{quantity/2.237}{CBeige}m/s{CEnd}")
    elif reponse1 == "3" and reponse2 == "2":
        print(f"{CBlue}{quantity*1.609}{CBeige}Km/h{CEnd}")
    elif reponse1 == "3" and reponse2 == "4":
        print(f"{CBlue}{quantity/1.151} {CBeige}Noeuds{CEnd}")
        
    elif reponse1 == "4" and reponse2 == "1":
        print(f"{CBlue}{quantity/1.94384}{CBeige}m/s{CEnd}")
    elif reponse1 == "4" and reponse2 == "2":
        print(f"{CBlue}{quantity*1.852}{CBeige}Km/h{CEnd}")
    elif reponse1 == "4" and reponse2 == "3":
        print(f"{CBlue}{quantity*1.151}{CBeige}mph{CEnd}")