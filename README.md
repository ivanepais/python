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
	
	Capacidad de ejecutar un bloque de sentencias de forma repetida.

	
	Reasignación:

		Es valido hacer más de una asignación a la misma variable.

		Debido a que Python utiliza
		el signo igual ( = ) para la asignación, es tentador interpretar una sentencia del tipo 'a = b' como una proposición matemática de igualdad, es decir, la afirmación de que a y b son iguales. 

		Sin embargo, esta interpretación es incorrecta.

		Primero, la igualdad es una relación simétrica y la asignación no lo es. 

		Por ejemplo, en matemáticas, si a = 7 entonces 7 = a. 

		Pero en Python, la sentencia a = 7 es legal y 7 = a no lo es.

		Además, en matemáticas, una proposición de igualdad es verdadera o falsa todo el tiempo.

		Si a = b ahora, entonces a siempre será igual a b. En Python, una sentencia de asignación puede igualar dos variables, pero no tienen que permanecer iguales:	

		```
		a = 5
		b = a
		a = 3

		```

		```
		b

		```
		>>> 3

		La reasignación de variables es a menudo útil, pero deberías utilizarla con precaución. 

		Si los valores de las variables cambian frecuentemente, puede hacer que el código sea difícil de leer y depurar.



	Actualizar variables:

		El nuevo valor de la variable depende del antiguo.

		```
		x = x + 1

		```

		Después de la asignación, significa “obten el valor actual de x , suma uno, y luego actualiza a x con el nuevo valor.”


		Si intentas actualizar una variable que no existe, obtienes un error, debido a que Python evalúa el lado derecho antes de asignar un valor a x :
		
			>>> x = x + 1
			
			NameError: name 'x' is not defined


		Antes de que puedas actualizar una variable, la tienes que inicializar, generalmente con
		una asignación simple:
			
			>>> x = 0
			
			>>> x = x + 1
		
		Actualizar una variable sumando 1 se llama incremento; restar 1 se llama decremento.


	while:

		Los computadores a menudo se utilizan para automatizar tareas repetitivas. 

		Repetir tareas idénticas o similares sin cometer errores es algo que los computadores hacen bien y las personas hacen mal. 

		En un programa de computador, la repetición también se llama 'iteración'.

		```python

		def cuenta_reg(n):
			while n > 0:
				print(n)
				n = n - 1
			print('Despegue!')

		```

		Casi puedes leer la sentencia while como si fuera inglés. 

		Significa, “Mientras n sea mayor que 0, muestra el valor de n y luego decrementa n . 

		Cuando llegues a 0, muestra la palabra !Despegue!”.


		Flujo de ejecución de while:

			1. Determinar si la condición es verdadera o falsa.

			2. Si es falsa, salir de la sentencia while y continuar con la ejecución de la siguiente sentencia.

			3. Si la condición es verdadera, ejecutar el cuerpo y luego volver al paso 1.


		El cuerpo del bucle debería cambiar el valor de una o más variables de modo que la condición se vuelva falsa eventualmente y el bucle termine. 

		De lo contrario, el bucle se repetirá por siempre, lo cual se llama bucle infinito.

		Podemos probar que el bucle termina: 

			si n es cero o negativo, el bucle nunca se ejecuta. 

		De lo contrario, n se hace más pequeño cada vez que se pasa por el bucle, por lo que eventualmente tenemos que llegar a 0.


	break:	

		A veces no sabes que es momento de terminar un bucle hasta que llegas a la mitad del cuerpo. 

		En ese caso puedes utilizar la sentencia break para saltar hacia afuera del bucle.

		Ej. Tomar la entrada del usuario hasta que se escriba listo.

		```python

		while True: 

			linea = input('> ')
			if linea == 'listo':
				break
			print(linea)
		print('1⁄2Listo!')

		```

		La condición del bucle es 'True', lo cual siempre es verdadero, así que el bucle se ejecuta hasta que llega a la sentencia break.

		En cada paso, solicita la entrada del usuario con un paréntesis angular. 

		Si el usuario escribe listo, la sentencia break hace que se salga del bucle.


	Raíces cuadradas:	

		Los bucles se utilizan a menudo en programas que calculan resultados numéricos iniciando con una respuesta aproximada y mejorándola iterativamente.


		Ej. Calcular raíces cuadradas es el método de Newton.

		Saber la raíz cuadrada de a.

		Si comienzas con casi cualquier estimación, x, puedes calcular una mejor estimación con la siguiente fórmula:

			y = x+a/x /2


		Cuando y == x, podemos parar. 

		Aquí hay un bucle que comienza con una estimación inicial, x, y la mejora hasta que deja de cambiar:

		```python

		while True:
			print(x)
			y = (x + a/x) / 2
			if y == x:
				break
			x = y

		```


		Para la mayoría de los valores de a esto funciona bien, pero en general es peligroso probar la igualdad de números 'float'. 

		Los valores de coma flotante son solo aproximadamente correctos: 

			la mayoría de los números racionales, como 1/3, y los números irracionales, como √2, no se pueden representar de manera exacta con un float.

		En lugar de verificar si x e y son exactamente iguales, es más seguro utilizar la función abs para calcular el valor absoluto, o magnitud, de la diferencia entre estos:

		```python

		if abs(y-x) < epsilon:
			break

		```

		Tiene un valor como 0.0000001 que determina qué tan cerca es lo suficientemente cerca.


	Algoritmos: 	

		El método de Newton es un ejemplo de algoritmo: 

			es un proceso mecánico para resolver una categoría de problemas (en este caso, calcular raíces cuadradas).		


		Para encontrar el producto de n y 9, puedes escribir n − 1 como el primer dígito y 10 − n como elsegundo dígito. 

		Este truco es una solución general para multiplicar cualquier número de un solo dígito por 9. 

		¡Eso es un algoritmo! Del mismo modo, las técnicas que aprendiste para la suma con reserva, resta con préstamo y división larga son todas algoritmos. 

		Una de las características de los algoritmos es que no requieren ninguna inteligencia para realizarlos. 

		Son procesos mecánicos donde cada paso sigue al último de acuerdo a un conjunto simple de reglas.


|| Depuración

	A medida que comiences a escribir programas más grandes, podrías encontrarte ocupando más tiempo en la depuración. 

	Más código significa más posibilidades de cometer un error y más lugares para esconder errores de programación.

	Una manera de acortar tu tiempo de depuración es la “depuración por bisección”. 

	Por ejemplo, si hay 100 líneas en tu programa y las revisas una a la vez, tomaría 100 pasos.

	En cambio, intenta separar el problema por la mitad.

	Mira la mitad del programa, o cerca de esta, para un valor intermedio que puedas verificar.

	Agrega una sentencia print (o algo más que tenga un efecto verificable) y ejecuta el programa.

	Si la verificación en el punto medio es incorrecta, debe haber un problema en la primera mitad del programa. 

	Si es correcta, el problema está en la segunda mitad.

	Cada vez que hagas una verificación como esta, reduces a la mitad el número de líneas que tienes que buscar. 

	Después de seis pasos (lo cual es menos que 100), estarías revisando una o dos líneas de código, al menos en teoría.

	No tiene sentido contar líneas y encontrar el punto medio exacto. 

	En cambio, piensa en lugares del programa donde podría haber errores y lugares donde es fácil poner una verificación. 

	Luego, escoge un sitio donde creas que las posibilidades de que el error esté antes o después de la verificación son casi las mismas.



