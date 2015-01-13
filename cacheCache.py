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
			"cases" : [7, 7],						# Nombre de lignes et de colonnes dans la grille
			"ptPokemons" : 100,						# Points gagnés pour chaque bonne case
			"ptMalus" : 20,							# Points perdus pour chaque mauvaise case
			"ptLim" : -200							# Limite inférieure déclanchant la perte du jeu
		},
		{
			"pokemons" : { "Sanglier": 3, "Laie": 3, "Marcassin": 3},	# Nombre de Pokémons cachés
			"cases" : [10, 10],						# Nombre de lignes et de colonnes dans la grille
			"ptPokemons" : 100,						# Points gagnés pour chaque bonne case
			"ptMalus" : 20,							# Points perdus pour chaque mauvaise case
			"ptLim" : -200							# Limite inférieure déclanchant la perte du jeu
		},
		{
			"pokemons" : { "Sanglier": 1, "Laie": 1, "Marcassin": 1},	# Nombre de Pokémons cachés
			"cases" : [7, 7],						# Nombre de lignes et de colonnes dans la grille
			"ptPokemons" : 100,						# Points gagnés pour chaque bonne case
			"ptMalus" : 20,							# Points perdus pour chaque mauvaise case
			"ptLim" : -200							# Limite inférieure déclanchant la perte du jeu
		},
		{
			"pokemons" : { "Sanglier": 1, "Laie": 1, "Marcassin": 1},	# Nombre de Pokémons cachés
			"cases" : [10, 10],						# Nombre de lignes et de colonnes dans la grille
			"ptPokemons" : 100,						# Points gagnés pour chaque bonne case
			"ptMalus" : 20,							# Points perdus pour chaque mauvaise case
			"ptLim" : -200							# Limite inférieure déclanchant la perte du jeu
		}
	],

	# Niveau par défaut
	"niveau" : 0
}

def init(niveau, Etat):
	turtle.clear() # On efface l'écran
	initEtat(niveau, Etat) # Initilisation du jeu
	dessin.initTexte()
	interface.initBouton()
	interface.dessine(Etat) # On dessine l'interface

# Initialisation du tableau contenant les variables d'état du jeu
def initEtat(niveau, Etat):
	Etat["niveau"] = niveau
	Etat["nbNiveaux"] = len(Config["niveaux"])
	Etat["ncol"] = Config["niveaux"][niveau]["cases"][0]
	Etat["nligne"] = Config["niveaux"][niveau]["cases"][1]
	
	Etat["cases"] = interface.genQuadrillage(100, 100, turtle.window_width()-50, turtle.window_height()-50, Etat["ncol"], Etat["nligne"]) # 50px de marges
	Etat["placepokemons"] = placement.placerPokemons(Config["niveaux"][niveau]["pokemons"], Config["pokemons"], Etat["ncol"], Etat["nligne"])

	Etat["ptPokemons"] = Config["niveaux"][niveau]["ptPokemons"]
	Etat["ptMalus"] = Config["niveaux"][niveau]["ptMalus"]
	Etat["ptLim"] = Config["niveaux"][niveau]["ptLim"]
	Etat["score"] = 0
	Etat["fin"] = False

	Etat["reset"] = init


# Fonction appellée lors d'un clic
def clic(x, y, Etat):
	if Etat["fin"]:
		interface.verifBouton(x, y)
	else:
		turtle.clear() # On efface l'écran
		jeu.clic(x, y, Etat)
		interface.dessine(Etat) # On redessine l'interface

def main():
	wm = turtle.Screen() # Initialisation de l'affichage

	interface.initTurtle() # Initialisation de la tortue

	Etat = {}
	init(Config["niveau"], Etat)

	wm.onclick(lambda x,y,e=Etat: clic(x,y,e)) # Fonction lambda utilisée pour passer en argument l'état du jeu à la fonction clic() qui gère le clic

	wm.listen()
	wm.mainloop()

main()
