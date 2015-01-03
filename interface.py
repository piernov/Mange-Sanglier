# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel
# Programme qui initialise l'interface
import turtle
import dessin

def initTurtle():
	# Fonction qui initialise la position de la tortue
	# Setworldcoordinates redéfini le système de coordonnées
	turtle.setworldcoordinates(0, turtle.window_height(), turtle.window_width(), 0)
	turtle.tracer(n=0, delay=0)

def genQuadrillage(x1, y1, x2, y2, nbLignes, nbColonnes):
	# Fontion qui crée un tableau les cases qui ont pour argument le point en haut à gauche et le point en bas à droite de la case
	cases = []
	largeur = x2-x1
	hauteur = y2-y1
	for i in range(nbLignes):
		for j in range(nbColonnes):
			cases.insert(j+i*nbColonnes, [x1+largeur*j/nbColonnes, y1+hauteur*i/nbLignes, x1+largeur*(j+1)/nbColonnes, y1+hauteur*(i+1)/nbLignes] )
	return cases

# Dessine l'interface
def draw(Etat):
	dessin.quadrillage(Etat["cases"], Etat["ncol"], Etat["nligne"]) # Dessine le quadrillage
	dessin.texte(10, 10, "Score : " + str(Etat["score"]) + " Niveau : " + str(Etat["niveau"])) # Affiche le niveau et le score

# Conversion du numéro de case vers numéro de colonne et de ligne
def caseVersCL(case, ncol, nligne):
	return case%nligne, case//ncol # (colonne, ligne)
