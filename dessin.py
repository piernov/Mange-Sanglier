# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel

# programme qui permet de dessiner le quadrillage du jeu, et les éléments de graphismes

import turtle
import interface

def ligne(x1, y1, x2, y2):
        # Fonction qui dessigne les lignes du quadrillage, la tortue prend comme arguments le point de coordonées (x1,y1) comme début de ligne
        #et le point de coordonées (x2,y2) comme point de fin de ligne 
	turtle.up()
	turtle.goto(x1, y1)
	turtle.down()
	turtle.goto(x2,y2)

def rectangle(x1, y1, x2, y2, fillcolor=False, color="white"):

	if fillcolor:
		turtle.fillcolor(fillcolor)
		turtle.begin_fill()
# Fonction qui prend pour arguments les coordonnées de deux points du rextangle
	ligne(x1, y1, x2, y1)
	ligne(x2, y1, x2, y2)
	ligne(x2, y2, x1, y2)
	ligne(x1, y2, x1, y1)
	if fillcolor:
		turtle.end_fill()

def cercle(x, y, r, fillcolor=False, color="white"):
	turtle.color(color)

	if fillcolor:
		turtle.fillcolor(fillcolor)
		turtle.begin_fill()

	turtle.up()
	turtle.goto(x,y)
	turtle.down()
	turtle.circle(r)

	if fillcolor:
		turtle.end_fill()


def texte(x,y,txt, align="left") :
        # Fonction qui fait écrire un texte à la tortue pour donner des informations à l'utilisateur
        # Elle prend pour arguments les coordonnée du point qui correspond au début du message
	turtle.up()
	turtle.goto (x,y)
	turtle.down()
	turtle.write (txt, align=align, font=(None, 18, "normal"))

def bouton(x, y, txt):
        # Fonction qui fait le dessin d'un bouton rectangulaire qui prend pour argument un texte à l'intérieur, centré, et les coordonnées de la position de ce bouton
	xx = x+40
	yy = y+20
	texte((xx+x)/2, yy, txt, align="center")
	rectangle(x, y, xx, yy)
	return xx, yy

def arbre(x1, y1):
	x2 = x1+30
	y2 = y1+150
	r = (x1+x2)/2
	rectangle(x1, y1, x2, y2, fillcolor="brown")
	cercle(x1, y1, r, fillcolor="green", color="green")
	cercle(x2, y1, r, fillcolor="green", color="green")
	cercle((x1+x2)/2, y1-r, r, fillcolor="green", color="green")
