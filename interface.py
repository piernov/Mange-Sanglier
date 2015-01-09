# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel
# Programme qui initialise l'interface
import turtle
import dessin

boutons = []

def initTurtle():
	# Fonction qui initialise la position de la tortue
	# Setworldcoordinates redéfini le système de coordonnées
	turtle.setworldcoordinates(0, turtle.window_height(), turtle.window_width(), 0)
	turtle.tracer(n=0, delay=0)
	turtle.bgcolor("SandyBrown")

def genQuadrillage(x1, y1, x2, y2, nbLignes, nbColonnes):
	# Fontion qui crée un tableau les cases qui ont pour argument le point en haut à gauche et le point en bas à droite de la case
	cases = []
	largeur = x2-x1
	hauteur = y2-y1
	for i in range(nbLignes):
		for j in range(nbColonnes):
			cases.insert(j+i*nbColonnes, [x1+largeur*j/nbColonnes, y1+hauteur*i/nbLignes, x1+largeur*(j+1)/nbColonnes, y1+hauteur*(i+1)/nbLignes] )
	return cases

def dessinQuadrillage(cases, ncol, nligne):
	# Fonction qui a pour argument le nombre de cases qu'il faut dans la partie
	i = 0
	while i < len(cases):
		c, l = caseVersCL(i, ncol, nligne)
		if c == 0:
			dessin.texte(cases[i][0]-15, (cases[i][1]+cases[i][3]+20)/2, l)
		if l == 0:
			dessin.texte((cases[i][0]+cases[i][2])/2, cases[i][1]-5, c)
		dessin.rectangle(*cases[i])
		i+=1

def dessinHud(Etat):
	dessin.rectangle(-9, -9, 120, 60, fillcolor="white")
	dessin.texte(10, 20, "Score : " + str(Etat["score"])) # Affiche le score
	dessin.texte(5, 40, " Niveau : " + str(Etat["niveau"])) # Affiche le niveau

# Dessine l'interface
def dessine(Etat):
	turtle.color("black")
	dessinQuadrillage(Etat["cases"], Etat["ncol"], Etat["nligne"]) # Dessine le quadrillage
	dessinHud(Etat)
	dessin.arbre(20, 150)

# Conversion du numéro de case vers numéro de colonne et de ligne
def caseVersCL(case, ncol, nligne):
	return case%nligne, case//ncol # (colonne, ligne)

def bouton(x, y, txt, callback):
	xx, yy = dessin.bouton(x, y, txt)
	boutons.append([x, y, xx, yy, callback])
	
def verifBouton(x, y):
	for i in boutons:
		if x > i[0] and x < i[2] and y > i[1] and y < i[3]:
			return i[4]()
