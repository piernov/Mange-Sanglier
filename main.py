import turtle
import random
import dessin
import interface

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

wm = turtle.Screen()

cases = []

pokemons = {
	"Sanglier" : 4,
	"Laie" : 3 ,
	"Marcassin" : 1 
}

niveaux = [
	{ "pokemons" : { "Sanglier": 3, "Laie": 3, "Marcassin": 3}, "cases": [10, 10] }
]
niveau = 0
ncol = niveaux[niveau]["cases"][0]
nligne = niveaux[niveau]["cases"][1]
placepokemons = {}

def placerPokemon(nCases, pokemon, placepokemons):
	if nCases == 1:
		n = random.randint(0, 99)
		while n in placepokemons:
			n = random.randint(0, 99)

		placepokemons[n] = pokemon
	return placepokemons

def placerPokemons(pokemonsNiv, placepokemons):
	for key, value in pokemonsNiv.items():
		i = 1
		while i <= value:
			placepokemons = placerPokemon(pokemons[key], value, placepokemons)
			i += 1
		print(key, value)
	for key, value in placepokemons.items():
		print(key,value)
	return placepokemons

def clic(x, y):
	i = 0
	while i < len(cases):
		if x < cases[i][2] and x > cases[i][0] and y < cases[i][3] and y > cases[i][1]:
			print(i, interface.caseVersCL(i, ncol, nligne))
			if i in placepokemons:
				dessin.texte(cases[i][0], cases[i][1], "Found!")
				print("MIAOUNYAN")
		i+=1


cases = interface.genQuadrillage(50, 50, turtle.window_width()-50, turtle.window_height()-50, ncol, nligne)


placepokemons = placerPokemons(niveaux[0]["pokemons"], placepokemons)

interface.initTurtle()

dessin.quadrillage(cases)

wm.onclick(clic)

wm.listen()	
wm.mainloop()
