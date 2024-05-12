# Thinking python

|| INTRODUCCIÓN
	
	Conceptos:

		Lenguajes de programación:

			Lenguajes de alto nivel:
				
				Como Python, diseñados para ser fácil de leer y escribir para la gente.

				Las computadoras sólo ejecutan programas escritos en lenguajes de bajo nivel. Los programas de alto nivel tienen que traducirse antes de ejecutarse.

				Son portables, lo que significa que pueden ejecutarse en tipos diferentes de computadores.


			Lenguaje de bajo nivel: 
				
				Diseñado para ser fácil	de ejecutar para un computador; también se lo llama “lenguaje de máquina” o “lenguaje ensamblador”.

				Sus programas sólo pueden ser ejecutarse en un tipo de computador y deben reescribirse para ejecutarlos en otro.

			
			Interpretes y compiladores:
				
				Programas que traducen lenguajes de alto nivel a lenguajes de bajo nivel.

				Un intérprete lee un programa de alto nivel y lo ejecuta, Traduce el programa poco a poco, leyendo y ejecutando cada comando.
	
					codigo fuente -> interprete -> salida

				Un compilador lee el programa y lo traduce todo al mismo tiempo, antes de ejecutar cualquiera de las instrucciones.
	
					codigo fuente -> compilador -> codigo objeto -> ejecutor -> salida

				Python es de alto nivel e interpretado.


		Programas:
			
			Son una secuencia de instrucciones que especifican cómo resolver un problema informático desde resolver operaciónes matemática, una función de buscar o hasta compilar un programa.

		
			Están compuestos por:

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

			print ("he llamado a la función")
	

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

		Es un valor que puedes asignar a una variable o pasarlo como argumento.

	
	Return:

		Valor-respuesta de una funcion que puede ser guardado en una variable.
		
		Cuando se ejecuta la sentencia return, la función se detiene inmediatamente.
		
		Si no definimos return, el valor de retorno es NONE; que se usa para representar casos donde no hay valor especifico asignado. No podríamos usar la respuesta de la llamada como variable porque no guarda valor.

			def sumar (x, y):							
				
				return x + y
				
			resultado = sumar (2, 2)
			4


	Análisis sintácticos del interprete:

		Definición incompleta: 

			el interprete mostrará puntos (...)

		Objeto función: 

			se crea al definirla y tiene tipo function.

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
		
		Son reglas de la conversión automática de tipos, si uno de los operandos matemáticos es tipo float, el otro se convierte automáticamente en float.

			>>> minuto = 59
			>>> minuto / 60.0
			0.983333333333

		Al usar un denomidador que es float, el otro se convierte en flotante y hace la operación sin enteros, sin redondear, etc.

	
	REGLAS DE COMPOSICIÓN:
		
		Los lenguajes de programación pueden tomar pequeños bloques de construcción y componerlos.

		Casi en cualquier lugar que puedes poner un valor, puedes poner una expresión arbitraria, con una excepción: el lado izquierdo de una sentencia de asignación tiene que ser un nombre de variable.

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
			
			Proporciona una función llamada Turtle ('T' mayús) que crea un objeto Turtle, el cual asignamos a una variable, aquí es bob.

		Al imprimir bob se muestra algo como:

			<turtle.Turtle object at 0xb7bfbf4c>

			refiere a un objeto con tipo Turtle


	mainloop:
		
		Le dice a la ventana que espere a que el usuario haga algo.


	METODOS/ACCIONES
		
		Lo que realizará nuestro objeto tortuga llamada bob.

		LLamar a un metodo:
			
			Es similar a una función, sintaxis: objeto.fd(). El objeto puede estar en una variable, etc.


		Método fd (forward):
			
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
			
			Similar a una definición de función, el cuerpo con sangrías. El FLUJO DE EJECUCIÓN pasa por el cuerpo y luego vuelve hacia arriba. 

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

		¿por qué no llamar al parámetro bob? 

		La idea es que t puede ser cualquier tortuga, no solo bob, así que podrías crear una segunda tortuga y pasarla como argumento a cuadrado.


	GENERALIZACIÓN:
		
		Acto de agregar un parámetro a una función para pasarle valores en la llamada. 

		Hace que la función sea más general: sin tener que determinar los valores en el cuerpo de la definición.

			def cuadrado (t, longitud):
				for i in range(4):
					t.fd(longitud)
					t.lt(90)
		
			cuadrado(bob, 100)

			agregar un parámetro longitud a cuadrado:
				definimos la variable longitud en metodo fd.

		
		Dibujar polígonos regulares con cualquier número de lados:	

			Tambien requiere una generalización:

			def poligono(t, n, longitud):
				angulo = 360.0 / n
				
				for i in range(n): 
					t.fd(longitud)
					t.lt(angulo)
			
			poligono(bob, 7, 70)

			n = lados = cant repeticion en la func, longitud y ángulos como valores en la llamada.

			python 2: angulo = 360.0/n, así usa la conversión de typos.
			

		Argumentos de palabra clave:

			Incluir los nombres de los parámetros en la lista de argumentos: evitamos olvidar que son o cúal era su orden.
			
				poligono(bob, n=7, longitud=70)

				# o en la definicion de func:

				def poligono (tortuga/objeto, lados, longitud)


	DISEÑO DE INTERFAZ:

		La interfaz de una función es un resumen de cómo esta se utiliza: 

			¿cuáles son los parámetros? 

			¿Qué hace la función? 

			¿Y cuál es el valor de retorno? 

		Una interfaz es “limpia” si permite a la sentencia llamadora hacer lo que quiere sin lidiar con detalles innecesarios.


		Circulo: 

			radio, r , como parámetro.

			calcula el perímetro de un círculo con radio r utilizando la fórmula 2πr.

			math.pi , tenemos que importar math.cos al comienzo del script. Es una buena practica.


	REFACTORIZACIÓN:

		Reorganizar un programa para mejorar las interfaces y facilitar la reutilización de código. 

		A veces no se cuenta con el tiempo para evitarlo y diseñar mejor el programa.

			Ej: notamos que había código similar
			en arco y poligono , así que “lo factorizamos” en polilinea .

			Si hubiéramos planificado con anticipación, podríamos haber escrito polilinea primero y haber evitado la refactorización.


