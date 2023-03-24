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



'''
ENCAPSULAMIENTO:
		
	Envolver un pedazo de código en una función para que pueda reutilizarse.	
'''
'''
def cuadrado (t):
	for i in range(4):
		t.fd(100) 	
		t.lt(90)

	#t es la acción que va a tomar nuestro objeto (turtle/bob) definido anteriormente, 
	#avanza, gira *4

cuadrado (bob) 
'''	
	#bob es nuestra variable que tiene el metodo u objeto tortuga.	
	#t = bob.fd(100)
'''
alice = turtle.Turtle()
cuadrado(alice)
'''

	#así podemos llamar a otra.

'''

'''
'''
GENERALIZACIÓN:
	
	Acto de agregar un parámetro a una función para pasarle valores en la llamada.
	sin tener que determinar los valores en el cuerpo de la definición.
'''
'''
def cuadrado (t, longitud):
	for i in range (4):
		t.fd(longitud) 	
		t.lt(90)

cuadrado (bob, 230)
'''
'''
Hacer un poligono: 
requiere otra generalización.

Pista: los ángulos exteriores de un polígono regular con n lados son de 360/n grados.

'''
'''
def poligono (t, longitud, n):

	angulo = 360/n

	for i in range(n): 
		t.fd(longitud)
		t.lt(angulo)
			
poligono(bob, 40, 10)
'''

import math
'''
def circulo(t, r):
	perimetro = 2 * math.pi * r
	n = 50
	longitud = perimetro / n
	poligono(t, n, longitud)

circulo (bob, 10)
'''

'''
def arco(t, r, angulo):
	
	longitud_arco = 2 * math.pi * r * angulo / 360
	
	n = int(longitud_arco / 3) + 1
	
	longitud_paso = longitud_arco / n
	
	angulo_paso = angulo / n
	
	for i in range(n):
		t.fd(longitud_paso)
		t.lt(angulo_paso)

arco (bob, 5, 20)
'''

def polilinea(t, n, longitud, angulo):
	
	for i in range(n):
		t.fd(longitud)
		t.lt(angulo)

#reescribir poligono y arco para que utilice a polilinea
def poligono(t, n, longitud):
	
	angulo = 360.0 / n
	
	polilinea(t, n, longitud, angulo)


def arco(t, r, angulo):
	
	longitud_arco = 2 * math.pi * r * angulo / 360
	
	n = int(longitud_arco / 3) + 1
	
	longitud_paso = longitud_arco / n
	
	angulo_paso = float(angulo) / n
	
	polilinea(t, n, longitud_paso, angulo_paso)

#circulo para que utilice a arco :
def circulo(t, r):
	
	arco(t, r, 360)

''' llamadas:

polilinea(t, n, longitud, angulo)
poligono(t, n, longitud)
arco(t, r, angulo)
circulo(t, r)
'''
#polilinea(bob, 5, 40, 20)
#poligono(bob, 5, 60)
#arco(bob, 50, 90)
circulo(bob, 70)

'''
def poligono(tortuga, lados, longitud):
    # Crea una ventana de dibujo
    #ventana = turtle.Screen()

    # Crea una tortuga para dibujar
    #tortuga = turtle.Turtle()

    # Calcula el ángulo de giro según el número de lados
    angulo = 360 / lados

    # Dibuja el polígono
    for i in range(lados):
        tortuga.forward(longitud)
        tortuga.right(angulo)

    # Cierra la ventana de dibujo cuando el usuario hace clic en ella
    #ventana.exitonclick()

poligono (bob, 5, 45)
'''

'''
DISEÑO DE INTERFAZ
Funciones que interactuen entre si.

Pseudocódigo funciones: 
	
	idea: desde la llamada dar valores.

	 va bien con el cuadrado, pero para poligono necesito; 
	avanzar, girar (45 grados), avanzar, girar (90), avanzar y aqui repetir
	
	antes de hacer el bucle, por lo menos crear un poligono.

	así con los demás.

	*los ángulos se calculan desde la posición del objeto.

	#poligono
	for i in range (2):
	bob.rt(45)
	bob.fd(45)
	bob.rt(90)
	bob.fd(45)
	bob.rt(45)
	bob.fd(45)

	#circulo: radio (p/2.pi), circunferencia (2.pi.r), APROX

	bob.fd()
	bob.rt()
	
'''
