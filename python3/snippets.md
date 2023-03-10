|| BASICOS
	
	Conceptos:

		Lenguajes de programación:

			Lenguajes de alto nivel:
			como Python diseñado para ser fácil de leer y escribir para la gente.

			Las computadoras sólo ejecutan programas escritos en lenguajes de bajo nivel. Los programas de alto nivel tienen que traducirse antes de ejecutarse.

			Son portables, lo que significa que pueden ejecutarse en tipos diferentes de computadores.

			Lenguaje de bajo nivel: 
			Diseñado para ser fácil	de ejecutar para un computador; también se lo llama “lenguaje de máquina” o “lenguaje ensamblador”.

			Sus programas sólo pueden ser ejecutarse en un tipo de computador y deben reescribirse para ejecutarlos en otro.

			Interpretes y compiladores:
			Programas que traducen lenguajes de alto nivel a lenguajes de bajo nivel.

			Un intérprete lee un programa de
			alto nivel y lo ejecuta, Traduce el programa poco a poco, leyendo y ejecutando cada comando.
	
				codigo fuente -> interprete -> salida

			Un compilador lee el programa y lo traduce todo al mismo tiempo, antes de
			ejecutar cualquiera de las instrucciones.
	
				codigo fuente -> compilador -> codigo objeto -> ejecutor -> salida

			Python es de alto nivel e interpretado.

		Programas:
		Son una secuencia de instrucciones que especifican cómo resolver un problema informático desde resolver operaciónes matemática, una función de buscar o hasta compilar un programa.

		Todos están compuestos por:

			Entrada:
			Recibir datos del teclado, o un archivo u otro aparato.

			Salida:
			Mostrar datos en el monitor o enviar datos a un archivo u otro aparato.

			Matemáticas:
			En las instrucciones se encuentran operaciones basicas como la adición, la multiplicación y más complejas.

			Operación condicional:
			Probar la veracidad de alguna condición y ejecutar una secuencia de instrucciones apropiada.

			Repetición:
			Ejecutar alguna acción repetidas veces, normalmente con alguna variación.

	Practica:
	# Si no mostras con print(), los cálculos, los valores de las varibles, etc; se van a ejecutar pero vas a ver el resultado del código en el interprete.

	# Error sintácto y de identación hace fallar todo el programa.

	#prompt

		def hola_mundo():
			print ("hola, mundo!")

		print ("he definido y he salido de la función")

		hola_mundo()

		print("he llamado a la función")
	
	#interprete		

		he definido y he salido de la función
		hola, mundo!
		he llamado a la función
		>>>


|| OPERACIONES MATEMÁTICAS

	ORDEN DE OPERACIONES:

	PEMDAS: 
	Paréntesis, exponenciación(**), multiplicación/división y adición y sustracción.

	Si hay igualdad signo/orden: 
	Se calcula de izquierda a derecha.


|| FUNCIONES MATEMÁTICAS

	Tenemos que importarlo con una sentencia import:
	>>> import math

	Crea un objeto de módulo llamado math.

		import math   #importar

		print (math)  #verificar
		<module 'math' (built-in)>


|| FUNCIONES
	
	Parámetro: 
	Es el nombre de la variable, se usa en la definición.
	
	Argumento:
	Es el valor para la variable/parametro, se usa en la llamada.
	
	Definición:	
		
		def sumarMismo (num): #parámetro/nom var
		print (num + num)

	Llamada:	
		
		sumarMismo(2)  #argum de func/valor/variable
		4              #valor retorno

	Variables y argumentos locales:
	Variable creada dentro de la función que solo puede usarse aquí.

		def catDoble(parte1, parte2):
			cat = parte1 + parte2
			imprimeDoble(cat)

		cantus1 = "Die Jesu domine, "
		cantus2 = "Dona eis requiem."
		
		catDoble(cantus1, cantus2)
		Jesu domine, Dona eis requiem. Die Jesu domine, Dona eis requiem.

		*cuando se termina de ejecutar, la VARIABLE SE DESTRUEYE.

			>>> print cat
			NameError: cat

	Variables globales como argumento:

		>>> latoya = ’Dafne, es mitad laurel mitad ninfa’
	
		>>> imprimeDoble(latoya)
		Dafne, es mitad laurel mitad ninfa. Dafne, es mitad laurel mitad ninfa.

	El nombre de la variable que pasamos como argumento -llamada- (latoya) no tiene nada que ver con el nombre del parámetro-definición- (paso). En imprimeDoble llamamos a todo el mundo paso.

	Asignar función a una variable:

		>>> nereida = type("32")
		>>> print nereida
		<type ’string’>

		>>> yanira = id(3)

		>>> yanira = 3
		>>> id(yanira)
		134882108
	
		>>> func1 = id(3)
		>>> id(func1)
		39199700

	Objeto de función:
	Es un valor que puedes asignar a una variable o pasarlo co-
	mo argumento.

	Return:





	Análisis sintácticos del interprete:

		Definición incompleta: el interprete mostrará puntos (...)

		Objeto función: se crea al definirla y tiene tipo function.

			print(imprimir_letra)
			function imprimir_letra at 0xb7e99e9c

			type(imprimir_letra)
			<class 'function'>

	Funciones productivas y nulas:

		Productivas:
		Devuelven un resultado, como las matemáticas; esperando usarlo en una variable o usarlo en una expresión.

		En modo terminal, math.sqrt(5) da 2.2360679774997898

		en modo script, el resultado se pierde: no almacena ni muestra el resultado,


		Nulas o void function:
		Realizan una acción pero no devuelven un valor, muestran algo en pantalla o tienen algún efecto.

		Si asignamos su resultado a una variable nos devuelve el valor none de tipo none.

		Ventajas de las funciones:

			Ponerle nombre a un grupo de sentencias, hace al programa más facil de leer y depurar

			Elimina el código repetitivo con solo llamar a la función creada en diferentes lugares.

			Dividir un programa largo en funciones te permite depurar las partes una a la vez y luego reunirlas en un todo funcional.

			Son útiles para muchos programas. Una vez que escribes y depuras una, la puedes reutilizar.







