import os
import subprocess

if __name__ == '__main__':
    print("itroduceti comanda Bash: (nu uita de | ca separator -> ")
    comanda : str = input()
    comanda_despartita = comanda.split("|")

    oldProcess :subprocess = None
    for com in comanda_despartita:
        com_in_cuvinte = com.split(" ")
        if(oldProcess!=None):
            oldProcess = subprocess.Popen(com_in_cuvinte, stdin=oldProcess.stdout, stdout=subprocess.PIPE)
        else:
            oldProcess = subprocess.Popen(com_in_cuvinte, stdin=None, stdout=subprocess.PIPE)

    rezultat = oldProcess.communicate()[0]
    print(rezultat)