|| Strings

	
	Las cadenas no son como los enteros, los números de coma flotante y los booleanos. 

	Una cadena es una secuencia, lo cual significa que es una colección ordenada de valores.


	Secuencia: 	

		Una cadena es una secuencia de caracteres. 

		Puedes acceder a los caracteres uno a la vez con el operador de corchetes:

		```python

		fruta = 'banana'
		letra = fruta[1]
		letra

		```
		>>>'a'

		Seleccionamos el carácter número 1 de fruta y lo asigna a letra.

		La expresión en los corchetes se llama 'índice'. El índice indica cuál carácter en la secuencia quieres.

		El índice es un desplazamiento desde el comienzo de la cadena, y el desplazamiento de la primera letra es 'cero'.

		```
		letra = fruta[0]
		letra

		```
		>>>'b'

		b es la 0-ésima letra (“cero-ésima”) de 'banana', a es la 1-ésima letra (“unoésima”) y n es la 2-ésima letra (“dos-ésima”).


		Como índice, puedes utilizar una expresión que contenga variables y operadores:
			
		```
		i = 1
		fruta[i]

		```
		>>>'a'


		```
		fruta[i+1]

		```
		>>>'n'


		El valor del índice tiene que ser un entero. 

		De lo contrario, obtienes:
		
		```
		letra = fruta[1.5]

		```
		
		>>>TypeError: string indices must be integers


	len: 	

		Función incorporada que devuelve el número de caracteres en una cadena:

		```
		fruta = 'banana'
		len(fruta)

		```
		>>>6


		Operaciones y error de max indice: 

			Obtener la última letra de una cadena, quizás te tientes a intentar algo así:

			```python

			longitud = len(fruta)
			ultima = fruta[longitud]

			```

			>>>IndexError: string index out of range


			El motivo del IndexError es que no hay letra en 'banana' con el índice 6. 

			Dado que comenzamos a contar desde cero, las seis letras se enumeran del 0 al 5. 

			Para obtener el último
			carácter, tienes que restar 1 a longitud:

			```
			ultima = fruta[longitud-1]
			ultima

			```
			>>>'a'


			O bien puedes utilizar índices negativos, que cuentan hacia atrás desde el final de la cadena. 

			La expresión fruta[-1] entrega la última letra, fruta[-2] entrega la penúltima, y así
			sucesivamente.


	Recorrido bucle for:

		Muchas operaciones computacionales implican procesar una cadena trabajando un carácter a la vez. 

		Generalmente parten al comienzo, seleccionan cada carácter en turno, le hacen algo, y continúan hasta el final. 

		Este patrón de procesamiento se llama recorrido.

		```python

		indice = 0
		while indice < len(fruta):
			letra = fruta[indice]
			print(letra)
			indice = indice + 1

		``` 

		Este bucle recorre la cadena y muestra cada letra en una línea. 

		La 'condición' del bucle es indice < len(fruta), entonces cuando indice es igual a la longitud de la cadena, la condición es 'falsa' y el cuerpo del bucle no se ejecuta. 

		El último carácter accedido es el que tiene índice len(fruta)-1 , que es el último carácter en la cadena.

	
		Bucle for: 

			```python

			for letra in fruta:	
				print(letra)

			```		

			En cada paso por el bucle, el siguiente carácter en la cadena se asigna a la variable letra.

			El bucle continúa hasta que no queden caracteres.


	Segmento de cadena: 

		Una parte de una cadena 'slice'.

		```
		s = 'Monty Python'
		s[0:5]
		>>>'Monty'
		s[6:12]
		>>>'Python'

		```

		Devuelve desde 0 al 5 y desde 6 al 12. 

		El operador [n:m] devuelve la parte de la cadena desde el “n-ésimo” carácter al “m-ésimo” carácter, incluyendo el primero pero excluyendo el último. 

		Este comportamiento es contraintuitivo, pero tal vez ayude imaginar los índices apuntando entre los caracteres.

			fruta -> ' b a n a n a '
			indice    0 1 2 3 4 5 6 


		1. Si omites el primer índice (antes del signo de dos puntos), el trozo comienza al principio de la cadena.

		2. Si omites el segundo índice, el trozo llega hasta el final de la cadena:

		```
		fruta = 'banana'
		fruta[:3]
		'ban'
		fruta[3:]
		>>>'ana'

		```

		Si el primer índice es mayor o igual al segundo, el resultado es una cadena vacía, representada por dos comillas:

		```
		fruta = 'banana'
		fruta[3:3]
		>>>''

		```

		Una cadena vacía no contiene caracteres y tiene longitud 0, pero aparte de eso, es lo mismo que cualquier otra cadena.


	Cadenas inmutables: 

		Intentar utilizar el operador [] en el lado izquierdo de una asignación, con la intención de cambiar un carácter en una cadena.

		```
		saludo = 'Hola, mundo'
		saludo[0] = 'J'

		```
		TypeError: 'str' object does not support item assignment


		El “objeto” en este caso es la cadena y el “ítem” es el carácter que intentaste asignar. 

		Por ahora, un objeto es lo mismo que un valor.

		La razón del error es que las cadenas son inmutables, lo cual significa que no puedes cambiar una cadena que ya existe. 

		Lo mejor que puedes hacer es crear una nueva cadena que sea una variación de la original:

		```
		saludo = 'Hola, mundo'
		nuevo_saludo = 'J' + saludo[1:]
		
		nuevo_saludo
		>>>'Jola, mundo'

		```
		
		Concatena una nueva primera letra con un trozo de saludo. 

		No tiene efecto en la cadena original.


	Buscar: 	

		```

		def encontrar(palabra, letra):
			indice = 0
			while indice < len(palabra):
				if palabra[indice] == letra:
					return indice
				indice = indice + 1
			return -1

		```

		Encontrar es la inversa del operador []. 

		En lugar de tomar un índice y extraer el carácter correspondiente, toma un carácter y encuentra el índice donde aparece ese carácter. 

		Si el carácter no se encuentra, la función devuelve -1.

		Este es el primer ejemplo que hemos visto de una sentencia return dentro de un bucle. 

		Si palabra[indice] == letra, la función se sale del bucle y devuelve inmediatamente. 

		Si el carácter no aparece en la cadena, el programa termina el bucle de manera normal y devuelve -1.

		Este patrón de computación —recorrer una secuencia y devolver cuando encontramos lo que buscamos— se llama búsqueda.


	Bucles y conteo: 

		contar el número de veces que aparece la letra 'a' en una cadena:

		```python

		palabra = 'banana'
		contar = 0
		for letra in palabra:
			if letra == 'a':
				contar = contar + 1
			print(contar)

		```

		Patrón llamado contador. 

		La variable contar se inicializa en 0 y luego se incrementa cada vez que se encuentra una a. 

		Cuando el bucle termina, contar contiene el resultado: 

			el número total de letras a .


	Métodos de cadena: 	

		Similares a una función —toma argumentos y devuelve un valor—.


		upper(): 

			Toma una cadena y devuelve una nueva cadena con todas las letras mayúsculas.

			En lugar de la sintaxis de función upper(palabra), utiliza la sintaxis de método palabra.upper().

			```
			palabra = 'banana'
			nueva_palabra = palabra.upper()
			nueva_palabra
			>>>'BANANA'

			```

			Los paréntesis vacíos indican que este método no toma argumentos.

			Se llama invocación; en este caso, diríamos que estamos invocando a upper en palabra.


		find(): 

			Similar a la función encontrar.

			```
			palabra = 'banana'
			indice = palabra.find('a')
			indice

			>>>1

			```

			Invocamos a find en palabra y pasamos la letra que buscamos como parámetro.

			puede encontrar subcadenas, no solo caracteres:

			```
			palabra.find('na')
			>>> 2

			```

			Por defecto, find comienza al principio de la cadena, pero puede tomar un segundo argumento, el índice donde debería comenzar:

			```
			palabra.find('na', 3)
			>>> 4

			```


			Argumento opcional; find puede tomar también un tercer argumento, el índice donde debería detenerse:

			```
			nombre = 'bob'
			nombre.find('b', 1, 2)
			>>>-1

			```

			b no aparece en el rango de índices desde 1 hasta 2 , sin incluir el 2.

			Buscar hasta el segundo índice, sin incluirlo, hace a find consistente con el operador de trozo.


	In: 

		Operador booleano que toma dos cadenas y devuelve 'True' si la primera aparece como una subcadena en la segunda:

		```
		'a' in 'banana'
		>>>True
		'semilla' in 'banana'
		>>>False

		```

		Imprime todas las letras de palabra1 que también aparecen en palabra2:

		```
		def en_ambas(palabra1, palabra2):
			for letra in palabra1:
				if letra in palabra2:
					print(letra)

		```

		“para (cada) letra en (la primera) palabra, si (la) letra (aparece) en (la segunda) palabra, imprimir (la) letra.”

		Esto es lo que obtienes si comparas uvas y tunas:
			
			>>> en_ambas('uvas', 'tunas')
				u
				a
				s


	Comparación: 

		Operadores relacionales funcionan en las cadenas. Para ver si dos cadenas son iguales:

		```
		if palabra == 'banana':
			print('Todo bien, bananas.')
		
		```

		Operaciones relacionales son útiles para poner palabras en orden alfabético:

		```
		if palabra < 'banana':
			print('Tu palabra, ' + palabra + ', viene antes de banana.')

		elif palabra > 'banana':
			print('Tu palabra, ' + palabra + ', viene después de banana.')

		else:
			print('Todo bien, bananas.')

		```

		Python no maneja letras mayúsculas y minúsculas de la misma manera en que lo hacen las personas. 

		Todas las letras mayúsculas vienen antes de todas las letras minúsculas, entonces:
			
			Tu palabra, Piña, viene antes de banana.

		Una manera común de abordar este problema es convertir las cadenas a un formato estándar, por ejemplo todas minúsculas, antes de realizar la comparación. 

		Ten eso en mente en caso de que tengas que defenderte de un hombre armado con una Piña.



|| Depuración

	Cuando utilizas índices para recorrer los valores en una secuencia, es difícil obtener el comienzo y final de un recorrido de manera correcta. 

	Aquí hay una función que se supone que compara dos palabras y devuelve 'True' si una de las palabras es el inverso de la otra, pero contiene dos errores:

	```python

	def es_inverso(palabra1, palabra2):
		if len(palabra1) != len(palabra2):
			return False
		i = 0
		j = len(palabra2)
		while j > 0:
			if palabra1[i] != palabra2[j]:
				return False
			i = i+1
			j = j-1
		return True

	```

	La primera sentencia if verifica si las palabras tienen la misma longitud. 

	Si no, podemos devolver False inmediatamente. 

	De lo contrario, para el resto de la función, podemos suponer que las palabras tienen la misma longitud. 

	Este es un ejemplo del patrón guardián.


	i y j son índices: 

		i recorre a palabra1 hacia adelante mientras j recorre a palabra2 hacia atrás. 

	Si encontramos dos letras que no coinciden, podemos devolver False inmediatamente. 

	Si terminamos todo el bucle y todas las letras coinciden, devolvemos True.

	Si probamos esta función con las palabras “pots” y “stop”, esperamos el valor de retorno True , pero obtenemos un IndexError:

		es_inverso('pots', 'stop')
		...

		File "inverso.py", line 15, in es_inverso
		if palabra1[i] != palabra2[j]:
		
		IndexError: string index out of range


	Para depurar este tipo de error, mi primer movimiento es imprimir los valores de los índices inmediatamente antes de la línea donde aparece el error.

	```python

	while j > 0:
		print(i, j)	# imprimir aquí
		
		if palabra1[i] != palabra2[j]:
			return False
		i = i+1
		j = j-1

	```

	Ahora cuando ejecuto el programa de nuevo, obtengo más información:

		>>> es_inverso('pots', 'stop')
		0 4
		...
		IndexError: string index out of range

	En el primer paso por el bucle, el valor de j es 4, lo cual está fuera de rango para la cadena 'pots'. 

	El índice del último carácter es 3, por lo que el valor inicial para j debería ser len(palabra2)-1.

	Si arreglo este error y ejecuto el programa de nuevo, obtengo:
		
		>>> es_inverso('pots', 'stop')
		0 3
		1 2
		2 1
		True

	Esta vez obtenemos la respuesta correcta, pero se ve como si el bucle solo se ejecutara tres veces, lo cual es sospechoso. 

	Para obtener una mejor idea de lo que está ocurriendo, es útil dibujar un diagrama de estado.

	Durante la primera iteración:

		palabra1 -> 'pots' 	palabra2 -> 'stop'

		'pots' 	'stop'
		i->0 	j->3