|| PLAN DE DESARROLLO

	Es un proceso para escribir programas.

		Ej: “encapsulamiento y generalización”.

		1. Comenzar escribiendo un programa pequeño sin definiciones de función.

		2. Una vez que el programa funciona, identifica una parte coherente, encapsula la parte en una función y dale un nombre.

		3. Generaliza la función agregando parámetros apropiados.
	
		4. Repite los pasos 1–3 hasta que tengas un conjunto de funciones eficaces. Copia y pega código que funcione para evitar repetir (y volver a depurar).

		5. Busca oportunidades para mejorar el programa refactorizando. Por ejemplo, si tienes código similar en muchos lugares, considera factorizarlo dentro de una función
		general apropiada.


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

			llamadas:

				polilinea(t, n, longitud, angulo)
				poligono(t, n, longitud)
				arco(t, r, angulo)
				circulo(t, r)
			
				polilinea(bob, 5, 40, 20)
				poligono(bob, 5, 60)
				arco(bob, 50, 90)
				circulo(bob, 70)


			*Este proceso para producir código tiene algunos incovenientes, pero hay alternativas. 

			Pero sirve para dividir un programa en funciones mientras avanzas. 



	Docstring:

		Es una cadena al comienzo de una función que explica la interfaz

		def polilinea(t, n, longitud, angulo):
			"""
				Dibuja n segmentos de línea con la longitud dada
				y el ángulo (en grados) entre ellos. t es una tortuga.
			"""
			for i in range(n):
				t.fd(longitud)
				t.lt(angulo)

		Explica de manera concisa lo que hace la función, sin detalles (si no es obvio).


	Depuración:

		Una interfaz es como un contrato entre una función y la sentencia llamadora. La llamadora acepta proporcionar ciertos argumentos y la función acepta hacer cierto trabajo.

		Requisitos: 

			Precondiciones:

				Se supone que son verdaderos antes de que la función comience a ejecutarse.

				Son responsabilidad de la llamadora. Si la llamadora viola una precondición (¡debidamente documentada!) y la función no funciona de forma correcta, el error está en la llamadora, no en la función.

			Postcondiciones:

				Son las condiciones al final de la función. 

				Ej, incluyen el efecto previsto de la función (como al dibujar segmentos de línea) y cualquier efecto secundario (como mover la tortuga o hacer otros cambios).

		Si las precondiciones se satisfacen y las postcondiciones no, el error está en la función. Si tus pre y post condiciones están claras, pueden ayudar con la depuración.



	Condicionales y recursividad: 

		La sentencia if ejecuta código diferente dependiendo del estado del programa.


		División entera y módulo:

			Operador división entera (//): 

				Divide dos números y redondea a un entero hacia abajo.

				Ej. La duración de una película es 105 minutos. 

				Quizás quieres saber cuánto dura en horas

				>>> minutos = 105
				>>> minutos / 60
				1.75



|| Recursividad

	Es valido para una función llamar a otra función; es valido también para una función llamarse a sí misma.

	```python

	def cuenta_reg(n):
		if n <= 0:
			print('Despegue!')
		else:
			print(n)
			cuenta_reg(n-1)

	```

	Si 'n' es 0 o negativo, muestra la palabra, “¡Despegue!” De lo contrario, muestra a 'n' y luego llama a la función con nombre 'cuenta_reg' (a sí misma) pasando a 'n-1' como argumento.


	Si llamamos a 'cuenta_reg(3)':
		
		La ejecución de cuenta_reg comienza con n=3 , y dado que n es mayor que 0, muestra el valor 3 y se llama a sí misma...

		La ejecución de cuenta_reg comienza con n=2 , y dado que n es mayor que 0. muestra el valor 2 y se llama a sí misma...

		Y luego estás de regreso en __main__ . 

		Por lo tanto, la salida completa se ve así en el diagrama de pila:

			__main__
			
			cuenta_reg -> 3
			
			cuenta_reg -> 2
			
			cuenta_reg -> 1

			cuenta_reg -> 0

		3
		2
		1 
		¡Despegue!


	Como siempre, la parte de arriba de la pila es el marco para __main__ . 

	Está vacío porque no creamos variables en __main__ ni le pasamos argumentos.

	Los cuatro marcos de cuenta_reg tienen valores diferentes para el parámetro n. 

	La parte de abajo de la pila, donde n=0 , se llama caso base. 

	No hace una llamada recursiva, así que no hay más marcos.



|| Recursividad infinita
	
	Si una recursividad nunca llega a un caso base, sigue haciendo llamadas recursivas por siempre y el programa nunca termina. 

	Esto se conoce como recursividad infinita y en general no es una buena idea.	

	Python entrega un mensaje de error cuando la recursividad alcanza la profundidad máxima:

	```python

	def recursivo():
		recursivo()

	```

		File "<stdin>", line 2, in recursivo...

			...
			
		RuntimeError: Maximum recursion depth exceeded



|| Entrada de teclado
	
	Función incorporada llamada input que detiene el programa y espera a que el usuario escriba algo.

	Cuando el usuario presiona Return o Enter , el programa continúa e input devuelve como cadena lo que escribió el usuario.

	```python

	texto = input()

	```

	```python

	nombre = input('Cuál...es tu nombre?\n')

	```

	La secuencia '\n' al final del mensaje representa una nueva línea, la cual es un carácter especial que provoca un salto de línea.



|| Depuración

	Cuando ocurre un error de sintaxis o de tiempo de ejecución, el mensaje de error contiene mucha información, pero esto puede ser abrumador.

		Qué tipo de error fue. 

		Dónde ocurrió.


	Los errores de sintaxis son generalmente fáciles de encontrar, pero hay algunas trampas.

	Los errores de espacio en blanco pueden ser complicados porque los espacios y las sangrías son invisibles y estamos acostumbrados a ignorarlos.

	Un mensaje de error puede indicar la línea 5, pero no hay nada malo con esa línea. 

	Para encontrar el error real, podría ser útil imprimir el valor de relacion, que resulta ser 0.

	El problema está en la línea 4, que utiliza división entera en lugar de división de coma flotante.

	Deberías tomarte el tiempo de leer cuidadosamente los mensajes de error, pero no supongas que todo lo que dice es correcto.



|| Funciones productivas
	
	Muchas de las funciones de Python que hemos utilizado, tales como las funciones matemáticas, producen valores de retorno. 

	Sin embargo, las funciones que hemos escrito son todas nulas: 	

		Tienen un efecto, como imprimir un valor o mover una tortuga, pero no tienen un valor de retorno.

	
	Valores de retorno: 

		Al llamar a una función se genera un valor de retorno, que usualmente asignamos a una variable o utilizamos como parte de una expresión.

			e = math.exp(1.0)

			altura = radio * math.sin(radianes)

		Las funciones que hemos escrito hasta ahora son todas nulas. 

		No tienen valor de retorno; de manera más precisa, su valor de retorno es 'None'.


	funciones productivas: 

		El primer ejemplo es area, que devuelve el área de un círculo con un radio dado:
			
		```python	

		def area(radio):
		
			a = math.pi * radio**2
			return a

		```

		En una función productiva la sentencia 'return' incluye una expresión. 

		Esta sentencia significa: “Sal inmediatamente de esta función y utiliza la siguiente expresión como valor de retorno.” 

		La expresión puede ser arbitrariamente complicada, por lo que podríamos haber escrito esta función de manera más concisa:
	
		```python

		def area(radio):
			return math.pi * radio**2

		```

			Por otra parte, las variables temporales como a pueden hacer más fácil la depuración.


	Multiples return:

		A veces es útil tener múltiples sentencias return, una en cada rama de un condicional.

		```python

		def valor_absoluto(x):
			if x < 0:
			return -x
		else:
			return x

		```

		Están en un condicional alternativo, solo se ejecuta una.

		Tan pronto como se ejecute una sentencia return, la función termina sin ejecutar ninguna de las sentencias posteriores. 

		El código que aparece después de una sentencia return , o cualquier otro lugar que el flujo de ejecución nunca puede alcanzar, se llama 'código muerto'.

		En una función productiva, es una buena idea asegurarse de que cada camino posible a
		través del programa llegue a una sentencia return. 

		```python

		def valor_absoluto(x):
			if x < 0:
				return -x
			if x > 0:
				return x
		
		```

		Esta función es incorrecta porque si x es 0, ninguna condición es verdadera, y la función termina sin llegar a una sentencia return. 

		Si el flujo de ejecución llega al final de una
		función, el valor de retorno es None, lo cual no es el valor absoluto de 0.

		>>> print(valor_absoluto(0))
		None



|| Desarrollo Incremental

	A medida que vayas escribiendo funciones más grandes, podrías encontrarte pasando más tiempo depurando.

	Para lidiar con programas cada vez más complejos, tal vez quieras intentar un proceso llamado desarrollo incremental.

	El objetivo del desarrollo incremental es evitar largas sesiones de depuración agregando y probando solo un pedazo de código a la vez.


	1. El primer paso es considerar cómo debería ser una función.
		
		cuáles son las entradas (parámetros).

		cuál es la salida (valor de retorno).

		Confirmado que la función es sintácticamente correcta y podemos comenzar agregando código al cuerpo.


	2. Un siguiente paso razonable es encontrar las diferencias.

		Puede almacenar esos valores en variables temporales y las imprime.

		Sabremos que la función obtiene los argumentos correctos y realiza el primer cálculo de manera correcta. 

		Si no, solo hay que revisar unas pocas líneas.

		Tendrías que ejecutar el programa en este punto y verificar la salida.

		Si eso funciona de manera correcta, estás listo. De lo contrario, tal vez quieras imprimir el valor de resultado antes de la sentencia return.

		La versión final de la función no muestra nada cuando se ejecuta: solo devuelve un valor.

		Las sentencias print que escribimos son útiles para depurar, pero una vez que la función esté bien, deberías borrarlas. 

		Un código como ese se llama andamiaje (en inglés, scaffolding) porque es útil para construir el programa pero no es parte del producto final.


	3. Claves: 

		1. Comienza con un programa que funcione y haz pequeños cambios incrementales. 

		En cualquier punto, si hay un error, deberías tener una buena idea de dónde está.

		
		2. Utiliza variables que guarden valores intermedios de tal manera que puedas mostrarlos y verificarlos.

		
		3. Una vez que el programa funciona, tal vez quieras borrar algo del andamiaje o consolidar varias sentencias en una expresión compuesta, pero solo si no hace al programa difícil de leer.



	Composición: 

		Puedes llamar a una función desde dentro de otra.

		Por ejemplo, una función que tome dos puntos, el centro de un círculo y un punto de su perímetro, y calcule el área del círculo.


		Supongamos que el punto central se almacena en las variables 'xc' e 'yc' , y el punto del perímetro está en 
		'xp' e 'yp' . 


		1. El primer paso es encontrar el radio del círculo, que es la distiancia entre los dos puntos. 

		Acabamos de escribir una función, distancia , que hace eso:

		```python

		radio = distancia(xc, yc, xp, yp)

		```

		2. El siguiente paso es encontrar el área de un círculo con ese radio; también escribimos eso:

		```python

		resultado = area(radio)

		```


		3. Encapsulando estos pasos en una función, obtenemos:

		```python

		def area_circulo(xc, yc, xp, yp):
			radio = distancia(xc, yc, xp, yp)
			
			resultado = area(radio)
			
			return resultado

		```

		Las variables temporales radio y resultado son útiles para el desarrollo y la depuración, pero una vez que el programa funciona, podemos hacerlo más conciso componiendo las llamadas a funciones:

		```python

		def area_circulo(xc, yc, xp, yp):
			return area(distancia(xc, yc, xp, yp))

		```


|| Factorial


	3! = 3 * 2 * 1 

		= 6


	```python

	def factorial(n):
		if n == 0:
			return 1
		else:
			recur = factorial(n-1)
			resultado = n * recur
			return resultado

	```

	Dado que 3 no es 0, tomamos la segunda rama y calculamos el factorial de n-1 ...
	
	Dado que 2 no es 0, tomamos la segunda rama y calculamos el factorial de n-1 ...


	Diagrama de pila: 

		__main__

		factorial n-> 3  recur -> 2 resultado -> 6 -> main

		factorial n-> 2  recur -> 1 resultado -> 2 

		factorial n-> 1  recur -> 1 resultado -> 1 

		factorial n-> 0 


		Cuando es 6, vuelve a main. 



|| Leer flujo de ejecución 
	
	Seguir el flujo de ejecución es una manera de leer programas, pero puede volverse abrumador rápidamente. 

	Una alternativa es lo que yo llamo “salto de fe”. 

	Cuando llegas a una llamada a función, en lugar de seguir el flujo de ejecución, supones que la función es correcta y que devuelve el resultado correcto.

	Una vez que nos hemos convencido de que esta función es correcta —examinando el código y probándolo— podemos utilizar la función sin mirar el cuerpo otra vez.

	```python

	def fibonacci(n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			return fibonacci(n-1) + fibonacci(n-2)

	```

	Si intentas seguir el flujo de ejecución aquí, incluso para valores de n bastante pequeños, tu cabeza estalla. 

	Sin embargo, de acuerdo al salto de fe, si supones que las dos llamadas recursivas funcionan correctamente, entonces está claro que obtienes el resultado correcto al sumarlas.



|| Verificar Tipos


	factorial(1.5)
	
	RuntimeError: Maximum recursion depth exceeded


	Se ve como una recursividad infinita.

	La función tiene un caso base:
		
		cuando n == 0  

	Pero si 'n' no es un entero, podemos perder el caso base y seguir con la recursividad sin parar.


	En la primera llamada recursiva, el valor de n es 0.5. En la siguiente, es -0.5. Desde allí, se hace menor (más negativo), pero nunca será 0.

	Tenemos dos opciones. 

	Podemos intentar generalizar la función factorial para que funcione con números de coma flotante o podemos hacer que factorial verifique el tipo de
	sus argumentos. 

	La primera opción se llama la 'función gamma' y está un poco más allá del alcance de este libro. 

	Entonces iremos por la segunda.
	
	Podemos utilizar la función incorporada 'isinstance' para verificar el tipo del argumento.

	Mientras estemos en ello, podemos también asegurarnos de que el argumento sea positivo:

	```python

	def factorial(n):
		
		if not isinstance(n, int):
			
			print('El factorial solo está definido para enteros.')
			
			return None
		
		elif n < 0:
			
			print('El factorial no está definido para enteros negativos.')

			return None

		elif n == 0:	
			
			return 1
		
		else:
			
			return n * factorial(n-1)

	```

	El primer caso base se encarga de los no enteros; el segundo se encarga de los enteros negativos. 

	En ambos casos, el programa imprime un mensaje de error y devuelve 'None' para indicar que algo anduvo mal:



|| Depuración

	Separar un programa grande en funciones pequeñas crea puntos de control naturales para la depuración. 

	Si una función no está funcionando, hay tres posibilidades a considerar:
		
		Hay algo mal en los argumentos que obtiene la función: 

			se viola una precondición.

		
		Hay algo mal en la función:

			se viola una postcondición.

		
		Hay algo mal en el valor de retorno o la manera en que se utiliza.


	Para descartar la primera posibilidad, puedes agregar una sentencia print al comienzo de la función y mostrar los valores de los parámetros (y quizás sus tipos). 

	O bien puedes escribir código que verifique las precondiciones de manera explícita.

	Si los parámetros se ven bien, agrega una sentencia 'print' antes de cada sentencia 'return' y muestra el valor de retorno. 

	Si es posible, verifica el resultado a mano. 

	Considera llamar a la función con valores que faciliten la verificación del resultado.

	Considera llamar a la función con valores que faciliten la verificación del resultado.

	Si la función parece funcionar, mira la llamada a función para asegurarte de que el valor de retorno se esté utilizando correctamente (¡o si al menos se está utilizando!).

	Agregar sentencias print al comienzo y al final de una función puede ayudar a hacer más visible el flujo de ejecución. 


	Por ejemplo, aquí hay una versión de factorial con sentencias print:

	```
	def factorial(n):
		
		espacio = ' ' * (4 * n)
		
		print(espacio, 'factorial', n)
		
		if n == 0:			
			print(espacio, 'devolviendo 1')			
			return 1
		
		else:
			recursivo = factorial(n-1)
			
			resultado = n * recursivo
			
			print(espacio, 'devolviendo', resultado)
			
			return resultado

	```

	espacio es una cadena de caracteres de espacio que controla la sangría de la salida. 

	Este es el resultado de factorial(4) :
					factorial 4
				factorial 3
			factorial 2
		factorial 1
	factorial 0
	devolviendo 1
		devolviendo 1
			devolviendo 2
				devolviendo 6
					devolviendo 24


	Si estás confundido acerca del flujo de ejecución, este tipo de salidas puede ser útil. 

	Desarrollar andamiaje eficaz toma algo de tiempo, pero un poco de andamiaje puede ahorrar mucha depuración.




|| Iteración




||