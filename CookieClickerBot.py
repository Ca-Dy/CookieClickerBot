#CABELLO Dylan
import webbrowser   #Importer les fichiers nécessaires
print("webbrowser OK")
from pynput.mouse import Button, Controller
print("mouse OK")
import time
print("time OK")
mouse = Controller()    #Activer la fonction souris (commande avec pynput)

cookiePos = 198, 378    #Pour aller plus vite on fait une variable avec les coordonnées du cookie
time.sleep(15)      #Attendre 15 s pcq voilà
on = True       #Variable pour ajouter un boutton off (V2?)
n = 10  #Var pour définir le nombre de clicks
c = 0   #? A SUPPRIMER VAR INUTILE
a = 0   #Compteur pour définir le nombre d'améliorations
upgradeX = 1209     #Coordonnées X pour la première amélioration
upgradeY = 382      #// //  // / Y // /// // / / // / // / / / /
p = 100             #Compteur pour les clicks (changer si on change n)
counterpos = 0

def leftClick():        #Pour que ça soit plus facile on fait une fonction click gauche(1fois). Aussi pcq ya pas dans le paquet
    mouse.press(Button.left)
    mouse.release(Button.left)

def upgradePos(x, y, z):    #vraiment la fonction pour améliorer. Bouge la souris et click a fois soit 6 fois
    if a < 7:
        mouse.position = (y, z)
        x += 1
        z += 55
        leftClick()
    else:
        return False    #Pour être sûr que la fonction est off


def upgrade():      #Fonction pour les améliorations
    print("Upgrading")
    upgradePos(counterpos, upgradeX, upgradeY)
    print("Upgraded")
    print('mouse moved {0}'.format(mouse.position))

print("opening webbrowser")
webbrowser.open('http://orteil.dashnet.org/cookieclicker/')     #ouvre le lien du cookie clicker
print("webbrowser opened")
time.sleep(60)      #attendre 60s pour être sûr que la page soit chargée
print("web page loaded")

while True:
    mouse.position = (cookiePos)    #La souris va sur le cookie
    print('mouse moved {0}'.format(mouse.position))     #Indique la pos de la souris (x, y)
    time.sleep(10)       #Pause de 10s pour pas trop faire lagger
    print("Clicking in progress")
    mouse.click(Button.left, n)     #Click n 
    print("Click finished")


    if p == 200:    #Quand le bot a clické 200 fois, il appelle la fonction upgrade()
        upgrade()
    else:           #Quand le bot n'a pas atteint 200 clicks, on ajoute 10 à p comme un compteur
        n = 10
        p = p + 10
        print("Reset")
