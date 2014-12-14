import turtle

def ligne(x1, y1, x2, y2):
	turtle.up()
	turtle.goto(x1, y1)
	turtle.down()
	turtle.goto(x2,y2)

def rectangle(x1, y1, x2, y2):
	ligne(x1, y1, x2, y1)
	ligne(x2, y1, x2, y2)
	ligne(x2, y2, x1, y2)
	ligne(x1, y2, x1, y1)

def texte(x,y,texte, align="left") :
	turtle.up()
	turtle.goto (x,y)
	turtle.down()
	turtle.write (texte, align=align)

def bouton(texte, x, y):
	xx = x+30
	yy = y-15
	texte((xx+x)/2, yy, texte, align="center")
	rectangle(x, y, xx, yy)

def quadrillage(cases):
	for case in cases:
		rectangle(*case)
