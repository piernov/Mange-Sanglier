from turtle import *
import dessin

meilleurScore = 0

def fin(resultat,score):
    if resultat:
        dessin.texte(x1,y1,"Félicitation vous avez gagné !") #La tortue écrit en haut à gauche le texte
        i = score
        if score > meilleurScore:
            meilleurScore = i
             
        else :
            dessin.texte(x1,y1,"Vous avez réalisé un score de : " + str(score) )
    else :
         dessin.texte(x1,y1,"Vous avez malheureusement perdu.") # La torue écrit en haut à gauche le texte
    dessin.texte(x1,y1-20,"Recommencer ?")
    dessin.bouton("Oui", x1, y1-40)
    dessin.bouton("Non", x1+40, y1-40)
