import turtle
import random
import dessin
import interface
import jeu

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

wm = turtle.Screen()

pokemons = {
	"Sanglier" : 4,
	"Laie" : 3 ,
	"Marcassin" : 1 
}

niveaux = [
	{ "pokemons" : { "Sanglier": 0, "Laie": 3, "Marcassin": 3}, "cases": [10, 10] }
]

Config = {
	"niveau" : 0
}

Etat = {
	"cases" : [],
	"niveau" : 0,
	"ncol" : 0,
	"nligne" : 0,
	"placepokemons" : {}
}

def selNextCase(ncase, direction, ncol, nligne):
	c, l = interface.caseVersCL(ncase, ncol, nligne)

	if direction == UP:
		l -= 1
	elif direction == RIGHT:
		c += 1
	elif direction == DOWN:
		l += 1
	elif direction == LEFT:
		c -= 1
	n = c+l*ncol

	return n

def placerPokemon(nCases, pokemon, num, placepokemons, ncol, nligne):
	finished = False
	while not finished:
		tmpCases = {}
		n = random.randint(0, 99)
		tmpCases[n] = pokemon


		if nCases == 3:
			direction = random.randint(0,3)
			n = selNextCase(n, direction, ncol, nligne)
			tmpCases[n] = pokemon
			if direction == 0 or direction == 2:
				direction = random.randint(0,1)*2+1
			else:
				direction = random.randint(0,1)*2
			n = selNextCase(n, direction, ncol, nligne)
			tmpCases[n] = pokemon

		# TODO : nCases == 4

		finished = True
		for k, v in tmpCases.items():
			if n in placepokemons or n < 0 or n > ncol*nligne:
				finished = False

	for k, v in tmpCases.items():
		placepokemons[k] = v+str(num)

def placerPokemons(pokemonsNiv, ncol, nligne):
	placepokemons = {}
	for key, value in pokemonsNiv.items():
		i = 1
		while i <= value:
			placerPokemon(pokemons[key], key, i, placepokemons, ncol, nligne)
			print(i, placepokemons)
			i += 1

	# Debug
	for key, value in placepokemons.items():
		print(key,value)

	return placepokemons

def clicHandle(x, y):
	jeu.clic(x, y, Etat)

def initEtat(Etat):
	Etat["niveau"] = Config["niveau"]
	Etat["ncol"] = niveaux[Etat["niveau"]]["cases"][0]
	Etat["nligne"] = niveaux[Etat["niveau"]]["cases"][1]
	
	Etat["cases"] = interface.genQuadrillage(50, 50, turtle.window_width()-50, turtle.window_height()-50, Etat["ncol"], Etat["nligne"])

	Etat["placepokemons"] = placerPokemons(niveaux[Etat["niveau"]]["pokemons"], Etat["ncol"], Etat["nligne"])

def main():
	initEtat(Etat)

	interface.initTurtle()

	dessin.quadrillage(Etat["cases"])

	wm.onclick(clicHandle)

	wm.listen()	
	wm.mainloop()

main()
