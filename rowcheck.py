#!/usr/bin/python

from distutils.log import error
import sys
from os import system, name
from getch import pause, getch
from time import sleep

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def RowCheck(n, args):
    counters = [-1, 0]
    verbose = False
    if(n == 1):
        if(("-p" not in args) and ("--print" not in args)):
            args.append("-sysprint")
    if(("-v" in args) or ("--verbose" in args)):
        verbose = True
    with open('it.po', 'r') as fp:
        righe = fp.readlines()

        for riga in righe:
            if("msgstr" in riga):
                counters[0]+=1
                if(verbose):
                    print("Riga aggiunta al totale, righe totali: {}".format(counters[0]))
                if('msgstr ""' not in riga):
                    counters[1]+=1
                    if(verbose):
                        print("Riga aggiunta alle tradotte, righe tradotte: {}".format(counters[1]))
        if(("-c" in args) or ("--clrscr" in args)):
            clear()
        if(("-p" in args) or ("--print" in args) or ("-sysprint" in args)):
            if(("-c" not in args) and ("--clrscr" not in args)):
                print("\n", end="")
            print("Righe totali:  {}".format(counters[0]))
            print("Righe fatte:   {}".format(counters[1]))
            print("Percentuale:   {}%\n".format(truncate((100 / counters[0]) * (counters[1]), 2)))
            if(("-c" in args) or ("--clrscr" in args)):
                if(n != 2 and n != 4):
                    print("Premi un qualsiasi tasto per continuare...")
                    getch()
                    clear()
        if("-sysprint" in args):
            args.remove("-sysprint")
        if((n == 3) or (n == 4)):
            return counters[1]
        else:
            return counters

ARG_LIST = ["-p", "-h", "-v", "--print", "--help", "--verbose", "-c", "--clrscr"]


def CheckArgs(args):
    retcode = 0
    for arg in args:
        if(arg not in ARG_LIST):
            retcode = ErrArgs(arg)
            break
    return retcode


def ErrArgs(arg):
    print("{} is not an argument, type -h or --help to see all the arguments".format(arg))
    return 5

def PrintToReadme(counters, args):
    row_index = 0
    with open('README.md', 'r') as readmefile:
        rows = readmefile.readlines()
        for row in range(0, len(rows) - 1):
            if("<sup><sub>" in rows[row]):
                row_index = row
        rows[row_index] = "<sup><sub>Progress (line): " + str(counters[1]) + "/" + str(counters[0]) + " (" + str(truncate((100 / counters[0]) * (counters[1]), 2)) + "%)</sub></sup>\n"
        with open('README.md', 'w') as newreadme_file:
            newreadme_file.writelines(rows)
            if(("-c" not in args) and ("--clrscr" not in args)):
                print("\n", end="")
            print("File riscritto con successo!", end="")
            if(("-c" in args) or ("--clrscr" in args)):
                print(" Premi un tasto qualsiasi per continuare...")
                getch()
            else:
                print("")



def PrintHelp():
    print("\nRowcheck controlla quante delle righe totali\nsiano state tradotte nel file di traduzione del\nprogetto OneShot - Italian Translation.")
    print("")
    print("Lista di argomenti:")
    print("\t-h o --help:    Richiama questa pagina")
    print("\t-v o --verbose: Stampa informazioni necessarie al debug (rallenta l'esecuzione)")
    print("\t-p o --print:   Stampa le informazioni sui dati raccolti")

def StartSession(session):
    with open('sett/session_start.txt', 'w') as session_file:
        session_file.write(str(session))

def StopSession(session):
    with open('sett/session_stop.txt', 'w') as session_file:
        session_file.write(str(session))
    with open('sett/session_start.txt', 'r') as start:
        with open('sett/session_stop.txt', 'r') as stop:
            startint = start.read()
            stopint = stop.read()
            sdonestr = str(int(stopint) - int(startint))
            print("Traduzioni fatte: {}".format(sdonestr))
            with open('sett/session_done.txt', 'w') as sdone:
                sdone.write(sdonestr)
            pause()

def main():
    gate = 0
    args = sys.argv
    args.pop(0)
    gate = CheckArgs(args)
    if(("-h" in args) or ("--help" in args)):
        gate = "5"
        PrintHelp()
    while gate != "5":
        if(("-c" in args) or ("--clrscr") in args):
            clear()
        print("1) Controlla le righe su file")
        print("2) Controlla le righe su file e modifica README.md")
        print("3) Start Session")
        print("4) Stop Session")
        print("5) Esci")
        print("")
        gate = input("Input: ")
        if((gate != "1") and (gate != "2") and (gate != "3") and (gate != "4") and (gate != "5")):
            print("Inserisci un input valido")  
            print("Premi un tasto qualsiasi per continuare...")
            getch()
            clear()
        else:
            if(gate == "1"):
                counters = RowCheck(1, args)
            elif(gate == "2"):
                counters = RowCheck(2, args)
                PrintToReadme(counters, args)
            elif(gate == "3"):
                StartSession(RowCheck(3, args))
            elif(gate == "4"):
                StopSession(RowCheck(4, args))
            elif(gate == "5"):
                if(("-c" in args) or ("--clrscr") in args):
                    clear()
                else:
                    print("")
                print("Uscita dal programma in corso...", end="")

if __name__ == "__main__":
    main()