# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel

# Programme qui affiche un message a la fin du jeu et demande si l'on veut rejouer

from turtle import *
import dessin
import interface

meilleurScore = 0

# Clic sur bonne case
# i: numéro de la case
def hit(i, Etat):
	Etat["cases"][i].insert(4, "green") # La case devient verte
	Etat["score"] += Etat["ptPokemons"] # On augmente le score

	# Ci-dessous on cherche si toutes les cases pour un Pokémon ont été trouvées
	casesToutesTrouvees = True
	for k, v in Etat["placepokemons"].items():
		if Etat["placepokemons"][i] == v and ( len(Etat["cases"][k]) < 5 or Etat["cases"][k][4] != "green" ): # On cherche les cases qui ont le même identifiant de Pokémon et qui ne sont pas vertes, càd qui n'ont pas encore été trouvées
			casesToutesTrouvees = False

	if casesToutesTrouvees:
		print("Pokemon trouvé: " + str(Etat["placepokemons"][i]))

		# Ci-dessous on cherche si tous les Pokémons ont été trouvés
		pokemonsTousTrouves = True
		for k, v in Etat["placepokemons"].items():
			if len(Etat["cases"][k]) < 5 or Etat["cases"][k][4] != "green": # On cherche les cases qui ne sont pas vertes, càd qui n'ont pas encore été trouvées
				pokemonsTousTrouves = False

		if pokemonsTousTrouves:
			fin(True, Etat["score"]) # Gagné

# Clic sur mauvaise case
# i: numéro de la case
def miss(i, Etat):
	Etat["cases"][i].insert(4, "red") # La case devient rouge
	Etat["score"] -= Etat["ptMalus"] # On diminue le score
	if Etat["score"] <= Etat["ptLim"]: # Score inférieur à la limite
		fin(False, Etat["score"]) # Perdu

# Gestion du clic sur l'écran
def clic(x, y, Etat):
	cases = Etat["cases"]
	i = 0
	while i < len(cases): # On parcourt toutes les cases pour en trouver une qui contient les coordonnées du clic
		if len(cases[i]) > 4 and cases[i][4] == "red": # Si la case était rouge, elle redevient incolore
			del cases[i][4]
		if x < cases[i][2] and x > cases[i][0] and y < cases[i][3] and y > cases[i][1]: # Les coordonnées correspondent
			print(i) # Debug
			if i in Etat["placepokemons"]: # Un Pokémon est caché derrière cette case
				print(Etat["placepokemons"][i]) #Debug
				if len(cases[i]) <= 4: # Case incolore donc qui n'a pas été cliquée
					hit(i, Etat)
			else:
				miss(i, Etat)
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