|| FLUJO DE EJECUCIÓN
	
	sentencias/def función > sentencias > llamada función (<< sentenc función) > sentencias.

	*leer flujo, no de inicio a fin.


|| DIAGRAMAS:

	Es un dibujo que informa sobre el valor y ubicación de las variables. A la izquierda va el nombre que junta a las variables globales, el nombre de la función y despues la llamada. En el recuadro (frame) van las variables. Sigue el flujo de ejecución.
	
	de Estado:
	Muestran el valor de cada variable

	de Pila (stack diagram):
	Muestran el valor y la función a la que pertenecen.

	Trackback / rastreo:
	Cuando hay un error en las funciones, puede mostrar un camino con una lista de funciones en el interprete, sigue el flujo de ejecución al igual que el stack de pila.

		*La ultima función que aparece es la que intentamos ejecutar.


|| COMBINACIONES

	CONVERSIÓN DE TIPOS:
	Es una función interna o nativa de python para convertir valores; llamamos al tipo y de damos un valor. Si no es posible da error.

		>>> int("32")
		32

		>>> int("Hola")
		ValueError: invalid literal for int(): Hola

		>>> int(3.99999)
		3    #redondea hacia abajo.

		>>> str(32)
		’32’

		>>> str(3.14149)
		’3.14149’

		La función float que convierte enteros y cadenas en números en coma flotante:

			>>> float(32)
			32.0

			>>> float("3.14159")   #cadena
			3.14159

		Python distingue entre el valor entero 1 y el valor
		de coma flotante 1.0.

		Ej: float()

		>>> minuto = 59
		>>> float(minuto) / 60.0
		0.983333333333

	COERCIÓN DE TIPOS:
	Son reglas de la conversión automática de tipos, si uno de
	los operandos matemáticos es tipo float, el otro se convierte automáticamente en float.

		>>> minuto = 59
		>>> minuto / 60.0
		0.983333333333

	Al usar un denomidador que es float, el otro se convierte en flotante y hace la operación sin enteros, sin redondear, etc.
	
	REGLAS DE COMPOSICIÓN:
	Los lenguajes de programación pueden tomar pequeños bloques de construcción y componerlos.

	Casi en cualquier lugar que puedes poner un valor, puedes poner una expresión arbitraria, con una excepción: el lado izquierdo de una sentencia de asignación tiene que ser un
	nombre de variable.

	Usar cualquier tipo de expresión como argumento en la llamada de una función o en sentencias, variables, etc.

		Cadenas:

			fruta = "plátano"
			bizcochoBueno = " pan de leche"
			print (fruta + bizcochoBueno)

			print('Chiste '*3)

			print ("Número de minutos desde la medianoche:",60+2)

		# calcula el porcentaje de la hora que ha pasado ya
		minuto = 60
		porcentaje = (minuto * 100) / 60.0

		El resultado queda asignado a x.

		x = math.cos(angulo + pi/2)

		x = math.exp(math.log(10.0))

		x = math.sin(grados / 360.0 * 2 * math.pi)

		x = math.exp(math.log(x+1))

		OPERAR ARGUMENTOS:

		def impr_2veces(bruce):
			print(bruce)
			print(bruce)

			>>> impr_2veces('Spam')
			Spam
			Spam

			>>> impr_2veces('Spam '*4)
			Spam Spam Spam Spam
			Spam Spam Spam Spam

		>>> imprimeDoble('Jamón'*4)
		JamónJamónJamónJamón JamónJamónJamónJamón
		
		>>> imprimeDoble(math.cos(math.pi))
		-1.0 -1.0


|| DEBUGGEAR
	
	Se trata de corregir los errores en los programas informaticos (bugs). La programación es un proceso de depuración hasta que el programa haga lo que querramos.

	Sintáctico:
	Error en la estructura y en las reglas del lenguaje de programación. Hace fallar todo el programa, al igual que el error de identación. No son permisivos.

	En tiempo de ejecución:
	No aparece hasta que se ejecuta el programa se llaman excepciones.

	Semánticos:
	Error de lógica en su programa, se ejecutará sin ningún mensaje de error, pero el resultado no será el deseado.
    Requiere trabajar al revés, observando el resultado del programa para averiguar lo que hace.

	Estudiar las claves para inducir los procesos y eventos llevaron a los resultados. Con una hipostesis correcta podemos predecir comportamientos para modificar el programa y llegar a un resultado correcto o esperado.

	Hay que leer el código, entender cada línea para corregir los errores.


