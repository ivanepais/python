import turtle
bob = turtle.Turtle()
print(bob)
#turtle.mainloop()

#mover, desactivar mloop

#angulo 90°
'''
bob.fd(100)
bob.lt(90)
bob.fd(100)
'''
'''
bob.fd(100)
bob.bk(100)
bob.lt(90)
bob.fd(100) #repetición
bob.rt(90)
bob.fd(100)
bob.rt(90) 
bob.fd(100) # 
'''

'''
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90) 
bob.fd(100) 
'''
'''
for i in range(4):
	bob.fd(100) #avanza, gira *4
	bob.lt(90)
'''

'''
for i in range(4):
	bob.fd(100) #forma cruz o tablero
	bob.bk(100)
	bob.lt(90)
	bob.fd(100) 
	bob.rt(90)
	bob.fd(100)
	bob.rt(90) 
	bob.fd(100)
'''

#turtle.mainloop()


def cuadrado (t):
	for i in range(4):
		t.fd(100) 	
		t.lt(90)

	#t es la acción que va a tomar nuestro objeto definido anteriormente, 
	#avanza, gira *4

cuadrado (bob) 
	
	#bob es nuestra variable que tiene el metodo u objeto tortuga.	
	#t = bob.fd(100)

alice = turtle.Turtle()
cuadrado(alice)

	#así podemos llamar a otra.

'''
def cuadrado (t, longitud):
	for i in range (4):



'''


'''
DISEÑO DE INTERFAZ
Funciones que interactuen entre si.

Pseudocódigo funciones: 
	
	idea: desde la llamada dar valores.

	un cuadrado va bien con el cuadrado, pero para poligono necesito; 
	avanzar, girar (45 grados), avanzar, girar (90), avanzar y aqui repetir
	
	antes de hacer el bucle, por lo menos crear un poligono.

	así con los demás.

	*los ángulos se calculan desde la posición del objeto.

'''

'''
#poligono
for i in range (2):
	bob.rt(45)
	bob.fd(45)
	bob.rt(90)
	bob.fd(45)
	bob.rt(45)
	bob.fd(45)
'''

'''
#circulo: radio (p/2.pi), circunferencia (2.pi.r), APROX

	bob.fd()
	bob.rt()
'''

'''
def cuadrado (tortuga, longitud):
	for i in range(4):
		longitud = bob.fd()
		bob.lt(90)

cuadrado (bob, longitud(150)) #bob es nuestra variable que tiene el metodo u objeto tortuga.
'''

'''
def poligono (tortuga, longitud, n):
	for i in range(4):
		longitud = bob.fd(100) #avanza, gira *4
		grados = bob.lt(90)
		n = 360/grados


poligono (bob, longitud(50), ) #bob es nuestra variable que tiene el metodo u objeto tortuga.
'''

'''
def circulo (t, r):
	poligono ()

'''