|| Juego de palabras

	Involucra resolver puzles de palabras buscando palabras que tengan ciertas propiedades. 

	Por ejemplo, encontrar los palíndromos más largos en inglés y buscaremos palabras cuyas letras aparezcan en orden alfabético. 

	Además, se mostrará otro plan de desarrollo de programa:

		Reducción a un problema previamente resuelto.


	Leer lista de palabras: 

		La más adecuada para nuestro propósito es una de las listas de palabras recopiladas y contribuidas al dominio público por Grady Ward como parte del proyecto léxico Moby.

		Lista de 113,809 palabras de crucigrama oficiales, es decir, palabras que se consideran válidas en crucigramas y otros juegos de palabras.

		El archivo está en texto plano, así que puedes abrirlo con un editor de texto, pero también puedes leerlo desde Python. 

		La función incorporada 'open' toma el nombre del archivo como parámetro y devuelve un objeto de archivo que puedes utilizar para leer dicho archivo.

		```python

		fin = open('words.txt')

		```

		'fin' es un nombre común para un objeto de archivo utilizado para la entrada ('file input'). 

		El objeto de archivo proporciona varios métodos para la lectura, incluyendo 'readline', que lee caracteres desde un archivo hasta que llega a una nueva línea y devuelve el resultado como una cadena:

		```python

		fin.readline()

		```
		'aa\n'

		La primera palabra de esta particular lista es “aa”, que es un tipo de lava. 

		La secuencia '\n' representa el carácter nueva línea que separa esta palabra de la siguiente.


		El objeto de archivo hace un seguimiento del lugar del archivo en donde este se encuentra en un instante determinado, así que si llamas a 'readline' de nuevo, obtienes la palabra siguiente:

		```
		fin.readline()

		```
		'aah\n'

		La palabra siguiente es “aah”,


		Si el caracter de nueva línea molesta, podemos quitarlo con el método de cadena strip:

		```
		linea = fin.readline()
		palabra = linea.strip()
		palabra

		```
		'aahed'


		También podemos utilizar un objeto de archivo como parte de un bucle for. 

		Este programa lee 'words.txt' e imprime cada palabra, una por línea:

		```python

		fin = open('words.txt')
		for linea in fin:
			palabra = linea.strip()
			print(palabra)

		```


	Patrones de búsqueda:

		```python

		def no_tiene_e(palabra):
			for letra in palabra:
				if letra == 'e':
					return False
			return True

		```

		for recorre los caracteres en 'palabra'. 

		Si encontramos la letra “e”, podemos devolver 'False' inmediatamente; de lo contrario, tenemos que ir a la siguiente 'letra.''

		Si terminamos el bucle de manera normal, significa que no encontramos una “e”, por lo cual devolvemos True.


		'excluye' es una versión más general de 'no_tiene_e':

		```python

		def excluye(palabra, prohibidas):
			for letra in palabra:
				if letra in prohibidas:
					return False
			return True

		```

		Podemos devolver 'False' apenas encontremos una 'letra' prohibida; si llegamos al final del bucle, devolvemos 'True'.


		'usa_solo' es similar, excepto que el sentido de la condición es inverso:

		```python

		def usa_solo(palabra, disponibles):
			for letra in palabra:
				if letra not in disponibles:
					return False
			return True

		```

		En lugar de recorrer las letras en 'palabra', el bucle recorre las letras requeridas. 

		Si alguna de las letras requeridas no aparece en la palabra, podemos devolver 'False'.


		'usa_todas' era una instancia de un problema previamente resuelto, y habrías escrito:

		```python

		def usa_todas(palabra, requeridas):
			return usa_solo(requeridas, palabra)

		```

		Es un ejemplo de un plan de desarrollo de programa llamado 'reducción a un problema previamente resuelto', lo cual significa que reconoces el problema en el que estás trabajando como una instancia de un problema resuelto y aplicas una solución existente.


	Bucles con índices:

		Usamos los bucles for porque solo necesitaba los caracteres en las cadenas; no tenía que hacer nada con los índices.

		Para 'es_abecedario' tenemos que comparar letras adyacentes, lo cual es un poco difícil con un bucle for:

		```python

		def es_abecedario(palabra):
			anterior = palabra[0]
			for c in palabra:
				if c < anterior:
					return False
				anterior = c
			return True

		```

		
		Una alternativa es usar recursividad:

		```python

		def es_abecedario(palabra):
			if len(palabra) <= 1:
				return True
			if palabra[0] > palabra[1]:
				return False
			return es_abecedario(palabra[1:])


		Otra opción es usar un bucle while:

		```python

			def es_abecedario(palabra):
				i = 0
				while i < len(palabra)-1:
					if palabra[i+1] < palabra[i]:
						return False
					i = i+1
				return True

		```

		Este bucle comienza con i=0 y termina cuando i=len(palabra)-1. 

		En cada paso por el bucle, compara al i-ésimo carácter (que puedes pensarlo como el carácter actual) con el i + 1-ésimo carácter (que puedes pensarlo como el siguiente).

		Si el siguiente carácter es menor (alfabéticamente anterior) que el actual, entonces hemos descubierto que se rompe la tendencia abecedaria y devolvemos False.

		Si llegamos al final del bucle sin encontrar una falla, entonces la palabra pasa la prueba.

		Para convencerte de que el bucle termina de manera correcta,

		Ej. 'flossy', la longitud de la palabra es 6, por lo cual la última vez que el bucle se ejecuta es cuando i es 4, que es el índice del penúltimo carácter. 

		En la última iteración, compara el penúltimo carácter con el último, que es lo que queremos.


		Versión de 'es_palindromo' que utiliza dos índices: uno comienza al principio y aumenta, el otro comienza al final y disminuye.

		```python

		def es_palindromo(palabra):
			i = 0
			j = len(palabra)-1
			while i<j:
				if palabra[i] != palabra[j]:
					return False
			i = i+1
			j = j-1
			return True

		```

		O bien podríamos reducir a un problema previamente resuelto y escribir:

		```python

		def es_palindromo(palabra):
			return es_inverso(palabra, palabra)

		```


|| Depuración

	Probar programas es difícil.

	Escoger un conjunto de palabras que pruebe todos los errores posibles está en algún lugar entre difícil e imposible.

	Hay dos casos obvios para verificar: las palabras que tienen una ‘e’ deberían devolver False y las palabras que no la tienen deberían devolver True.

	Dentro de cada caso, hay algunos subcasos menos obvios. 

	Entre las palabras que tienen una “e”, deberías probar palabras con una “e” al principio, al final y en algún lugar del medio. 

	Deberías probar palabras largas, palabras cortas y palabras muy cortas, como la cadena vacía. 

	La cadena vacía es un ejemplo de un 'caso especial', que es uno de los casos no obvios donde los errores a menudo acechan.

	Además de los casos de prueba que generes, puedes también probar tu programa con una lista de palabras como words.txt. 

	Escudriñando la salida, podrías ser capaz de captar los errores, pero ten cuidado: podrías captar un tipo de error (palabras que no deberían estar incluidas, pero lo están) y otro no (palabras que deberían estar incluidas, pero no lo están).

	En general, las pruebas pueden ayudarte a encontrar errores, pero no es fácil generar un buen conjunto de casos de prueba, e incluso si lo haces, no puedes asegurarte de que tu programa está correcto.

		— Edsger W. Dijkstra

		Se pueden probar programas para mostrar la presencia de errores, ¡pero nunca
		para mostrar su ausencia!



|| Listas

	Es un tipo de dato.  

	Una lista es una secuencia de valores.

	En una cadena, los valores son caracteres; en una lista, pueden ser de cualquier tipo. 

	Los valores en una lista se llaman elementos o a veces ítems.


	Hay varias maneras de crear una lista nueva; la más simple es encerrar los elementos en corchetes ( [ y ] ):
		
		[10, 20, 30, 40]

		['crunchy frog', 'ram bladder', 'lark vomit']


	El primer ejemplo es una lista de cuatro enteros. 

	El segundo es una lista de tres cadenas.

	Los elementos de una lista no tienen que ser del mismo tipo.

	La siguiente lista contiene una cadena, un número de coma flotante, un entero y (¡atención!) otra lista:
		
		['spam', 2.0, 5, [10, 20]]


	Una lista dentro de otra lista está anidada.
	
	Una lista que no contiene elementos se llama lista vacía; puedes crear una con corchetes vacíos, [].


	Puedes asignar valores de lista a variables:

		```python
		
		quesos = ['Cheddar', 'Edam', 'Gouda']
		
		numeros = [42, 123]
	
		vacio = []

		print(quesos, numeros, vacio)

		```

		['Cheddar', 'Edam', 'Gouda'] [42, 123] []


	Las listas son mutables: 
		
		Para acceder a los elementos de una lista es la misma que para acceder a los caracteres de una cadena: el operador de corchetes. 

		La expresión dentro de los corchetes especifica el índice. 

		Los índices comienzan en 0:	

		```
		quesos[0]

		```	
		'Cheddar'


		A diferencia de las cadenas, las listas son mutables.

		Cuando el operador de corchetes aparece en el lado izquierdo de una asignación, este identifica el elemento de la lista que será asignado.

		```
		numeros = [42, 123]
		numeros[1] = 5
		numeros

		```	
		[42, 5]


	Diagrama de estado: 

		quesos -> list
					0 -> 'Cheddar'
					1 -> 'Edam'
					2 -> 'Gouda'

		numeros -> list 
					0 -> 42
					1 -x- 123
					1 -> 5

		vacio -> list



		El uno-ésimo elemento de 'numeros' , que solía ser 123, ahora es 5.


		Las listas se representan por cajas con la palabra “list” por fuera y los elementos de la lista por dentro.

 		'quesos' se refiere a una lista con tres elementos con índices 0, 1 y 2. 

 		'numeros' contiene dos elementos; el diagrama muestra que el valor del segundo elemento ha sido
		reasignado de 123 a 5. 

		'vacio' se refiere a una lista sin elementos.

		Los índices de las listas funcionan de la misma manera que los índices de las cadenas:
			
			Cualquier expresión entera se puede utilizar como índice.

			Si intentas leer o escribir un elemento que no existe, obtienes un 'IndexError'.

			Si un índice tiene un valor negativo, se cuenta hacia atrás desde el final de la lista.


		El operador 'in' también funciona en las listas.

			```python

			quesos = ['Cheddar', 'Edam', 'Gouda']
		
			'Edam' in quesos
				
			'Brie' in quesos
			
			```
			True
			False


	Recorrer una lista:

		Usando un ciclo 'for' es la forma más común de recorrer los elementos de una lista. 

		```
		for queso in quesos:
			print(queso)

		```

		Esto funciona bien si solo necesitas leer los elementos de la lista. 

		Pero si quieres escribir o actualizar los elementos, necesitas los índices. 

		Una manera común de hacer eso es combinar las funciones incorporadas 'range' y 'len':

		```python

		for i in range(len(numeros)):
			numeros[i] = numeros[i] * 2

		```

		Este bucle recorre la lista y actualiza cada elemento.

		'len' devuelve el número de elementos en la lista. 

		'range' devuelve una lista de índices de 0 a n − 1, donde n es el largo de la lista. 

		En cada paso por el bucle, i obtiene el índice del siguiente elemento. 

		La sentencia de asignación en el cuerpo usa i para leer el valor antiguo del elemento y asignar el nuevo valor.

		Un bucle for a través de una lista vacía nunca ejecuta el cuerpo:
		
		```
		for x in []:
			print('Esto nunca ocurre.')

		```
		

		A pesar de que una lista puede contener otra lista, la lista anidada aún cuenta como un solo elemento. 

		La longitud de esta lista es cuatro:

		```
		['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

		```


	Operaciones de lista:

		El operador + concatena listas:

			```
			a = [1, 2, 3]
			b = [4, 5, 6]
			c = a + b
			c

			```
			[1, 2, 3, 4, 5, 6]


		El operador * repite una lista un número dado de veces:
			
			```
			[0] * 4

			```
			[0, 0, 0, 0]


			```
			[1, 2, 3] * 3

			```
			[1, 2, 3, 1, 2, 3, 1, 2, 3]

			El primer ejemplo repite [0] cuatro veces. 

			El segundo ejemplo repite la lista [1, 2, 3] tresveces.


		Trozos de lista:

			```
			t = ['a', 'b', 'c', 'd', 'e', 'f']
			
			t[1:3]
			
			```
			['b', 'c']
	

			```
			>>> t[:4]

			```
			['a', 'b', 'c', 'd']


			```
			t[3:]

			```
			['d', 'e', 'f']


			Si omites el primer índice, el trozo comienza al principio.

			Si omites el segundo, el trozo llega al final.

			Entonces, si omites ambos, el trozo es una copia de la lista completa.

			```
			t[:]

			```
			['a', 'b', 'c', 'd', 'e', 'f']

			Dado que las listas son mutables, a menudo es útil crear una copia antes de realizar operaciones que modifiquen listas.


			Un operador de trozo en el lado izquierdo de una asignación puede actualizar múltiples elementos:

			```
			t = ['a', 'b', 'c', 'd', 'e', 'f']

			t[1:3] = ['x', 'y']

			t
			
			```
			['a', 'x', 'y', 'd', 'e', 'f']


	Métodos de lista:
	
		Operan en listas. 

		Por ejemplo, 'append' agrega un nuevo elemento al final de la lista:	

		```
		t = ['a', 'b', 'c']
		t.append('d')
		t

		```
		['a', 'b', 'c', 'd']


		'extend' toma una lista como argumento y anexa todos los elementos:

		```
		t1 = ['a', 'b', 'c']
		t2 = ['d', 'e']
		t1.extend(t2)
		t1

		```
		['a', 'b', 'c', 'd', 'e']
		
		Este ejemplo deja a t2 sin modificar.


		'sort' ordena los ejementos de la lista de menor a mayor:

		```
		t = ['d', 'c', 'e', 'b', 'a']
		t.sort()
		t

		```
		['a', 'b', 'c', 'd', 'e']

		La mayoría de los métodos de lista son nulos: modifican la lista y devuelven 'None'.

		Prueba escribiendo 

		```
		t = t.sort()

		```


	Mapas, filtro y reducción: 

		Sumar todos los números de una lista:

		```python

		def sumar_todos(t):
			total = 0
			for x in t:
				total += x
			return total

		```

		'total' se inicializa en 0.

		En cada paso por el bucle, x obtiene un elemento de la lista. 

		El operador += proporciona una manera corta de actualizar una variable. 

		Esta sentencia de asignación aumentada:

			total += x
 			
 			equivalente a:
			
			total = total + x

		A medida que el bucle se ejecuta, total acumula la suma de los elementos; una variable que se utiliza de esta manera a veces se llama 'acumulador'.

		Sumar los elementos de una lista es una operación tan común que Python la facilita como función incorporada, 'sum':

		```
		t = [1, 2, 3]
		sum(t)

		```
		6

		Una operación como esta que combina una secuencia de elementos en un solo valor a veces se llama 'reducción'.


		Recorrer una lista mientras se crear otra: 

			La función toma una lista de cadenas y devuelve una nueva lista que contiene cadenas que comienzan con mayúscula:

			```python

			def todas_con_mayuscula(t):
				res = []
				for s in t:
					res.append(s.capitalize())
				return res

			```

			'res' se inicializa con una lista vacía; en cada paso por el bucle, anexamos el elemento siguiente. 

			Entonces res es otro tipo de acumulador.

			Una operación como 'todas_con_mayuscula' a veces es llamada mapa porque “mapea” una función (en este caso el método 'capitalize' ) sobre cada uno de los elementos en una secuencia.


		Otra operación común es seleccionar algunos de los elementos de una lista y devolver una sublista. 

		Por ejemplo, la siguiente función toma una lista de cadenas y devuelve una lista que contiene solo las cadenas escritas con mayúsculas:

		```
		def solo_mayusculas(t):
			res = []
			for s in t:
				if s.isupper():
					res.append(s)
			return res

		```

		'isupper' es un método de cadena que devuelve True si la cadena solo contiene letras mayúsculas.

		Una operación como solo_mayusculas se llama 'filtro' porque selecciona algunos de los  elementos y filtra los otros.

		La mayoría de las operaciones de lista se pueden expresar como una combinación de mapa, filtro y reducción.


	Eliminar elementos: 	

		Si conoces el índice del elemento que quieres, puedes utilizar 'pop':		

		```
		t = ['a', 'b', 'c']
		x = t.pop(1)
		t

		```
		['a', 'c']


		```
		x

		```
		'b'

		'pop' modifica la lista y devuelve el elemento que se eliminó. 

		Si no entregas un índice, elimina y devuelve el último elemento.


		Si no necesitas el valor eliminado, puedes utilizar el operador 'del':

		```
		t = ['a', 'b', 'c']
		del t[1]
		t

		```
		['a', 'c']


		Si conoces el elemento que quieres eliminar (pero no el índice), puedes utilizar 'remove':

		```
		t = ['a', 'b', 'c']
		t.remove('b')
		t

		```
		['a', 'c']
		
		El valor de retorno de remove es 'None'.


		Para eliminar más de un elemento, puedes utilizar del con índices de trozo:
		
		```
		t = ['a', 'b', 'c', 'd', 'e', 'f']
		
		del t[1:5]
		t

		```
		['a', 'f']

		
		El trozo selecciona todos los elementos hasta el segundo índice pero sin incluirlo.


	Lista y cadenas:

		Una cadena es una secuencia de caracteres y una lista es una secuencia de valores, pero una lista de caracteres no es lo mismo que una cadena. 

		Para convertir una cadena en una lista de caracteres, puedes utilizar 'list':

		```
		s = 'spam'
		t = list(s)
		t

		```
		['s', 'p', 'a', 'm']

		Dado que 'list' es el nombre de una función incorporada, deberías evitar utilizarlo como nombre de variable. 

		Evito 'l' porque se parece mucho a 1, entonces, 't'.


		La función list separa la cadena en letras individuales. 

		Si quieres separar una cadena en palabras, puedes utilizar el método 'split':

		```
		s = 'pining for the fjords'
		t = s.split()
		t

		```
		['pining', 'for', 'the', 'fjords']


		Un argumento opcional llamado 'delimitador' especifica qué caracteres usar como separador de palabras. 

		El siguiente ejemplo usa un guión como delimitador:

		```
		s = 'spam-spam-spam'
		delimitador = '-'
		t = s.split(delimitador)
		t

		```
		['spam', 'spam', 'spam']


		'join' es el inverso de split . 

		Toma una lista de cadenas y concatena los elementos.

		'join' es un método de cadena, por lo que tienes que invocarlo en el delimitador y pasarle la lista como parámetro:

		```
		t = ['pining', 'for', 'the', 'fjords']
		delimitador = ' '
		s = delimitador.join(t)
		s

		```
		'pining for the fjords'

		En este caso el delimitador es un carácter de espacio, por lo que join pone un espacio entre las palabras.

		Para concatenar cadenas sin espacios, puedes usar la cadena vacía, '' , como 'delimitador'.


	Objetos y valores:

		Si ejecutamos estas sentencias de asignación:

		```
		a = 'banana'
		b = 'banana'

		```

		Sabemos que a y b se refieren a una cadena, pero no sabemos si se refieren a la misma cadena. 

		Hay dos estados posibles:

			En el primer caso, a y b se refieren a dos objetos diferentes que tienen el mismo valor. 

			En el segundo caso, se refieren al mismo objeto.

		Para verificar si dos variables se refieren al mismo objeto, puedes usar el operador 'is'.

			a -> 'banana'
			b -> 'banana'

			a -> 'banana' <- b
		
		```
		a = 'banana'
		b = 'banana'
		a is b

		```
		True

		Python solo crea un objeto de cadena y tanto a como b se refieren a este.


		Pero cuando creas dos listas, obtienes dos objetos:

		```
		a = [1, 2, 3]
		b = [1, 2, 3]
		a is b
		
		```
		False

			a -> [1, 2, 3]
			b -> [1, 2, 3]		


		En este caso diríamos que las dos listas son 'equivalentes', porque tienen los 'mismos elementos', pero 'no idénticos', porque no son el mismo objeto. 

		Si dos objetos son idénticos, son también equivalentes, pero si son equivalentes, no necesariamente son idénticos.

		Hasta ahora, hemos estado utilizando “objeto” y “valor” indistintamente, pero es más preciso decir que un 'objeto tiene un valor'. 

		Si evalúas [1, 2, 3], obtienes un objeto de lista cuyo valor es una secuencia de enteros. 

		Si otra lista tiene los mismos elementos, decimos que tiene el mismo valor, pero no es el mismo objeto.


	Alias: 

		Si 'a' se refiere a un objeto y asignas 'b = a' , entonces ambas variables se refieren al mismo objeto:

		```
		a = [1, 2, 3]
		b = a
		b is a

		```
		True

		La asociación de una variable con un objeto se llama 'referencia'. 

		En este ejemplo, hay dos referencias al mismo objeto.

		Un objeto con más de una referencia tiene más de un nombre, por lo que decimos que el objeto tiene un 'alias'.

			a y b -> [1, 2, 3]

		Si el objeto con alias es mutable, los cambios realizados con un alias afectan al otro:

		```
		b[0] = 42
		a

		```
		[42, 2, 3]

		Aunque este comportamiento puede ser útil, es propenso a errores.

		En general, es más seguro evitar los alias cuando trabajes con objetos mutables.

		Para los objetos inmutables como las cadenas, los alias no son tan problemáticos. 

		En este ejemplo:

			a = 'banana'
			b = 'banana'

		Casi nunca hace una diferencia si a y b se refieren a la misma cadena o no.


	Argumentos de lista: 

		Cuando pasas una lista a una función, la función obtiene una referencia a la lista.

		Si la función modifica la lista, la sentencia llamadora ve el cambio. 

		Por ejemplo, no_head quita el primer elemento de una lista:

		```
		def sin_cabeza(t):
			del t[0]

		```

		Se utiliza de la siguiente manera:

		```
		letras = ['a', 'b', 'c']
		no_head(letras)
		letras

		```
		['b', 'c']

		El parámetro 't' y la variable 'letras' son alias para el mismo objeto. 

		El diagrama de pila: la Figura

		__main__: letras y no_head: t

			list
				0 -> 'a'
				1 -> 'b'
				2 -> 'c'
					
		
		Es importante distinguir entre operaciones que modifican listas y operaciones que crean nuevas listas. 

		Por ejemplo, el método 'append' modifica una lista, pero el operador + crea una nueva lista.

		```
		t1 = [1, 2]
	 	t2 = t1.append(3)
	 	t1

		```
		[1, 2, 3]
		

		```
		t2

		```
		None

		El valor de retorno de 'append' es None.


		Aquí hay un ejemplo que utiliza el operador + :
		
		```
		t3 = t1 + [4]
		t1
		
		```
		[1, 2, 3]


		```
		t3
	
		```

		[1, 2, 3, 4]

		El resultado del operador es una lista nueva y la lista original no ha cambiado.



|| Depuración
	
	El uso descuidado de las listas (y otros objetos mutables) puede llevar a largas horas de depuración. 

	Aquí hay algunas trampas comunes y maneras de evitarlas:

	1. La mayoría de los métodos de lista modifican el argumento y devuelven 'None': 

		Esto es lo opuesto a los métodos de cadena, que devuelven una nueva cadena y dejan sola a la original.

		Si te acostumbraste a escribir código de cadena como este:

			```
			palabra = palabra.strip()

			```
		
		Es tentador escribir código de lista como este:
			
			```
			t = t.sort()
			# INCORRECTO!

			```
		
		Dado que sort devuelve 'None', es probable que la siguiente operación que realice con 't' falle.

		Antes de utilizar métodos y operadores de lista, deberías leer la documentación cuidadosamente y luego probarlos en modo interactivo.


	2. Escoge una forma y quédate con esa:
		
		Parte del problema con las listas es que hay muchas maneras de hacer las cosas.

		Por ejemplo, para eliminar un elemento de una lista, puedes utilizar 'pop', 'remove', 'del', o incluso una asignación de trozo.

		Para agregar un elemento, puedes utilizar el método 'append' o el operador '+'.

		Suponiendo que 't' es una lista y 'x' es un elemento de lista, estas líneas son correctas:

		```
		t.append(x)
		t = t + [x]
		t += [x]
		
		```

		Estas son incorrectas:

		```
		t.append([x])
		#INCORRECTO!

		t = t.append(x)
		#INCORRECTO!

		t + [x]
		#INCORRECTO!

		t = t + x
		#INCORRECTO!

		```

		Prueba cada uno de estos ejemplos en modo interactivo para asegurarte de que entiendes lo que haces. 

		Nota que solo el último provoca un error de tiempo de ejecución; los otros tres son legales, pero hacen lo incorrecto.


	3. Crea copias para evitar los alias.
		
		Si quieres utilizar un método como 'sort' que modifique el argumento, pero necesitas mantener la lista original también, puedes crear una copia.

		```
		t = [3, 1, 2]
		t2 = t[:]
		t2.sort()
		t

		```
		[3, 1, 2]


		```
		t2

		```
		[1, 2, 3]

		En este ejemplo podrías utilizar también la función incorporada 'sorted', que devuelve una nueva lista ordenada y deja sola a la original.

		```
		t2 = sorted(t)
	 	t

	 	```
	 	[3, 1, 2]


	 	```
		t2

		```
		[1, 2, 3]




|| Diccionarios

	Una de las mejores caractgerísticas de Python.  

	Los diccionarios son bloques de construcción de muchos algoritmos eficientes y elegantes.


	Un diccionario es un mapeo:

		Es como una lista, pero más general.

		En una lista, los índices tienen que ser enteros; en un diccionario pueden ser (casi) de cualquier tipo.

		Un diccionario contiene una 'colección de índices', que se llaman claves, y una 'colección de valores'. 

		Cada clave está asociada a un valor único. 

		La asociación de una clave y un valor se llama par clave-valor, o a veces 'ítem'.

		En lenguaje matemático, un diccionario representa un 'mapeo' de las claves a los valores, por tanto puedes decir también que cada clave “mapea a” un valor. 

		Como ejemplo, construiremos un diccionario que mapea de palabras en inglés a palabras en español, así las claves y los valores son todas cadenas.

		La función 'dict' crea un nuevo diccionario sin ítems.

		Como dict es el nombre de una función incorporada, deberías evitar utilizarla como nombre de variable.

		```
		ing_esp = dict()
		ing_esp

		```
		{}

		Las llaves, {}, representan un diccionario vacío. 

		Para agregar ítems al diccionario, puedes utilizar corchetes:

		```
		ing_esp['one'] = 'uno'

		```

		Esta línea crea un ítem que mapea de la clave 'one' al valor 'uno'. 

		Si imprimimos el diccionario de nuevo, vemos un par 'clave-valor' con un signo de dos puntos entre la clave y el valor:

		```
		ing_esp

		```
		{'one': 'uno'}


		Este formato de salida es también un formato de entrada. 

		Por ejemplo, puedes crear un nuevo diccionario con tres ítems:

		```
		ing_esp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

		```

		Pero si imprimes ing_esp quizás te sorprendas:

		```
		ing_esp

		```
		{'one': 'uno', 'three': 'tres', 'two': 'dos'}

		El orden de los pares clave-valor podría no ser el mismo. 

		Si escribiste el mismo ejemplo en tu computador, podrías obtener un resultado diferente. 

		En general, el 'orden' de los ítems en un diccionario es 'impredecible'.


		Sin embargo, eso no es un problema porque los elementos de un diccionario nunca se indexan con índices enteros. 

		En cambio, utilizas las claves para buscar los valores correspondientes:

		```
		ing_esp['two']

		```	
		'dos'

		La clave 'two' siempre mapea al valor 'dos', entonces el orden de los ítems no importa.


		Si la clave no está en el diccionario, obtienes una excepción:

		```
		ing_esp['four']
		
		```
		KeyError: 'four'

	
		La función 'len' funciona con diccionarios: 

		Devuelve el número de pares clave-valor.

		```
		len(ing_esp)

		```
		3


		El operador 'in' también funciona con diccionarios:

		Te dice si algo aparece como una clave en el diccionario (aparecer como un valor no basta).

		```
		'one' in ing_esp

		```
		True


		```
		'uno' in ing_esp

		```
		False

		Para ver si algo aparece como un 'valor' en un diccionario, puedes utilizar el método 'values', el cual devuelve una colección de valores, y entonces utilizar el operador in:

		```
		valores = ing_esp.values()
		'uno' in valores
		
		```
		True


		El operador 'in' utiliza diferentes algoritmos para las listas y los diccionarios. 

		Para las listas, busca los elementos de la lista en orden.

		A medida que la lista se vuelve más larga, el tiempo de búsqueda se hace más largo en proporción directa.

		Los diccionarios de Python utilizan una estructura de datos llamada 'tabla hash que tiene una propiedad notable: 

		el operador 'in' toma casi la misma cantidad de tiempo sin importar cuántos ítems hay en el diccionario.


	Diccionario como colección de contadores:

		Si tenemos una cadena y quieremos contar cuántas veces aparece cada letra. 

		Hay varias maneras para hacerlo:

		1. Podrías crear 26 variables, una para cada letra del alfabeto: 

			Luego podrías recorrer la cadena y, para cada carácter, incrementar el contador correspondiente, probablemente utilizando un condicional encadenado.


		2. Podrías crear una lista de 26 elementos. 

			Luego podrías convertir cada carácter a un número (usando la función incorporada 'ord' ), utilizar el número como un índice dentro de la lista e incrementar el contador apropiado.


		3. Podrías crear un diccionario con caracteres como claves y contadores como los valores correspondientes. 

			La primera vez que veas un carácter, añadirías un ítem al diccionario.

			Después de eso incrementarías el valor de un ítem existente.


		Una 'implementación' es una manera de realizar un calculo o algoritmo; algunas implementaciones son mejores que otras. 

		Por ejemplo, una ventaja de la implementación con diccionario es que no tenemos que saber de antemano qué letras aparecen en la cadena y solo tenemos que hacer espacio para las letras que sí aparecen.

		```
		def histograma(s):
			d = dict()
			for c in s:
				if c not in d:
					d[c] = 1
				else:
					d[c] += 1
			return d

		```

		El nombre de la función es histograma, que es un término estadístico para una colección de contadores (o frecuencias).

		La primera línea de la función crea un diccionario vacío. 

		El bucle for recorre la cadena. 

		En cada paso por el bucle, si el carácter c no está en el diccionario, creamos un nuevo ítem con clave c y valor inicial 1 (dado que hemos visto esta letra una vez). 

		Si c ya está en el diccionario, incrementamos d[c].

		Funciona así:
		
		```
		h = histograma('brontosaurus')
		h

		```
		{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}


		Los diccionarios tienen un método llamado 'get' que toma una clave y un valor por defecto.
		
		Si la clave aparece en el diccionario, 'get' devuelve el valor correspondiente; de lo contrario, devuelve el valor por defecto.

		```
		>>> h = histograma('a')
		>>> h

		```
		{'a': 1}


		```
		h.get('a', 0)
		
		```
		1


		```
		h.get('c', 0)

		```
		0


	Bucles y diccionarios:

		Si utilizas un diccionario en una sentencia 'for', este recorre las claves del diccionario. 

		Ej. 'imprimir_hist' imprime cada clave y el valor correspondiente:

		```
		def imprimir_hist(h):
			for c in h:
				print(c, h[c])

		```

		La salida es: 

		```
		h = histograma('parrot')
		imprimir_hist(h)
		
		```
		a 1
		p 1
		r 2
		t 1
		o 1


		Nuevamente, las claves no estan en un orden particular. 

		Para recorrer las claves en orden, puedes utilizar la función incorporada 'sorted':

		```
		for clave in sorted(h):

			print(clave, h[clave])

		```
		a 1
		o 1
		p 1
		r 2
		t 1


	Consulta inversa:

		Dado un diccionario d y una clave k , es fácil encontrar el valor correspondiente v = d[k].
		
		Esta operación se llama consulta ('lookup').

		Si tienes 'v' y quieres encontrar 'k', tienes dos problemas: 

		Primero, podría haber más de una clave que mapee al valor v. 

		Dependiendo de la aplicación, quizás puedas elegir una o tengas que hacer una lista que las contenga a todas. 

		Segundo, no hay una sintaxis sencilla para hacer una consulta inversa: tienes que buscar.

		Una función que toma un valor y devuelve la primera clave que mapea a ese valor:

		```
		def consulta_inversa(d, v):
			for k in d:
				if d[k] == v:
					return k
			raise LookupError()

		```

		Esta función es otro ejemplo de patrón de búsqueda pero que utiliza una característica que no hemos visto antes, 'raise'. 

		La sentencia raise causa una excepción; en este caso causa un 'LookupError', que es una excepción incorporada que se utiliza para indicar que falló una operación de consulta.

		Si se llega al final del bucle, significa que 'v' no aparece en el diccionario como valor, por lo que plantea una excepción.

		Consulta inversa eficaz:

		```
		h = histograma('parrot')
		clave = consulta_inversa(h, 2)
		clave

		```
		'r'


		Y una ineficaz:

		```
		clave = consulta_inversa(h, 3)

		```
		Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
			File "<stdin>", line 5, in consulta_inversa
		LookupError


		El efecto de cuando levantas una excepción mediante raise es el mismo que cuando Python levanta una: imprime un rastreo y un mensaje de error.

		Cuando levantes una excepción, puedes proporcionar un mensaje de error detallado como argumento opcional. 

		Por ejemplo:

		```
		raise LookupError('el valor no aparece en el diccionario')

		```
		Traceback (most recent call last):
			File "<stdin>", line 1, in ?

		LookupError: el valor no aparece en el diccionario


		Una consulta inversa es mucho más lenta que una consulta directa; si tienes que hacerlo a menudo, o si el diccionario se vuelve grande, el rendimiento de tu progama se verá afectado.


	Diccionarios y listas:

		Las listas pueden aparecer como valores en un diccionario. 

		Por ejemplo, si te dan un diccionario que mapea de letras a frecuencias, quizás quieras invertirlo, es decir, crear un diccionario que mapee de frecuencias a letras. 

		Dado que podría haber muchas letras con la misma frecuencia, cada valor en el diccionario invertido debería ser una lista de letras.

		función que invierte un diccionario:

		```ython
		def invertir_dict(d):
			inverso = dict()
			for clave in d:
				valor = d[clave]
				if valor not in inverso:
					inverso[valor] = [clave]
				else:
					inverso[valor].append(clave)
			return inverso

		```

		En cada paso por el bucle, clave obtiene una clave de d y valor obtiene el valor correspondiente. 

		Si valor no está en inverso, lo cual significa que no lo hemos visto antes, entonces creamos un nuevo ítem y lo inicializamos con un 'singleton' (una lista que contiene un único elemento).

		De lo contrario, hemos visto este valor antes, por lo cual anexamos a la lista la clave correspondiente.

		Ejemplo de uso:

		```
		>>> hist = histograma('parrot')
		>>> hist

		```		
		{'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}


		```
		>>> inv = invertir_dict(hist)
		>>> inv

		```
		{1: ['a', 'p', 't', 'o'], 2: ['r']}

		
		Diagrama de estado: 

			hist -> dict
					'a'-> 1
					'p'-> 1
					'r'-> 2
					't'-> 1
					'o'-> 1
					
			inv -> dict list
					1 -> 0 -> 'a'
						 1 -> 'p'
						 2 -> 't'
						 3 -> 'o'

					2 -> 0 -> 'r'
		
		Muestra a 'hist' e 'inv'. 

		Un diccionario se representa como una caja con el tipo dict arriba suyo y el par clave-valor adentro. 

		Si los valores son enteros, números de coma flotante o cadenas, los dibujo adentro de la caja, pero usualmente dibujo las listas afuera de la caja, solo para mantener simple al diagrama.


		Las listas pueden ser valores en un diccionario, tal como muestra este ejemplo simple, pero no pueden ser claves. 

		Esto es lo que ocurre si lo intentas:

		```
		t = [1, 2, 3]
		d = dict()
		d[t] = 'ups'

		```

		Traceback (most recent call last):
			File "<stdin>", line 1, in ?
		TypeError: list objects are unhashable


		Anteriormente mencioné que un diccionario se implementa utilizando una 'tabla hash' y eso significa que las claves tienen que ser 'hashables'.

		Un hash es una función que toma un valor (de cualquier tipo) y devuelve un entero.

		Los diccionarios utilizan estos enteros, llamados 'valores hash', para almacenar y consultar pares clave-valor.

		Este sistema funciona bien si las claves son inmutables. 

		Pero si las claves son mutables, como las listas, ocurren cosas malas. 

		Por ejemplo, cuando creas un par clave-valor, Python hashea la clave y la almacena en la ubicación correspondiente. 

		Si modificas la clave y luego la hasheas de nuevo, iría a una ubicación diferente. 

		En ese caso podrías tener dos entradas para la misma clave, o quizás no seas capaz de encontrar una clave.

		De cualquier manera, el diccionario no funcionaría de manera correcta.

		Por eso es que las claves tienen que ser hashables y, por la misma razón, los tipos mutables como las listas no lo son. 

		La manera más simple de evitar esta limitación es utilizar 'tuplas'.

		Dado que los diccionarios son mutables, estos no pueden utilizarse como claves, pero pueden utilizarse como valores.


	Memos: 

		En la función fibonacci mientras más grande es el argumento que entregues, más tarda la función en ejecutarse. 

		Además, el tiempo de ejecución aumenta rápidamente.

		Gráfico de llamadas para fibonacci con n=4:

			fibonacci n->4: 
				n->3 n->2

			fibonacci n->3:
				n->2 n->1

			fibonacci n->2:
				n->1 n->0

			fibonacci n->2:
				n->1 n->0

			
		Un gráfico de llamadas muestra un conjunto de marcos de funciones, con líneas que conectan cada marco a los marcos de las funciones que están siendo llamadas. 

		En la parte de arriba del gráfico, fibonacci con n=4 llama a fibonacci con n=3 y n=2. 

		A su vez, fibonacci con n=3 llama a fibonacci con n=2 y n=1. 

		Y así sucesivamente.
	
		Cuenta cuántas veces se llama a fibonacci(0) y fibonacci(1). 

		Esta es una solución ineficiente para el probema y se pone peor a medida que el argumento se hace más grande.

		Una solución es hacer un seguimiento de los valores que ya han sido calculados almacenándolos en un diccionario. 

		Un valor previamente calculado que se almacena para un uso posterior se llama 'memo'. 

		Aquí hay una versión “memoizada” de fibonacci:

		```
		conocidos = {0:0, 1:1}
		
		def fibonacci(n):
			if n in conocidos:
				return conocidos[n]

		resultado = fibonacci(n-1) + fibonacci(n-2)
		conocidos[n] = resultado
		return resultado

		```

		'conocidos' es un diccionario que hace un seguimiento de los números de Fibonacci que ya conocemos. 

		Comienza con dos ítems: 0 mapea a 0 y 1 mapea a 1.

		Cada vez que se llama a fibonacci, revisa a conocidos. 

		Si el resultado ya está ahí, puede devolverlo inmediatamente. 

		De lo contrario, tiene que calcular el nuevo valor, agregarlo al diccionario y devolverlo.

		Si ejecutas esta versión de fibonacci y la comparas con la original, encontrarás que esta es mucho más rápida.


	Variables globales:

		En el ejemplo anterior, 'conocidos' se crea fuera de la función, por lo que pertenece al marco especial llamado '__main__'. 

		Las variables en __main__ a veces se llaman globales porque se puede acceder a ellos desde cualquier función. 

		A diferencia de las variables locales, que desaparecen cuando su función termina, las 'variables globales persisten' de una llamada a función a la siguiente.

		Es común utilizar variables globales para las banderas (en inglés, 'flags'), es decir, 'variables booleanas' que indican si una condición es verdadera. 

		Por ejemplo, algunos programas utilizan una bandera llamada 'verbose' para controlar el nivel de detalle en la salida:		

		```
		verbose = True
		def ejemplo1():
			if verbose:
				print('Ejecutando ejemplo1')

		```

		Si intentas reasignar una variable global, quizás te sorprendas. 

		El siguiente ejemplo se supone que hace seguimiento de si la función ha sido llamada:

		```
		fue_llamada = False
		
		def ejemplo2():
			fue_llamada = True
			# INCORRECTO

		```


		Pero si lo ejecutas verás que el valor de 'fue_llamada' no cambia. 

		El problema es que 'ejemplo2' crea una nueva variable local con nombre fue_llamada. 

		La variable local se va cuando la función termina y no tiene efecto en la variable global.

		Para reasignar una variable global dentro de una función, tienes que declarar la variable global antes de utilizarla:

		```
		fue_llamada = False
		def ejemplo2():
			global fue_llamada
			fue_llamada = True

		```

		La sentencia 'global' le dice al intérprete algo como “En esta función, cuando digo fue_llamada, me refiero a la variable global; no crees una local.”



|| Depuración

	A medida que trabajes con conjuntos de datos más grandes, depurar imprimiendo y verificando la salida a mano puede volverse algo difícil de manejar. 

	Aquí hay algunas sugerencias para depurar conjuntos grandes de datos.

	1. Reduce la escala:

		Si es posible, reduce el tamaño del conjunto de datos. 

		Por ejemplo, si el programa lee un archivo de texto, comienza solo con las primeras 10 líneas, o con el ejemplo más pequeño que puedas encontrar. 

		Puedes editar aquellos archivos o (mejor) modificar el programa de manera que este lea solo las primeras n líneas.

		Si hay un error, puedes reducir n al valor más pequeño que muestre el error y luego incrementarlo gradualmente mientras encuentras y corriges los errores.


	2. Revisa resúmenes y tipos:

		En lugar de imprimir y verificar el conjunto de datos completo, considera imprimir resúmenes de los datos: por ejemplo, el número de ítems en el diccionario o el total de una lista de números.

		Una causa común de errores de tiempo de ejecución es un valor que no es del tipo correcto. 

		Para depurar esta clase de errores, a menudo es suficiente imprimir el tipo del valor.


	3. Escribe verificaciones automáticas: 

		A veces puedes escribir código para verificar errores de manera automática. 

		Por ejemplo, si estás calculando el promedio de una lista de números, podrías verificar que el resultado no sea mayor que el elemento más grande de la lista ni menor que el más pequeño.

		A esto se le llama “prueba de cordura” (en inglés, 'sanity check') porque detecta resultados que son “locos”. 

		Otro tipo de prueba compara los resultados de dos computaciones diferentes para ver si son consistentes. 

		A esto se le llama “prueba de consistencia”.


	4. Dale formato a la salida: 

		Dar formato a la salida de la depuración puede hacer más fácil detectar un error.

		Otra herramienta que quizás encuentres útil es el módulo 'pprint', el cual proporciona una función pprint que muestra tipos incorporados en un formato más legible por humanos ( 'pprint' significa “pretty print”).

	
	Nuevamente, el tiempo que pasas construyendo andamiaje puede reducir el tiempo que pasas depurando.



|| Tuplas

	Son un tipo de dato que pueden trabajar junto con las listas, diccionarios.


	Inmutabilidad: 

		Una tupla es una secuencia de valores. 

		Los valores pueden ser de cualquier tipo y están indexados por enteros, por lo que en ese sentido las tuplas se parecen mucho a las listas.

		La diferencia importante es que las tuplas son inmutables.

		Una tupla es una lista de valores separados por comas:

		```
		t = 'a', 'b', 'c', 'd', 'e'

		```


		Aunque no es necesario, es común encerrar las tuplas en paréntesis:

		```
		t = ('a', 'b', 'c', 'd', 'e')

		```


		Para crear una tupla con un solo elemento, tienes que incluir una coma final:

		```
		t1 = 'a',
		type(t1)

		```
		<class 'tuple'>


		Un valor en paréntesis no es una tupla:

		```
		t2 = ('a')
		type(t2)

		```
		<class 'str'>


		Otra manera de crear una tupla es la función incorporada 'tuple'. 

		Sin argumentos, esta crea una tupla vacía:

		```
		t = tuple()
		t

		```
		()

		Si el argumento es una secuencia (cadena, lista o tupla), el resultado es una tupla con los elementos de la secuencia:

		```
		t = tuple('lupins')
		t

		```
		('l', 'u', 'p', 'i', 'n', 's')

		Dado que tuple es el nombre de una función incorporada, deberías evitar usarlo como nombre de una variable.


		La mayoría de los operadores de lista funcionan también en tuplas. 

		El operador de corchetes indexa un elemento:

		```
		t = ('a', 'b', 'c', 'd', 'e')
		t[0]

		```
		'a'

		Y el operador de trozo selecciona un rango de elementos.

		```
		t[1:3]

		```
		('b', 'c')

		Sin embargo, si intentas modificar uno de los elementos de la tupla, obtienes un error:

		```
		t[0] = 'A'

		```
		TypeError: object doesn't support item assignment

		Dado que las tuplas son inmutables, no puedes modificar sus elementos.

		Pero puedes reemplazar una tupla con otra:

		```
		t = ('A',) + t[1:]
		t

		```
		('A', 'b', 'c', 'd', 'e')

		Esta sentencia crea una nueva tupla y luego hace que t se refiera a esta.


		Los operadores relacionales funcionan con las tuplas y otras secuencias; Python comienza comparando el primer elemento de cada secuencia. 

		Si son iguales, avanza a los siguientes elementos, y así sucesivamente, hasta que encuentre elementos que sean diferentes. 

		Los elementos posteriores no se consideran (incluso si son realmente grandes).

		```
		(0, 1, 2) < (0, 3, 4)

		```
		True

		```
		(0, 1, 2000000) < (0, 3, 4)

		```
		True


	Asignación de tupla:

		A menudo es útil intercambiar los valores de dos variables. 

		Con asignaciones convencionales, tienes que utilizar una variable temporal.

		Por ejemplo, para intercambiar a y b :

		```
		temp = a
		a = b
		b = temp

		```

		Esta solución es incómoda; la asignación de tupla es más elegante:

		```
		a, b = b, a

		```

		El lado izquierdo es una tupla de variables; el lado derecho es una tupla de expresiones.

		Cada valor es asignado a su respectiva variable. 

		Todas las expresiones en el lado derecho son evaluadas antes que cualquiera de las asignaciones.

		La cantidad de variables en el lado izquierdo y la cantidad de valores del lado derecho tienen que ser la misma:

		```
		a, b = 1, 2, 3

		```
		ValueError: too many values to unpack

		De manera más general, el lado derecho puede ser cualquier tipo de secuencia (cadena, lista o tupla). 

		Por ejemplo, para separar una dirección de email en nombre de usuario y dominio, podrías intentar:

		```
		direccion = 'monty@python.org'
		nombre_usuario, dominio = direccion.split('@')

		```

		El valor de retorno de split es una lista con dos elementos: el primer elemento se asigna a nombre_usuario, el segundo a dominio.

		```
		nombre_usuario

		```
		'monty'


		```
		dominio

		```
		'python.org'


	Tuplas como valores de retorno:

		Estrictamente hablando, una función puede devolver solo un valor de retorno, pero si el valor es una tupla, el efecto es el mismo que devolver múltiples valores.

		Por ejemplo, si quieres dividir dos enteros y calcular el cociente y el resto, es ineficiente calcular x//y y luego x %y.

		Es mejor calcular ambos al mismo tiempo.

		La función incorporada 'divmod' toma dos argumentos y devuelve una tupla de dos valores: el cociente y el resto. 

		Puedes almacenar el resultado como una tupla:

		```
		t = divmod(7, 3)
		t

		```
		(2, 1)


		O bien, utilizar asignación de tupla para almacenar los elementos por separado:

		```
		cociente, resto = divmod(7, 3)
		cociente

		```
		2


		```
		resto

		```
		1


		Ejemplo de una función que devuelve una tupla:

		```
		def min_max(t):
			return min(t), max(t)

		```

		max y min son funciones incorporadas que encuentran los elementos más grande y más pequeño en una secuencia.

		'min_max' calcula ambos y devuelve una tupla de dos valores.


	Tuplas de argumentos de longitud variable:

		Las funciones pueden tomar una cantidad variable de argumentos. 

		Un nombre de parámetro que comienza con * hace una reunión de argumentos en una tupla. 

		Por ejemplo, 'printall' toma cualquier cantidad de argumentos y los imprime:

		```
		def printall(*args):
			print(args)

		```

		El parámetro de reunión puede tener cualquier nombre que quieras, pero args es convencional. 

		Aquí se muestra cómo opera la función:

		```
		printall(1, 2.0, '3')

		```
		(1, 2.0, '3')

		El complemento de la reunión es la dispersión. 

		Si tienes una secuencia de valores y quieres pasarlo a una función como multiples argumentos, puedes utilizar el operador *. 

		Por ejemplo, 'divmod' toma exactamente dos argumentos; no funciona con una tupla:

		```
		t = (7, 3)
		divmod(t)

		```
		TypeError: divmod expected 2 arguments, got 1

		Sin embargo, si dispersas la tupla, funciona:

		```
		divmod(*t)

		```
		(2, 1)

		Muchas de las funciones incorporadas utilizan tuplas de argumentos de longitud variable.

		Por ejemplo, max y min pueden tomar cualquier cantidad de argumentos:

		```
		max(1, 2, 3)

		```
		3

		Pero sum no puede.

		```
		sum(1, 2, 3)

		```
		TypeError: sum expected at most 2 arguments, got 3

		
	Listas y tuplas:

		'zip' es una función incorporada que toma dos o más secuencias y las intercala. 

		El nombre de la función se refiere a una cremallera (zipper), ya que esta intercala dos filas de dientes.

		Este ejemplo le hace zip a una cadena y una lista:

		```
		s = 'abc'
		t = [0, 1, 2]
		zip(s, t)

		```
		<zip object at 0x7f7d0a9e7c48>

		El resultado es un objeto zip que sabe cómo iterar a través de los pares. 

		El uso más común de zip es en un bucle for:

		```
		for par in zip(s, t):

		```
		...
		print(par)
		...
		('a', 0)
		('b', 1)
		('c', 2)

		Un objeto zip es una especie de iterador, que es cualquier objeto que itera a través de una secuencia. 

		Los iteradores son similares a las listas de alguna manera, pero a diferencia de las listas, no puedes utilizar un índice para seleccionar un elemento de un iterador.

		Si quieres utilizar operadores de lista y métodos, puedes utilizar un objeto zip para crear una lista:

		```
		>>> list(zip(s, t))

		```
		[('a', 0), ('b', 1), ('c', 2)]

		El resultado es una lista de tuplas; en este ejemplo, cada tupla contiene un carácter de la cadena y el elemento correspondiente de la lista.


		Si las secuencias no tienen la misma longitud, el resultado tiene la longitud de la secuencia más corta.

		```
		list(zip('Anne', 'Elk'))

		```
		[('A', 'E'), ('n', 'l'), ('n', 'k')]

		Puedes utilizar asignación de tupla en un bucle for para recorrer una lista de tuplas:

		```
		t = [('a', 0), ('b', 1), ('c', 2)]
		for letra, numero in t:
			print(numero, letra)

		```

		En cada paso por el bucle, Python selecciona la siguiente tupla en la lista y asigna los elementos a letra y numero. 

		La salida de este bucle es:
		0 a
		1 b
		2 c

		Si combinas zip, for y asignación de tupla, obtienes una manera útil para recorrer dos (o más) secuencias al mismo tiempo. 

		Por ejemplo, 'tiene_coincidencia' toma dos secuencias, t1 y t2 , y devuelve True si hay un índice i tal que t1[i] == t2[i]:

		```
		def tiene_coincidencia(t1, t2):
			for x, y in zip(t1, t2):
				if x == y:
					return True
				return False

		```

		Si necesitas recorrer los elementos de una secuencia y sus índices, puedes utilizar la función incorporada enumerate:

		```
		for indice, elemento in enumerate('abc'):
			print(indice, elemento)

		```

		El resultado de enumerate es un objeto enumerate, que itera una secuencia de pares; cada par contiene un índice (comenzando desde 0) y un elemento de la secuencia dada.

		En este ejemplo, la salida es
		0 a
		1 b
		2 c
		otra vez.


	Diccionarios y tuplas:

		Los diccionarios tienen un método llamado 'items' que devuelve una secuencia de tuplas, donde cada tupla es un par clave-valor.

		```
		d = {'a':0, 'b':1, 'c':2}
		t = d.items()
		t

		```
		dict_items([('c', 2), ('a', 0), ('b', 1)])


		El resultado es un objeto dict_items, que es un iterador que itera los pares clave-valor.

		Puedes utilizarlo en un bucle for así:

		```
		for clave, valor in d.items():

		```
		...
		print(clave, valor)
		...
		c 2
		a 0
		b 1

		Tal como esperarías de un diccionario, los ítems no están en un orden particular.

		En sentido contrario, puedes utilizar una lista de tuplas para inicializar un nuevo diccionario:

		```
		t = [('a', 0), ('c', 2), ('b', 1)]
		d = dict(t)
		d

		```
		{'a': 0, 'c': 2, 'b': 1}

		Combinando dict con zip se produce una manera concisa de crear un diccionario:

		```
		>>> d = dict(zip('abc', range(3)))
		>>> d

		```
		{'a': 0, 'c': 2, 'b': 1}

		El método de diccionario update además toma una lista de tuplas y las agrega, como pares clave-valor, a un diccionario existente.

		Es común utilizar tuplas como claves en diccionarios (principalmente porque no puedes utilizar listas). 

		Por ejemplo, un directorio telefónico podría mapear de pares apellido-nombre a números telefónicos. 

		Suponiendo que hemos definido apellido, nombre y numero, podríamos escribir:

		```
		directorio[apellido, nombre] = numero

		```

		La expresión en corchetes es una tupla. 

		Podríamos utilizar asignación de tupla para recorrer este diccionario.

		```
		for apellido, nombre in directorio:
			print(nombre, apellido, directorio[apellido,nombre])

		```

		Este bucle recorre las claves en directorio, que son tuplas.

		Asigna los elementos de cada
		tupla a apellido y nombre, luego imprime el nombre completo y el número telefónico correspondiente.


		Hay dos maneras de representar tuplas en un diagrama de estado. 

		La versión más detallada muestra los índices y elementos tal como aparecen en una lista. 

		Por ejemplo, la tupla ('Cleese', 'John') se mostraría como en la Figura 12.1.

		Pero en un diagrama más grande quizás quieras omitir los detalles. 

		Por ejemplo, un diagrama del directorio telefónico podría mostrarse como en la Figura 12.2.


	Secuencias de secuencias:

		Los ej se aplicaron a listas de tuplas, pero casi todos también con listas de listas, tuplas de tuplas y tuplas de listas. 

		Para evitar enumerar las
		posibles combinaciones, a veces es más fácil hablar de secuencias de secuencias.

		En muchos contextos, los diferentes tipos de secuencias (cadenas, listas y tuplas) se pueden utilizar indistintamente.

		Entonces, ¿cómo deberías escoger uno por sobre los otros?

		Para comenzar con lo obvio, las cadenas son más limitadas que las otras secuencias porque
		los elementos tienen que ser caracteres. 

		Además, son inmutables. 

		Si necesitas la posibilidad
		de cambiar los caracteres en una cadena (en contraposición a crear una nueva cadena), quizás quieras utilizar una lista de caracteres en su lugar.

		Las listas son más comunes que las tuplas, principalmente porque son mutables. 

		Sin embargo, hay algunos casos donde podrías preferir tuplas:

		1. En algunos contextos, como una sentencia return, es sintácticamente más simple
		crear una tupla que una lista.

		2. Si quieres utilizar una secuencia como clave de diccionario, tienes que utilizar un tipo
		inmutable como una tupla o una cadena.

		3. Si pasas una secuencia como argumento a una función, utilizar tuplas reduce las posibilidades de comportamiento inesperado debido a los alias.

		Dado que las tuplas son inmutables, no proporcionan métodos como sort y reverse,
		que modifican listas existentes. 

		Sin embargo, Python proporciona la función incorporada
		sorted, que toma cualquier secuencia y devuelve una lista nueva con los mismos elementos en orden, y reversed, que toma una secuencia y devuelve un iterador que recorre la
		lista en orden invertido.



|| Depuración

	Las listas, diccionarios y tuplas son ejemplos de 'estructuras de datos'; comenzamos a ver estructuras de datos combinadas, como listas de tuplas, o diccionarios que contienen tuplas como claves y listas como valores. 

	Las estructuras de datos combinadas son útiles, pero son propensas a lo que yo llamo 'errores de forma', es decir, errores causados cuando una estructura de datos tiene el tipo, tamaño o estructura incorrecta. 

	Por ejemplo, si estás esperando una lista que contiene un entero y yo te doy un simple y viejo entero (no en una lista), no funcionará.

	Para ayudar a depurar esta clase de errores, he escrito un módulo llamado 'structshape' que proporciona una función, también llamada structshape, que toma cualquier tipo de estructura de datos como argumento y devuelve una cadena que resume su forma. 

	Aquí hay un resultado para una lista simple:

	```
	from structshape import structshape
	t = [1, 2, 3]
	structshape(t)

	```
	'list of 3 int'

	Un programa más elegante podría escribir “list of 3 ints”, pero fue más fácil no lidiar con los plurales. 

	Aquí hay una lista de listas:

	```
	t2 = [[1,2], [3,4], [5,6]]
	structshape(t2)

	```
	'list of 3 list of 2 int'

	Si los elementos de la lista no son del mismo tipo, structshape los agrupa, en orden, por
	tipo:

	```

	t3 = [1, 2, 3, 4.0, '5', '6', [7], [8], 9]
	structshape(t3)

	```
	'list of (3 int, float, 2 str, 2 list of int, int)'


	Aquí hay una lista de tuplas:

	```
	s = 'abc'
	lt = list(zip(t, s))
	structshape(lt)

	```
	'list of 3 tuple of (int, str)'

	Y aquí hay un diccionario con 3 ítems que mapean enteros a cadenas.

	```
	d = dict(lt)
	structshape(d)

	```
	'dict of 3 int->str'

	Si tienes problemas al hacer seguimiento de tus estructuras de datos, structshape puede ayudar.



|| Estudio de Estructuras de datos
	
	Las estructuras de datos y de control son fundamentales para los algoritmos. 


	Números aleatorios:

		Dadas las mismas entradas, la mayoría de los programas de computador generan las mismas salidas cada vez, por lo que se dice que son 'deterministas'. 

		El determinismo es usualmente algo bueno, ya que esperamos que los mismos cálculos produzcan el mismo resultado. 

		Para algunas aplicaciones, sin embargo, queremos que el computador sea impredecible.

		Los juegos son un ejemplo obvio, pero hay más.

		Hacer un programa verdaderamente no determinista resulta difícil, pero hay maneras de hacer que al menos parezca no determinista. 

		Una de ellas es utilizar algoritmos que generen 'números pseudoaleatorios¿.

		Los números pseudoaleatorios no son verdaderamente aleatorios porque se generan por una computación determinista, pero solo mirando a dichos números es casi imposible distinguirlos de los aleatorios.

		El módulo 'random' proporciona funciones que generan números pseudoaleatorios (que simplemente llamaré “aleatorios” desde aquí en adelante).

		La función random devuelve un número de coma flotante aleatorio entre 0.0 y 1.0 (incluyendo 0.0 pero no 1.0).

		Cada vez que llamas a random, obtienes el siguiente número de una larga serie. 

		Para ver una muestra, ejecuta este bucle:

		```python

		import random
		for i in range(10):
			x = random.random()
			print(x)

		```

		La función 'randint' toma los parámetros low y high y devuelve un entero entre low y high (incluyendo a ambos).

		```
		random.randint(5, 10)
	
		```
		5


		```	
		random.randint(5, 10)

		```
		9


		Para escoger un elemento de una secuencia de manera aleatoria, puedes usar 'choice':

		```
		t = [1, 2, 3]
		random.choice(t)

		```
		2


		```
		random.choice(t)

		```
		3

		El módulo random también proporciona funciones para generar valores aleatorios a partir de 'distribuciones continuas', incluyendo la gaussiana, exponencial, gamma y más. 


	Palabras más comunes:

		Para encontrar las palabras más comunes, podemos crear una lista de tuplas, donde cada tupla contenga una palabra y su frecuencia, y ordenarla.

		La siguiente función toma un histograma y devuelve una lista de tuplas frecuencia-palabra:

		```
		def mas_comunes(hist):
			t = []
			for clave, valor in hist.items():
				t.append((valor, clave))
			t.sort(reverse=True)
			return t

		```
		
		En cada tupla, la frecuencia aparece primero, por lo que la lista resultante está ordenada por frecuencia.

		Aquí hay un bucle que imprime las diez palabras más comunes:

		```
		t = mas_comunes(hist)
		
		print('Las palabras más comunes son:')
			
			for frec, palabra in t[:10]:
				print(palabra, frec, sep='\t')

		```

		El argumento de palabra clave 'sep' es para decirle a print que utilice un carácter de tabulación como “separador”, en lugar de un espacio, así la segunda columna está alineada.

		Estos son los resultados de 'Emma':

		Las palabras más comunes son:
		
			to
			5242

			the
			5205

			and
			4897

			of
			4295

			i
			3191

			a
			3130

			it
			2529

			her
			2483

			was
			2400

			she
			2364

		Este código se puede simplificar utilizando el parámetro key de la función 'sort'


	Parámetros opcionales:

		Es posible, además, escribir funciones definidas por el programador con argumentos opcionales. 

		Por ejemplo, aquí hay una función que imprime las palabras más comunes de un histograma:

		```
		def imprime_mas_comunes(hist, num=10):
			t = mas_comunes(hist)
			print('Las palabras más comunes son:')
			for frec, palabra in t[:num]:
				print(palabra, frec, sep='\t')

		```

		El primer parámetro es obligatorio, el segundo es opcional. 

		El valor por defecto de num es 10.

		Si solo entregas un argumento:

		```
		imprimir_mas_comunes(hist)

		```
		'num' obtiene el valor por defecto. 


		Si entregas dos argumentos:

		```
		imprimir_mas_comunes(hist, 20)
	
		```
		'num' obtiene el valor del argumento en su lugar. 

		En otras palabras, el argumento opcional 'anula' al valor por defecto.

		Si una función tiene parámetros tanto obligatorios como opcionales, todos los parámetros obligatorios tienen que ir primero, seguido por los opcionales.


	Diferencia de diccionarios:

		Encontrar las palabras del libro que no están en la lista de palabras de words.txt es un problema que podrías reconocer como 'diferencia de conjuntos', es decir, queremos encontrar todas las palabras de un conjunto (las palabras en el libro) que no están en el otro (las palabras en la lista).

		'diferencia' toma dos diccionarios, d1 y d2, y devuelve un nuevo diccionario que contiene todas las claves de d1 que no están en d2 . 

		Dado que en realidad no nos importan los valores, los ponemos todos como 'None'.

		```
		def diferencia(d1, d2):
			res = dict()
			for clave in d1:
				if clave not in d2:
					res[clave] = None
			return res

		```

		Para encontrar las palabras en el libro que no están en words.txt, podemos utlizar 'procesar_archivo' para construir un histograma para words.txt, y luego obtener la diferencia:

		```
		palabras = procesar_archivo('words.txt')
		
		dif = diferencia(hist, palabras)
		
		print("Palabras en el libro que no están en la lista de palabras:")
			
			for palabra in dif:
				print(palabra, end=' ')

		```
		
		Aquí hay algunos de los resultados para Emma:
		
		Palabras en el libro que no están en la lista de palabras:
		
		rencontre jane's blanche woodhouses disingenuousness
		friend's venice apartment ...

		Algunas de esas palabras son nombres y posesivos. 

		Otras, como “rencontre”, ya no son de uso común. 

		Sin embargo, ¡algunas son palabras comunes que realmente deberían estar en la lista!.

		Python proporciona una estructura de datos llamada 'set' que provee muchas operaciones de conjunto comunes.


	Palabras aleatorias:

		Para escoger una palabra de forma aleatoria del histograma, el algoritmo más simple es construir una lista con múltiples copias de cada palabra, según la frecuencia observada, y luego escoger de la lista:

		```
		def palabra_aleatoria(h):
			t = []
			for palabra, frec in h.items():
				t.extend([palabra] * frec)
			return random.choice(t)

		```

		La expresión [palabra] * frec crea una lista con frec copias de la cadena palabra. 

		El método 'extend' es similar a 'append', excepto que el argumento es una secuencia.

		Este algoritmo funciona, pero no es muy eficiente: cada vez que escoges una palabra aleatoria, reconstruye la lista, que es tan grande como el libro original. }

		Una mejora obvia es construir la lista una vez y luego hacer múltiples selecciones, pero la lista es grande aún.

		Una alternativa es:

		1. Utilizar 'keys' para obtener una lista de las palabras del libro.

		2. Construir una lista que contenga la suma acumulativa de las frecuencias de las palabras. 

		El último ítem en esta lista es el número total de palabras en el libro: n.

		3. Escoger un número de 1 a n. Utilizar búsqueda de bisección para encontrar el índice donde el número aleatorio sería insertado en la suma acumulativa.

		4. Utilizar el índice para encontrar la palabra correspondiente en la lista de palabras.



|| Depuración
	
	Cuando estés depurando un programa, y especialmente si estás trabajando en un error de programación difícil, hay cinco cosas para probar:


	Lectura: 

		Examina tu código, léelo de nuevo a ti mismo y verifica que dice lo que querías decir.


	Ejecución: 

		Experimenta haciendo cambios y ejecutando versiones diferentes. 
		
		A menudo, si muestras en pantalla lo correcto en el lugar correcto del programa, el problema se vuelve obvio, pero a veces tienes que construir andamiaje.


	Rumiación: 

		¡Tómate un tiempo para pensar! 

		¿Qué tipo de error es: 

			de sintaxis, de tiempo de ejecución o semántico?

 		¿Qué información puedes obtener a partir de los mensajes de error o de la salida del programa? 

 		¿Qué tipo de error podría causar el problema que estás viendo? 

		¿Qué cambiaste últimamente, antes de que el problema apareciera?

	
	Patito de goma: 

		Si le explicas el problema a alguien más, a veces encuentras la respuesta antes de terminar la pregunta. 

		A menudo no necesitas a la otra persona; podrías simplemente hablarle a un patito de goma. 

		Y ese es el origen de la conocida estrategia llamada método de depuración del patito de goma (en inglés, rubber duck debugging).


	Retroceso: 

		En algún punto, lo mejor que se puede hacer es retroceder, deshacer los cambios recientes, hasta que regreses a un programa que funcione y que entiendas. 

		Luego puedes comenzar a reconstruir.

		Los programadores principiantes a veces se atascan en una de estas actividades y olvidan las otras. 

		Cada actividad viene con su propio modo de fallo.

		Por ejemplo, leer tu código podría ayudar si el problema es un error tipográfico, pero no si el problema es un malentendido conceptual. 

		Si no entiendes lo que tu programa hace, puedes leerlo 100 veces y nunca ver el error, porque el error está en tu cabeza.

		Ejecutar experimentos puede ayudar, especialmente si ejecutas pruebas pequeñas y simples. 

		Pero si ejecutas experimentos sin pensar ni leer tu código, podrías caer en un patrón que yo llamo “programación de camino aleatorio”, que es el proceso de hacer cambios aleatorios hasta que el programa haga lo correcto.

		No hace falta decir que la programación de camino aleatorio puede tomar mucho tiempo.

		Tienes que tomarte el tiempo de pensar. 

		La depuración es como una ciencia experimental: deberías tener al menos una hipótesis acerca de cuál es el problema. 

		Si hay dos o más posibilidades, intenta pensar en una prueba que eliminaría una de ellas.

		Sin embargo, incluso las mejores técnicas de depuración fallarán si hay muchos errores, o si el código que intentas arreglar es muy grande y complicado.

		A veces la mejor opción es retroceder, simplificando el programa hasta que obtengas algo que funcione y que entiendas.

		Los programadores principiantes son a menudo reacios a retroceder porque no pueden soportar eliminar una línea de código (incluso si es incorrecta).

		Si te hace sentir mejor, copia tu programa en otro archivo antes de comenzar a recortarlo. 

		Luego puedes volver a copiar los pedazos uno a la vez.

		Encontrar un error de programación difícil requiere lectura, ejecución, rumiación y a veces retroceso. 

		Si te atascas en una de estas actividades, intenta las otras. 



|| Archivos

	Presenta la idea de programas “persistentes” que mantienen los datos en almacenamiento permanente y muestra cómo utilizar diferentes 'tipos de almacenamiento permanente', tales como 'archivos' y 'bases de datos'.


	Persistencia: 


		




