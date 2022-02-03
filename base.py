from datetime import datetime, date
import platform, os
from console_progressbar import ProgressBar
from time import *
from txt.text import *
import random

now = datetime.now()
time = now.strftime("%H:%M:%S")
jour = date.today()
day = jour.strftime("%d/%m/%y")

CBlack = "\033[90m"
CRed = "\033[91m"
CGreen = "\033[92m"
CYellow = "\033[93m"
CYellow2 = "\033[33m"
CBlue = "\033[94m"
CPurple = "\033[95m"
CBeige = "\033[96m"
CWhite = "\033[97m"
CClear = "\033[30m"
CEnd = "\033[0m"

ColorList = [CRed, CGreen, CYellow, CYellow2, CBlue, CBeige]
color = random.choice(ColorList)

def important():
    cls()
    base()
    print(cmdline)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def base():
    print(f"""\
        {color}
    |   |  |  |   _)                    |               ___|                                  |               
    |   |  |  __|  |  __ `__ \    _` |  __|   _ \      |       _ \   __ \ \ \   /  _ \   __|  __|   _ \   __| 
    |   |  |  |    |  |   |   |  (   |  |     __/      |      (   |  |   | \ \ /   __/  |     |     __/  |    
    \___/ _| \__| _| _|  _|  _| \__,_| \__| \___|      \____| \___/ _|  _|  \_/  \___| _|    \__| \___| _|    
{CEnd}""")
    if platform.system() == "Windows" and platform.release() == "10":
        print(f"""\
                        {CBlue}....,,:;+ccllll   
          ...,,+:;  cllllllllllllllllll   
    ,cclllllllllll  lllllllllllllllllll   
    llllllllllllll  lllllllllllllllllll   
    llllllllllllll  lllllllllllllllllll      {CEnd}Time :    [ {CRed}{day}{CEnd} |  {CGreen}{time}{CEnd} ]{CBlue}
    llllllllllllll  lllllllllllllllllll   
    llllllllllllll  lllllllllllllllllll      {CEnd}Author :  [ {CGreen}Imprevisible{CEnd} ]{CBlue}
    llllllllllllll  lllllllllllllllllll   
                                             {CEnd}Version : [ {CBlue}0.1{CEnd} ]{CBlue}
    llllllllllllll  lllllllllllllllllll   
    llllllllllllll  lllllllllllllllllll      {CEnd}PC :      [ {CYellow}{platform.system()} {platform.release()}{CEnd} ]{CBlue}
    llllllllllllll  lllllllllllllllllll
    llllllllllllll  lllllllllllllllllll                {CEnd}[ {color}{random.choice(text)}{CEnd} ]{CBlue}
    llllllllllllll  lllllllllllllllllll
    `'ccllllllllll  lllllllllllllllllll
           `' \*::  :ccllllllllllllllll
                           ````''*::cll{CEnd}
    """)
    elif platform.system() == "Windows" and platform.release() == "11":
        print(f"""\
    {CBeige}################  ################
    ################  ################
    ################  ################
    ################  ################      {CEnd}Time :    [ {CRed}{day}{CEnd} |  {CRed}{time}{CEnd} ]{CBeige}
    ################  ################
    ################  ################      {CEnd}Author :  [ {CGreen}Imprevisible{CEnd} ]{CBeige}
    ################  ################
    ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ{CEnd}Version : [ {CBlue}0.1{CEnd} ]{CBeige}
    ################  ################
    ################  ################      {CEnd}PC :      [ {CYellow}{platform.system()} {platform.release()}{CEnd} ]{CBeige}
    ################  ################
    ################  ################                {CEnd}[ {color}{random.choice(text)}{CEnd} ]{CBeige}
    ################  ################
    ################  ################
    ################  ################{CEnd}
    """)
    elif platform.system() == "Windows" and platform.release() == "7":
        print(f"""\
{CRed}        ,.=:!!t3Z3z.,
{CRed}       :tt:::tt333EE3
{CRed}       Et:::ztt33EEEL {CGreen}@Ee.,      ..,
{CRed}      ;tt:::tt333EE7 {CGreen};EEEEEEttttt33#
{CRed}     :Et:::zt333EEQ. {CGreen}$EEEEEttttt33QL        {CEnd}Time :    [ {CRed}{day}{CEnd} |  {CRed}{time}{CEnd} ]
{CRed}     it::::tt333EEF {CGreen}@EEEEEEttttt33F
{CRed}    ;3=*^```"*4EEV {CGreen}:EEEEEEttttt33@.         {CEnd}Author :  [ {CGreen}Imprevisible{CEnd} ]
{CBlue}    ,.=::::!t=., {CRed}` {CGreen}@EEEEEEtttz33QF
{CBlue}   ;::::::::zt33)   {CGreen}"4EEEtttji3P*           {CEnd}Version : [ {CBlue}0.1{CEnd} ]
{CBlue}  :t::::::::tt33.{CYellow}:Z3z..  {CGreen}`` {CYellow},..g.
{CBlue}  i::::::::zt33F {CYellow}AEEEtttt::::ztF            {CEnd}PC :      [ {CYellow}{platform.system()} {platform.release()}{CEnd} ]
{CBlue} ;:::::::::t33V {CYellow};EEEttttt::::t3
{CBlue} E::::::::zt33L {CYellow}@EEEtttt::::z3F                       {CEnd}[ {color}{random.choice(text)}{CEnd} ]
{CBlue}(3=*^```"*4E3) {CYellow};EEEtttt:::::tZ`
            {CBlue} ` {CYellow}:EEEEtttt::::z7
                 {CYellow}"VEzjt:;;z>*`{CEnd}
                 """)
    
    elif platform.system() == "Linux":
        print(f"""\
           {CBlack}#####
          #######
          ##{CWhite}O{CBlack}#{CWhite}O{CBlack}##                           {CEnd}Time :    [ {CRed}{day}{CEnd} |  {CRed}{time}{CEnd} ]
          {CBlack}#{CYellow}#####{CBlack}#
        {CBlack}##{CWhite}##{CYellow}###{CWhite}##{CBlack}##                         {CEnd}Author :  [ {CGreen}Imprevisible{CEnd} ]
       {CBlack}#{CWhite}##########{CBlack}##
      {CBlack}#{CWhite}############{CBlack}##                       {CEnd}Version : [ {CBlue}0.1{CEnd} ]
      {CBlack}#{CWhite}############{CBlack}###
    {CYellow}##{CBlack}#{CWhite}###########{CBlack}##{CYellow}#                       {CEnd}PC :      [ {CYellow}{platform.system()} {platform.release()}{CEnd} ]
   {CYellow}######{CBlack}#{CWhite}#######{CBlack}#{CYellow}######
   {CYellow}#######{CBlack}#{CWhite}#####{CBlack}#{CYellow}#######                              {CEnd}[ {color}{random.choice(text)}{CEnd} ]   
     {CYellow}#####{CBlack}#######{CYellow}#####{CEnd}
    """)
    elif platform.system() == "Darwin":
        print(f"""\
                   {CGreen} c.'
                 ,xNMM.
               .OMMMMo
               lMM"
     .;loddo:.  .olloddol;.                 {CEnd}Time :    [ {CRed}{day}{CEnd} |  {CRed}{time}{CEnd} ]{CGreen}
   cKMMMMMMMMMMNWMMMMMMMMMM0:{CYellow}
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.               {CEnd}Author :  [ {CGreen}Imprevisible{CEnd} ]{CYellow}
 XMMMMMMMMMMMMMMMMMMMMMMMX. {CRed}     
;MMMMMMMMMMMMMMMMMMMMMMMM:                  {CEnd}Version : [ {CBlue}0.1{CEnd} ]{CRed}
:MMMMMMMMMMMMMMMMMMMMMMMM:       
.MMMMMMMMMMMMMMMMMMMMMMMMX.                 {CEnd}PC :      [ {CYellow}{platform.system()} {platform.release()}{CEnd} ]{CRed}
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.{CPurple}
 'XMMMMMMMMMMMMMMMMMMMMMMMMMMk                        {CEnd}[ {color}{random.choice(text)}{CEnd} ]{CPurple} 
  'XMMMMMMMMMMMMMMMMMMMMMMMMK.{CBlue}
    kMMMMMMMMMMMMMMMMMMMMMMd
     ;KMMMMMMMWXXWMMMMMMMk.
       "cooc*"    "*coo'"{CEnd}
    """)   
    else:
        print(f"""\
           {CGreen} ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####                {CEnd}Time :    [ {CRed}{day}{CEnd} |  {CRed}{time}{CEnd} ]{CGreen}
                       d###P
                    _g###@F                 {CEnd}Author :  [ {CGreen}Imprevisible{CEnd} ]{CGreen} 
                 _gN##@P
               gN###F"                      {CEnd}Version : [ {CBlue}0.1{CEnd} ]{CGreen}
              d###F
             0###F                          {CEnd}PC :      [ {CYellow}{platform.system()} {platform.release()}{CEnd} ]{CGreen}
             0###F
             0###F                                    {CEnd}[ {color}{random.choice(text)}{CEnd} ]{CGreen}
             "NN@'

              ___
             q###r
              ""{CEnd}""")      


def loading():
    cls()
    pb = ProgressBar(total=100,prefix=f'{color}Loading', suffix=f'{CEnd}', decimals=3, length=50, fill='X', zfill='-')
    for i in range(100):
        pb.print_progress_bar(i)
        sleep(0.005)