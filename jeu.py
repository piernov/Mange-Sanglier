# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel

# Programme qui affiche un message a la fin du jeu et demande si l'on veut rejouer

from turtle import *
import dessin
import interface

meilleurScore = 0

def clic(x, y, Etat):
	cases = Etat["cases"]
	i = 0
	while i < len(cases):
		if x < cases[i][2] and x > cases[i][0] and y < cases[i][3] and y > cases[i][1]:
			print(i)
			if i in Etat["placepokemons"]:
				dessin.texte(cases[i][0]+10, cases[i][1]+10, "Found!")
				print("MIAOUNYAN")
		i+=1
	return True

def fin(resultat,score):
    #La tortue écrit en coordonnée x1 et y1 le message
    if resultat:
        dessin.texte(x1,y1,"Félicitation vous avez gagné !")
        i = score
        if score > meilleurScore:
            meilleurScore = i
             
        else :
            dessin.texte(x1,y1,"Vous avez réalisé un score de : " + str(score) )
    else :
         dessin.texte(x1,y1,"Vous avez malheureusement perdu.")
    # Bouton qui permet de jouer une nouvelle partie
    dessin.texte(x1,y1-20,"Recommencer ?")
    dessin.bouton("Oui", x1, y1-40)
    dessin.bouton("Non", x1+40, y1-40)
