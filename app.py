from base import *
from time import *
import units.monnaies as monnaies
import units.distances as distances
import units.volumes as volumes
import units.masses as masses
import units.vitesses as vitesses
import units.energies as energies




def baseQuestion():
    print(f"{CRed}Pour commencez, choisissez ce que vous voulez convertir !")
    print("\n"+f"""\
        {CBlue}[1]{CEnd} {CBeige}Monnaies{CEnd}     {CBlue}[5]{CEnd} {CBeige}Vitesses{CEnd}
        {CBlue}[2]{CEnd} {CBeige}Distances{CEnd}    {CBlue}[6]{CEnd} {CBeige}Energies{CEnd}
        {CBlue}[3]{CEnd} {CBeige}Volumes{CEnd}
        {CBlue}[4]{CEnd} {CBeige}Masses{CEnd}

    {CBlue}[e]{CEnd} {CBeige}exit{CEnd}
        """)
    reponse = input(cmdline)
    if reponse == "1":
        monnaies.convert()
    elif reponse == "2":
        distances.convert()
    elif reponse == "3":
        volumes.convert()
    elif reponse == "4":
        masses.convert()
    elif reponse == "5":
        vitesses.convert()
    elif reponse == "6":
        energies.convert()
    elif reponse == "e":
        cls()
        exit()
    else:
        print("Commande incomprise ! Veuillez réessayer.")
        sleep(1)
        cls()
        start()
    

def start():
    loading()
    cls()
    base()
    baseQuestion()



start()