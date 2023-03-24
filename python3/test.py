import turtle

def dibujar_circulo_completo(radio, color="black"):
	
	#crean ventana de dibujo y una tortuga
    ventana = turtle.Screen() 
    tortuga = turtle.Turtle()

    # configuran la tortuga antes de dibujar el círculo. 
    """
	el color de la tortuga según el valor del argumento "color".

	movemos la tortuga a la posición inicial del círculo utilizando los métodos "penup" y "setposition".
    
	usamos el método "pendown" para comenzar a dibujar
    """
    tortuga.color(color)
    tortuga.penup()
    tortuga.setposition(0, -radio)
    tortuga.pendown()

    # método "circle" de la tortuga para dibujar un círculo completo con el radio especificado.
    tortuga.circle(radio, extent=360)

    # Cierra la ventana con un click.
    ventana.exitonclick()

dibujar_circulo_completo(150, "blue")
