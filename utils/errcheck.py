defid = []
itid = [] 
with open('default.txt', 'r') as deftxt:
    with open('it.txt', 'r') as ittxt:
        deflist = deftxt.readlines()
        itlist = ittxt.readlines()
        for line in deflist:
            if("msgid" in line):
                defid.append(line)
        for line in itlist:
            if("msgid" in line):
                itid.append(line)
        defidlen = len(defid)
        itidlen = len(itid)
        if(defidlen != itidlen):
            print("Lunghezza di lista differente")
        else:
            for x in range(0, len(defid)):
                if(defid[x] != itid[x]):
                    print("Errore di lista numero {}, stringa:\nDefault: \"{}\"\nItalian: \"{}\"".format(x, defid[x], itid[x]))
        print("Processo terminato...")
                