# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel

# programme qui permet de dessiner le quadrillage du jeu, et les éléments de graphismes

import turtle

def ligne(x1, y1, x2, y2):
        # Fonction qui dessigne les lignes du quadrillage, la tortue prend comme arguments le point de coordonées (x1,y1) comme début de ligne
        #et le point de coordonées (x2,y2) comme point de fin de ligne 
	turtle.up()
	turtle.goto(x1, y1)
	turtle.down()
	turtle.goto(x2,y2)

def rectangle(x1, y1, x2, y2):
# Fonction qui prend pour arguments les coordonnées de deux points du rextangle
	ligne(x1, y1, x2, y1)
	ligne(x2, y1, x2, y2)
	ligne(x2, y2, x1, y2)
	ligne(x1, y2, x1, y1)

def texte(x,y,texte, align="left") :
        # Fonction qui fait écrire un texte à la tortue pour donner des informations à l'utilisateur
        # Elle prend pour arguments les coordonnée du point qui correspond au début du message
	turtle.up()
	turtle.goto (x,y)
	turtle.down()
	turtle.write (texte, align=align)

def bouton(texte, x, y):
        # Fonction qui fait le dessin d'un bouton rectangulaire qui prend pour argument un texte à l'intérieur, centré, et les coordonnées de la position de ce bouton
	xx = x+30
	yy = y-15
	texte((xx+x)/2, yy, texte, align="center")
	rectangle(x, y, xx, yy)

def quadrillage(cases):
  # Fonction qui a pour argument le nombre de cases qu'il faut dans la partie
	for case in cases:
		rectangle(*case)
