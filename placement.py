# projet programmation peip1
# PAYET Marion
# NOVAC Pierre-Emmanuel
import random
import interface

# Constantes pour la direction de la prochaine case lors du placement aléatoire
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Retourne le numéro de la prochaine case en fonction de la case actuelle et de la direction à prendre
# ncase: numéro de la case courante
# direction: direction à prendre pour sélectionner la prochaine case
# ncol/nligne: nombre de colonne/ligne sur la grille
def selNextCase(ncase, direction, ncol, nligne):
	c, l = interface.caseVersCL(ncase, ncol, nligne) # On converti le numéro de case en numéro de ligne/colonne

	if direction == UP and l > 0:
		l -= 1
	elif direction == RIGHT and c < ncol:
		c += 1
	elif direction == DOWN and l < nligne:
		l += 1
	elif direction == LEFT and c > 0:
		c -= 1
	else: # On a atteint un des bords de la grille (ou la direction est invalide), fera échouer le placement
		return -1

	return c+l*ncol # On reconverti en numéro de case

# Placement aléatoire d'un Pokémon sur la grille
# nCases: nombre de cases occupées par le Pokémon
# pokemon: type du Pokémon
# num: numéro du Pokémon de ce type à placer
# placepokemons: Pokemons déjà placés
# ncol/nligne: nombre de colonne/ligne sur la grille
def placerPokemon(nCases, pokemon, num, placepokemons, ncol, nligne):
	fini = False # Indique que le Pokémon a été correctement placé
	while not fini: # Tant que le Pokémon n'est pas placé correctement, on re-sélectionne des cases aléatoirement
		tmpCases = {}
		n = random.randint(0, 99) # On choisi une case aléatoire
		tmpCases[n] = pokemon


		if nCases >= 3:
			direction1 = random.randint(0,3) # On choisit une direction aléatoire
			n = selNextCase(n, direction1, ncol, nligne) # Et on trouve la prochaine case
			tmpCases[n] = pokemon

			if direction1 == UP or direction1 == DOWN: # Si les 2 cases ont été placées verticalement
				direction = random.randint(0,1)*2+1 # La 3ème sera placées à droite ou à gauche par rapport à la 2nde
			else:
				direction = random.randint(0,1)*2 # Sinon en haut ou en bas

			n = selNextCase(n, direction, ncol, nligne)
			tmpCases[n] = pokemon

		if nCases == 4:
			# On complete le carré avec la dernière case
			if direction1 == UP:
				direction = DOWN
			elif direction1 == RIGHT:
				direction = LEFT
			elif direction1 == DOWN:
				direction = UP
			elif direction1 == LEFT:
				direction = RIGHT
			n = selNextCase(n, direction, ncol, nligne)
			tmpCases[n] = pokemon

		# Ci dessus on cherche si les numéros de cases trouvées sont correctes et si elles ne sont pas déjà occupées.
		fini = True
		for k, v in tmpCases.items():
			if k in placepokemons or k < 0 or k > ncol*nligne:
				fini = False # Placement incorrect

	# Enfin on ajoute les cases sélectionnées au tableau contenant les Pokémons placés
	for k, v in tmpCases.items():
		placepokemons[k] = v+str(num)

# Placement de tous les Pokémons sur la grille
# pokemonsNiv: Type et nombre de Pokémons de ce niveau
# pokemonsConf: nombre de case occupées par chaque Pokémons
# ncol/nligne: nombre de colonne/ligne sur la grille
def placerPokemons(pokemonsNiv, pokemonsConf, ncol, nligne):
	placepokemons = {} # Tableau qui contiendra le placement des Pokémons
	for key, value in pokemonsNiv.items():
		i = 1
		while i <= value:
			placerPokemon(pokemonsConf[key], key, i, placepokemons, ncol, nligne)
			i += 1

	# Debug
	for key, value in placepokemons.items():
		print(key,value)

	return placepokemons
