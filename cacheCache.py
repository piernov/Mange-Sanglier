# projet programmation peip1 
# PAYET Marion
# NOVAC Pierre-Emmanuel
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
	{ "pokemons" : { "Sanglier": 3, "Laie": 3, "Marcassin": 3}, "cases": [10, 10] }
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

	if direction == UP and l > 0:
		l -= 1
	elif direction == RIGHT and c < ncol:
		c += 1
	elif direction == DOWN and l < nligne:
		l += 1
	elif direction == LEFT and c > 0:
		c -= 1
	else:
		return -1

	n = c+l*ncol

	return n

def placerPokemon(nCases, pokemon, num, placepokemons, ncol, nligne):
	finished = False
	while not finished:
		tmpCases = {}
		n = random.randint(0, 99)
		tmpCases[n] = pokemon


		if nCases >= 3:
			direction1 = random.randint(0,3)
			n = selNextCase(n, direction1, ncol, nligne)
			tmpCases[n] = pokemon
			if direction1 == 0 or direction1 == 2:
				direction = random.randint(0,1)*2+1
			else:
				direction = random.randint(0,1)*2
			n = selNextCase(n, direction, ncol, nligne)
			tmpCases[n] = pokemon

		# TODO : nCases == 4
		if nCases == 4:
			if direction1 == 0:
				direction = 2
			elif direction1 == 1:
				direction = 3
			elif direction1 == 2:
				direction = 0
			elif direction1 == 3:
				direction = 1
			n = selNextCase(n, direction, ncol, nligne)
			tmpCases[n] = pokemon

		finished = True
		for k, v in tmpCases.items():
			if k in placepokemons or k < 0 or k > ncol*nligne:
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
	turtle.clear()
	draw(Etat)

def initEtat(Etat):
	Etat["niveau"] = Config["niveau"]
	Etat["ncol"] = niveaux[Etat["niveau"]]["cases"][0]
	Etat["nligne"] = niveaux[Etat["niveau"]]["cases"][1]
	
	Etat["cases"] = interface.genQuadrillage(50, 50, turtle.window_width()-50, turtle.window_height()-50, Etat["ncol"], Etat["nligne"])

	Etat["placepokemons"] = placerPokemons(niveaux[Etat["niveau"]]["pokemons"], Etat["ncol"], Etat["nligne"])

def draw(Etat):
	dessin.quadrillage(Etat["cases"], Etat["ncol"], Etat["nligne"])

def main():
	initEtat(Etat)

	interface.initTurtle()

	draw(Etat)

	wm.onclick(clicHandle)

	wm.listen()	
	wm.mainloop()

main()
