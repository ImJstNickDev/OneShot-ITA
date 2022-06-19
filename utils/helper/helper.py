from time import sleep

while(1):
    while(1):
        sleep(0.5)
        try:
            f = open('DOCUMENT.oneshot.txt', 'r')
            #print("Opened.")
        except OSError:
            break
        datafile = f.read()
        code = datafile[-7:-1]
        #print(code)
        if("Dear" in datafile):
            try:
                f1 = open('out.txt', 'r')
            except OSError:
                f1 = open('out.txt', 'w')
                f2 = open('codes/code1ita.txt', 'r')
                dataf2 = f2.read()
                f1.write(dataf2)
                f1.write(code)
                print("trovato e scritto.")
                f1.close()
        f.close()