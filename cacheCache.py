# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel
import turtle
import dessin
import interface
import jeu
import placement

# Configuration globale
Config = {
	# Type de Pokémons disponnibles et nombre de cases associées
	"pokemons" : {
		"Sanglier" : 4,
		"Laie" : 3 ,
		"Marcassin" : 1
	},

	# Configuration de chacun des niveaux
	"niveaux" : [
		{
			"pokemons" : { "Sanglier": 3, "Laie": 3, "Marcassin": 3},	# Nombre de Pokémons cachés
			"cases" : [10, 10],						# Nombre de lignes et de colonnes dans la grille
			"ptPokemons" : 100,						# Points gagnés pour chaque bonne case
			"ptMalus" : 10,							# Points perdus pour chaque mauvaise case
			"ptLim" : -300							# Limite inférieure déclanchant la perte du jeu
		}
	],

	# Niveau par défaut
	"niveau" : 0
}

# Initialisation du tableau contenant les variables d'état du jeu
def initEtat(niveau):
	Etat = {}

	Etat["niveau"] = niveau
	Etat["ncol"] = Config["niveaux"][niveau]["cases"][0]
	Etat["nligne"] = Config["niveaux"][niveau]["cases"][1]
	
	Etat["cases"] = interface.genQuadrillage(50, 50, turtle.window_width()-50, turtle.window_height()-50, Etat["ncol"], Etat["nligne"]) # 50px de marges
	Etat["placepokemons"] = placement.placerPokemons(Config["niveaux"][niveau]["pokemons"], Config["pokemons"], Etat["ncol"], Etat["nligne"])

	Etat["ptPokemons"] = Config["niveaux"][niveau]["ptPokemons"]
	Etat["ptMalus"] = Config["niveaux"][niveau]["ptMalus"]
	Etat["ptLim"] = Config["niveaux"][niveau]["ptLim"]
	Etat["score"] = 0

	return Etat


# Fonction appellée lors d'un clic
def clic(x, y, Etat):
	jeu.clic(x, y, Etat)
	turtle.clear() # On efface l'écran
	interface.draw(Etat) # On redessine l'interface

def main():
	wm = turtle.Screen() # Initialisation de l'affichage

	interface.initTurtle() # Initialisation de la tortue

	Etat = initEtat(Config["niveau"]) # Initilisation du jeu

	interface.draw(Etat) # On dessine l'interface

	wm.onclick(lambda x,y,e=Etat: clic(x,y,e)) # Fonction lambda utilisée pour passer en argument l'état du jeu à la fonction clic() qui gère le clic

	wm.listen()
	wm.mainloop()

main()