|| DISEÑO DE INTERFAZ
	Diseñar funciones que interactúen entre sí.	

	Modelo turtle:
	Permite crear imágenes utilizando gráficas.

		import turtle
		bob = turtle.Turtle() 
		#Crea ventana con una flecha que representa a la tortuga.

	turtle vs Turtle:

		Modelo turtle:
		Proporciona una función llamada Turtle ('T'
		mayús) que crea un objeto Turtle, el cual asignamos a una variable, aquí es bob.

		Al imprimir bob se muestra algo como:

			<turtle.Turtle object at 0xb7bfbf4c>

		refiere a un objeto con tipo Turtle

	mainloop:
	Le dice a la ventana que espere a que el usuario haga algo.

	METODOS/ACCIONES
	Lo que realizará nuestro objeto tortuga llamada bob.

		LLamar a un metodo:
		Es similar a una función, sintaxis: objeto.fd(). El objeto puede estar en una variable, etc.

		método fd (forward):
		Está asociado con el objeto tortuga que llamamos bob. En la llamada le defimos que se mueva hacia adelante en (100) px, distancia asociada al tamaño real de la pantalla.

		bk (backward):
		Retroceder.

		lt (left turn) y lr (right turn):
		El argumento/valor es en grados (90 = 90°) gira sobre su eje hacia estos lados.

		pu (pen up) y pd (pen down):
		Sostiene una pluma, que está arriba o abajo; si la pluma está abajo, la tortuga deja un rastro cuando se mueve.

	DIBUJAR:
	Agregar varias líneas de código.

		ángulo recto:

			bob.fd(100)
			bob.lt(90)
			bob.fd(100)

			bob.fd(100)
			bob.bk(100)
			bob.lt(90)
			bob.fd(100)

		cuadrado:

			bob.fd(100)
			bob.bk(100)
			bob.lt(90)
			bob.fd(100)
			bob.rt(90)
			bob.fd(100)
			bob.rt(90)
			bob.fd(100)

	REPETICIÓN o BUCLES:
	Hacerlo de forma más concisa.

		for i in range(4):
		print('Hola!')

		Hola!
		Hola!
		Hola!
		Hola!

		for:
		Similar a una definición de función, el cuerpo con sangrías. El FLUJO DE EJECUCIÓN pasa por el cuerpo
		y luego vuelve hacia arriba. 

			En el ejemplo, pasa por el cuerpo cuatro veces: EJECUTA CUATRO VECES EL GRUPO DE SENTENCIAS.

				for i in range(4): #avanza y gira *4
					bob.fd(100)
					bob.lt(90)

	ENCAPSULAMIENTO:	
	Envolver un pedazo de código en una función. 

	El código definido apropiadamente sirve como documentación para pasar valores.
	Puede ser reutilizado tan solo llamando a la función dando otros valores, sin tener que escribir más código.

		def cuadrado (t):
			for i in range(4):
				t.fd(100) 	
				t.lt(90)

		#t variable, es la acción que va a tomar nuestro objeto definido anteriormente, avanza, gira *4

			>>>cuadrado (bob) 
		
		#bob valor, es nuestra variable que tiene el metodo u objeto tortuga.	
	
		#t = bob.fd(100)

		t se refiere a la misma tortuga bob , por lo que t.lt(90) tiene el mismo efecto que bob.lt(90). 

		¿por qué no llamar al parámetro bob ? 

		La idea es que t puede ser cualquier tortuga, no solo bob, así que podrías crear una segunda tortuga y pasarla como argumento a cuadrado

	GENERALIZACIÓN:
	Acto de agregar un parámetro a una función para pasarle valores en la llamada. 

	Hace que la función sea más general: sin tener que determinar los valores en el cuerpo de la definición.

		def cuadrado(t, longitud):
			for i in range(4):
				t.fd(longitud)
				t.lt(90)
		
		cuadrado(bob, 100)

		#agregar un parámetro longitud a cuadrado:
		#definimos la variable longitud en metodo fd.

		Dibujar polígonos regulares con cualquier número de lados:		
			def poligono(t, n, longitud):
				angulo = 360 / n
				
				for i in range(n): 
					t.fd(longitud)
					t.lt(angulo)
			
			poligono(bob, 7, 70)

			#n = lados = cant repeticion en la func, longitud y ángulos como valores en la llamada.

			#python 2: angulo = 360.0/n, así usa la conversión de typos.

		Argumentos de palabra clave:

		Incluir los nombres de los parámetros en la lista de argumentos: evitamos olvidar que son o cúal era su orden.
			
			poligono(bob, n=7, longitud=70)

			# o en la definicion de func:

			def poligono (tortuga/objeto, lados, longitud)

		

