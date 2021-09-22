'''
*** Exo 6: Générateur de mot de passe ***
Créer un programme qui génère un mot de passe de longueur variable
en concaténant des caractères de façon aléatoire.
Le mot de passe devra contenir:
- au moins une majuscule
- au moins une minuscule
- au moins une valeur numérique
- au moins au caractères spécial (/;|%, etc.)

La longeur sera donnée par une saisie utilisateur
ex: longueur: 8 => Hn_y9l2%
'''
print("*** EXO 5: Générateur de mot de passe ***")
from random import choice, randint

alphabetMin = [ chr(i) for i in range (97,123) ]
alphabetMaj = [ chr(i) for i in range (65,91) ]
digit = [ chr(i) for i in range (48,58) ]
special = [ chr(i) for i in range (33,48)]



def password(n, min= True, maj = True, chiffre = True, cspecial = True):
    alphabets = dict()
    key = 0
    if min:
        alphabets[key] = alphabetMin
        key += 1
    if maj:
        alphabets[key] = alphabetMaj
        key += 1
    if chiffre:
        alphabets[key] = digit
        key += 1
    if cspecial:
        alphabets[key] = special
        key += 1
    pwd = ''
    for i in range(n):
        s = randint(0,key-1)
        pwd += choice( alphabets[s])
    return pwd

print(password(5))