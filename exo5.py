'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png

Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")
import os, shutil

targetDir = "flagBis/"
os.makedirs(targetDir, exist_ok=True)

countFolder = './flags'
filesNames = os.listdir(countFolder)
filesNumber = len(filesNames)
for x in filesNames:
  if x != 'missing.png':
    nameMaj = x.upper()
    newName = nameMaj[:2]
    originalPath = './flags/%s' % x
    targetPath = './flagBis/%s' % newName
    shutil.copyfile(
      originalPath,
      targetPath
    )