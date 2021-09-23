'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")
import csv
score = 0
title = ""
counter = 0

with open("deniro.csv", "r") as csvFile:
    rows = csv.reader(csvFile, delimiter = ',')
    for r in rows:
        try:
            if int(r[1].strip()) > int(score):
                score = r[1].strip()
                title = r[2]
        except:
            pass
        try:
            if int(r[0].strip()) < 2011 and int(r[0].strip()) > 1999:
                counter += 1
        except:
            pass
    #print("Nom du film le mieux noté: %s" % title)
    #print("Nombre de films entre 2000 et 2010: %s" % counter)

f = open("./deniro-report.txt", "w")
f.write("Nom du film le mieux note: %s\r\n" % title)
f.write("Nombre de films entre 2000 et 2010: %s\r\n" % counter)
f.close
        

