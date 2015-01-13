# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel

# programme qui permet de dessiner le quadrillage du jeu, et les éléments de graphismes

import turtle
import interface
import random

def ligne(x1, y1, x2, y2):
	# Fonction qui dessigne les lignes du quadrillage, la tortue prend comme arguments le point de coordonées (x1,y1) comme début de ligne
	#et le point de coordonées (x2,y2) comme point de fin de ligne 
	turtle.up()
	turtle.goto(x1, y1)
	turtle.down()
	turtle.goto(x2,y2)

def rectangle(x1, y1, x2, y2, fillcolor=False, color="black"):
	turtle.color(color)

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

def triangle (x,y,longueur):
	turtle.up()
	turtle.goto(x,y)
	turtle.down ()

	i=0
	while i<=2:
		turtle.left(240)
		turtle.forward(longueur)
		i=i+1

def cercle(x, y, r, fillcolor=False, color="black"):
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


def texte(x,y,txt, align="left", color="black") :
	# Fonction qui fait écrire un texte à la tortue pour donner des informations à l'utilisateur
	# Elle prend pour arguments les coordonnée du point qui correspond au début du message
	turtle.color(color)
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

def herbe (x,y,i):
	somme = 0
	r=0
	turtle.fillcolor('green')

	while r<= i :
		turtle.begin_fill()
		longueur= random.randint(10,65)
		triangle(x+somme+longueur,y,longueur)
		somme += longueur
		r=r+1
		turtle.end_fill()

def soleil (x,y,rayon,longueur):
	turtle.pencolor('yellow')
	turtle.up()
	turtle.goto(x,y)
	turtle.down()
	turtle.fillcolor('yellow')
	turtle.begin_fill()
	turtle.circle (rayon)
	turtle.end_fill()

	turtle.up()
	turtle.goto(x-rayon,y+rayon)
	turtle.down()
	turtle.forward(-longueur)
	turtle.up()
	turtle.goto(x+rayon,y+rayon)
	turtle.down()
	turtle.forward(longueur)

	turtle.up()
	turtle.goto(x,y+2*rayon)
	turtle.down()
	turtle.left(90)
	turtle.forward(longueur)
	turtle.up()
	turtle.goto(x,y+2*rayon)
	turtle.down()
	turtle.forward(-longueur)
	turtle.right(90)

def champignon(x1,y1):
	x2 = x1+40
	y2 = y1+50
	r = (x1+x2)/2
	rectangle(x1, y1, x2, y2, fillcolor="white")

	r = 30
	turtle.up()
	turtle.goto((x1+x2)/2,y1-2*r)
	turtle.down()
	turtle.fillcolor('red')
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

	r = 10
	turtle.fillcolor('white')
	turtle.up()
	turtle.goto(x1+5,y1-2*r)
	turtle.down()
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

	turtle.up()
	turtle.goto(x2-5,y1-2*r)
	turtle.down()
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

def pattesTete (x1,y1,x2,y2):
	turtle.fillcolor('brown')
	turtle.up()
	turtle.goto(x1,y2)
	turtle.down()
	i=0
	turtle.begin_fill()
	while i<3:
		turtle.left(90)
		turtle.forward(y2-y1)
		i=i+1
	turtle.end_fill()
	turtle.up()
	turtle.goto(x2,y2)
	turtle.down()
	turtle.right(180)
	
	i=0
	turtle.begin_fill()
	while i<3:
		turtle.forward(y2-y1)
		turtle.left(90)
		i=i+1
	turtle.end_fill()
	
	turtle.up()
	turtle.goto(x2,y2)
	i=0
	turtle.down()
	turtle.begin_fill()
	while i<3:
		turtle.forward (y2-y1)
		turtle.right(90)
		i=i+1
	turtle.end_fill()

	turtle.up()
	turtle.goto(x2,-10+(y2+y1)/2)
	turtle.right(90)
	turtle.forward ((y2-y1)/2)
	turtle.down()
	turtle.fillcolor('white')
	turtle.begin_fill()
	turtle.circle(5)
	turtle.end_fill()

# Fonction qui dessine le marcassin
def marcassin(x1,y1,x2,y2):
	rectangle (x1,y1,x2,y2,fillcolor="brown")
	pattesTete (x1+y2-y1,y1,x2,y2)
