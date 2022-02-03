from time import *
from base import *
from currency_converter import CurrencyConverter

c = CurrencyConverter()

def convert():
    print("\n"+f"""\
        {CRed}Valeur à convertir{CEnd}
        """)
    prix = float(input(cmdline))
    monnaiesChoice(prix)

def monnaiesChoice(price):
    print("\n"+f"""\
        {CRed}Monnaie de base
        \n
        {CBlue}[1]{CEnd} {CBeige}Euro{CEnd}
        {CBlue}[2]{CEnd} {CBeige}USD{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Livres{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)
    reponse1 = input(cmdline)

    if reponse1 == "e":
        cls()
        exit()

    print("\n"+f"""\
        {CRed}Monnaie à obtenir
        \n
        {CBlue}[1]{CEnd} {CBeige}Euro{CEnd}
        {CBlue}[2]{CEnd} {CBeige}USD{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Livres{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)

    reponse2 = input(cmdline)
    if reponse2 == "e":
        exit()

    elif reponse1 == reponse2:
        print("Il est impossible de convertir une unité par elle même !")
        sleep(1)
        cls()
        monnaiesChoice()
    elif reponse1 == "1" and reponse2 == "2":
        print(CBlue,c.convert(price, "EUR", "USD"), CBeige,"$",CEnd)
    elif reponse1 == "1" and reponse2 == "3":
        print(CBlue,c.convert(price, "EUR", "GBP"), CBeige,"£",CEnd)
    elif reponse1 == "2" and reponse2 == "1":
        print(CBlue,c.convert(price, "USD", "EUR"), CBeige,"€",CEnd)
    elif reponse1 == "2" and reponse2 == "3":
        print(CBlue,c.convert(price, "USD", "GBP"), CBeige,"£",CEnd)
    elif reponse1 == "3" and reponse2 == "1":
        print(CBlue,c.convert(price, "GBP", "EUR"), CBeige,"€",CEnd)
    elif reponse1 == "3" and reponse2 == "2":
        print(CBlue,c.convert(price, "GBP", "USD"), CBeige,"$",CEnd)