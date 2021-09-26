'''
*** EXO 8: Heath Check ***
Créer un programme qui, à partir du fichier websites.txt
vérifie que chacun des sites listées répond
à raison d'une requête toutes les n secondes

la périodicité sera fournie en entrée par l'utilisateur

Un fichier de log contiendra:
- la date de la requpete
- l'url interrogée
- le status code obtenu ou une indication d'erreur en cas de non réponse
'''
print("*** EXO 8: Health Check ***")

# votre code ici

import requests as req
import time, datetime
 
rows = []
f = open("./websites.txt", "r")
for x in f:
    rows.append(x)
f.close

period = int(input("Time between each status check (seconds): "))
while True:
    time.sleep(period)
    f = open("./logFiles.txt", "a")
    for y in rows:
        try:
            response = req.get(y.strip())
            status = response.status_code
            now = datetime.datetime.now()
            f.write(" %s Status of %s is %s \n"  % (now,y,status))
        except:
            z = y.strip()
            f.write("Url invalid: %s \n" % z)
    print("Status checked, press crtl+c to stop")
    f.close

