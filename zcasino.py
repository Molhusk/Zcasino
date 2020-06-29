import math
import random
import os
import pickle

os.chdir(os.getcwd())

i= int()

butin = 500
init = {'initializate' : 0}

playerName = input('Quel est votre nom de joueur ?')
playerName = playerName.lower()

saveFound = False

create = open('saved files/coinStatus.txt','wb')
crt = create.write(str(init))
create.close()

saved = open('saved files/coinStatus.txt','rb')
savedStr = saved.read()
saved.close()

saveList = savedStr.split(',') #on crée une liste qui contient chaque valeur du dictionnaire, utilisé pour len()



with open('saved files/coinStatus.txt', 'rb') as file :
    recoverSave = pickle.Unpickler(file)
    dic = recoverSave.load()

for key in dic.keys(): #Si aucune clé, la boucle ne démarre pas !
    print(key)
    if playerName == key:
        butin = dic[key]
        saveFound = True
if saveFound == False:
    print('Aucune Sauvegarde trouvée, création du joueur...')
    dic[playerName] = butin
    with open('saved files/coinStatus.txt','ab') as file :
        newSave = pickle.Pickler(file)
        newSave.dump(dic)
#Bloc de test d'écriture sur fichier
with open('saved files/coinStatus.txt','rb') as file :
    test = pickle.Unpickler(file)
    dic = test.load()


power = True 

while power == True :
    choix = input('Sur quel chiffre voulez vous miser ?')
    if choix.lower() == 'q':
        save = open('saved files/casinoCoin.txt','w')
        butin = str(butin)
        save = save.write(butin)
        break
    try:
        choix = int(choix)
        assert choix < 50 and choix >= 0
    except ValueError :
        print('Vous n\'avez pas saisi un chiffre')
        continue
    except AssertionError :
        print('Le nombre saisi doit être dans l\'intervalle 0-49')
        continue
    if choix%2 == 0:
        print('Vous avez choisi le ',choix,' Noir')
    else:
        print('Vous avez choisi le ',choix,' Rouge')

    montantMise = input('Combien voulez-vous miser ?')
    try :
        montantMise = int(montantMise)
    except ValueError :
        print('Vous n\'avez pas saisi un chiffre')
        continue
    if montantMise > butin or montantMise <= 0:
        print('Vous n\avez pas les moyens, ou ce chiffre est négatif')
        print('Votre fortune est actuellement de : ',butin)
        continue
    butin = butin - montantMise
    print('Les jeux sont faits...')
    nbr_roulette = random.randrange(0, 49)
    couleur='vert'
    if nbr_roulette%2 == 0:
        couleur = 'Noir'
    elif nbr_roulette%2 != 0:
        couleur = 'Rouge'
        
    print('La bille s\'arrête sur le ',nbr_roulette,' ',couleur)

    if nbr_roulette == choix:
        montantMise = montantMise*3
        butin = butin + montantMise
        print('Bravo, vous avez gagné ',montantMise,' vous avez dorénavant : ',butin)
    elif nbr_roulette%2 == 0 and choix%2 == 0 and nbr_roulette != choix :
        montantMise = math.ceil(montantMise/2)
        butin = butin + montantMise
        print('Vous êtes tombé sur un chiffre Noir, vous récupérez donc ',montantMise,' il vous reste donc ',butin)
    elif nbr_roulette%2 == 1 and choix%2 == 1 and nbr_roulette != choix:
        montantMise = math.ceil(montantMise/2)
        butin = butin + montantMise
        print('Vous êtes tombé sur un chiffre Rouge, vous récupérez donc ',montantMise,' il vous reste donc ',butin)
    else :
        print('Dommage vous avez perdu, il vous reste actuellement ',butin)
    if butin <= 0 :
        power = False
