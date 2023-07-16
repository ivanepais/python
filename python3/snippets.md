# Ayuda rapida, info, anotaciones

|| PSEUDOCÓDIGO:

	Pensar como se crea o puede llegar a crear cada objeto.

	Las instrucciones (comandos, órdenes) basicas:
	
	entrada:

		Recibir datos del teclado, o un archivo u otro aparato.

	salida:

		Mostrar datos en el monitor o enviar datos a un archivo u otro aparato.

	matemáticas:

	 	Operaciones básicas de matemáticas como la adición y la multiplicación.

	operación condicional:

		Probar la veracidad de alguna condición y ejecutar una secuencia de instrucciones apropiada.

	repetición: 

		Ejecutar alguna acción repetidas veces, normalmente con alguna variación.


|| CREAR FUNCIONES:

	encapsular: 

		Meter el código que crea los objetos en las definiciones de función.


	generalizar:

		Crear variables genericas  en el cuerpo de la función, sin valores determinados para pasarles valores en la llamada.

		Así los objetos son diferentes en dimensiones, formas, aspecto, etc.


	diseño de interfaz:

		Explica como se utiliza la función: 

			¿cuáles son los parámetros? 

			¿Qué hace la función? 

			¿Y cuál es el valor de retorno? 

		Una interfaz es “limpia” si permite a la sentencia llamadora hacer lo que quiere sin lidiar con detalles innecesarios.		

	refactorización:

		Reorganizar un programa para mejorar las interfaces y facilitar la reutilización de código. 


	depuración:

		Corregir errores es programar.


			hipótesis:

				Con una hipostesis correcta podemos predecir comportamientos para modificar el programa y llegar a un resultado correcto o esperado.

				Hay que leer el código, entender cada línea para corregir los errores.


			flujo de ejecución:

				sentencias/def función > sentencias > llamada función (<< sentenc función) > sentencias.

				*leer flujo, no de inicio a fin.


|| PLAN DE DESARROLLO

	un proceso para escribir programas.

		Ej: “encapsulamiento y generalización”.

		1. Comenzar escribiendo un programa pequeño sin definiciones de función.

		2. Una vez que el programa funciona, identifica una parte coherente, encapsula la parte en una función y dale un nombre.

		3. Generaliza la función agregando parámetros apropiados.
	
		4. Repite los pasos 1–3 hasta que tengas un conjunto de funciones eficaces. Copia y pega código que funcione para evitar repetir (y volver a depurar).

		5. Busca oportunidades para mejorar el programa refactorizando. Por ejemplo, si tienes código similar en muchos lugares, considera factorizarlo dentro de una función
		general apropiada.


|| TÉCNICAS
	
	Paso a paso:

		Escribir las ideas que vamos aplicar en cada línea de código, paso a paso; antes de escribir una variable, función, etc.

		Esto nos dará una idea general sobre como empezar el programa.

		Dividir el programa en muchas funciones, cada una debería hacer una sola cosa.


	Abtraer problemas:

		Leer y pensar en el problema, sin programar.

		Hacer pruebas son entradas simples que nos de una salida esperada.

		Buscar patrones, escribir el algoritmo a alto nivel.

		Ir iterando cada vez más a bajo nivel.

		Una vez con la solución, encontrar cosas para mejorar, patrones para abstraer; herramientas del lenguaje que nos ayuden.

		No hay una sola posible solución, primero hacemos que funciones, despues lo hacemos legible.


	Autoevaluación:

		Cosas que no entendemos, Por qué es?, Qué conceptos están en juego? Que no los tenemos claro.

		Probar otras cosas y ver las consecuencias. Fallas en el razonamiento, Cuales? Por qué?

		Entender el tema, las operaciones, los pasos a seguir y ejecutarlos.


	Implementación avanzada:

		A veces resolvemos un problema pero que para un nivel inicial.

		Pero podemos usar conceptos avanzados: estructuras de control correctas, que el código sea eficiente (complejidad, orden de ejecución), código limpio, legible, modular, estructuras de datos.



|| BUENAS PRACTICAS:
	
	Escribir las variables, const, func y documentar en inglés.

	Crear formulas en variables para pasarselas a las funciones, metodos nativos o creadas, etc.

	import math, al inicio del programa.



|| INTERFAZ
	
	La interfaz de una función es un resumen de cómo esta se utiliza: 

		¿cuáles son los parámetros? 

		¿Qué hace la función? 

		¿Y cuál es el valor de retorno? 

	Es “limpia” si permite a la llamada hacer lo que quiere sin lidiar con detalles innecesarios.


|| ESTRUCTURA DE DATOS

	Se utilizan para organizar y almacenar información de manera eficiente.

		Cadena/String (cadena de caracter): 



		Vector/Matriz/Array (formación o matrix): 

			Es una cantidad de elementos en un orden específico, generalmente todos del mismo tipo (según el lenguaje, los elementos individuales pueden verse forzados a ser del mismo tipo o pueden ser de casi cualquier tipo).

			Pueden ser de longitud fija o de tamaño variable.


		Listas/List/Linked list: 

			Es una colección ordenada de elementos, donde cada elemento se identifica por un índice.

			Son versatiles y pueden contener elementos de diferentes tipos de datos. 

			Se utilizan para almacenar y manipular conjuntos de datos de manera flexible.

			La principal ventaja de una lista enlazada sobre una matriz es que los valores siempre se pueden insertar y eliminar de manera eficiente sin reubicar el resto de la lista.


		Tuplas/celdas/Tuple/record/estructure (registros o estructura/struct-structure/rows): 

			Es un valor que contiene otros valores, normalmente en un número y una secuencia fijos y normalmente indexados por nombres. Los elementos de los registros suelen denominarse campos o miembros (fields or members).

			Similares a las listas, pero son inmutables, no se pueden modificar después de su creación. 

			Se utilizan para almacenar un conjunto de valores relacionados y se accede a ellos mediante índices.


		Diccionario/hash table (vector asiciativo o mapa/hash): 

			Almacenan elementos como pares clave-valor. Cada elemento se identifica por una clave única y se puede acceder al valor correspondiente utilizando esa clave. 

			Utilizan una función hash para asignar claves a índices en una matriz, lo que permite un acceso en tiempo constante en el caso promedio.

			Son útiles cuando necesitas almacenar y recuperar datos de forma rápida y eficiente utilizando una clave personalizada. 

			Pueden ocurrir colisiones (collisions) de hash, lo que puede afectar su rendimiento. Se emplean técnicas como el encadenamiento y el direccionamiento (chaining and open addressing) abierto para manejar las colisiones.


		Conjuntos/sets:

			Es una colección desordenada de elementos únicos.

			Se utilizan cuando necesitas almacenar elementos sin duplicados y realizar operaciones como intersección, unión y diferencia de conjuntos de manera eficiente.


		Colas/queues: 

			Es una estructura de datos donde el primer elemento que se agrega es el primero en ser eliminado (FIFO: First-In, First-Out).

			Se utilizan para mantener un orden de elementos y son útiles en situaciones donde el orden de llegada es importante, como la gestión de tareas en un sistema.


		Pilas/Stacks: 

			Es una estructura de datos donde el último elemento que se agrega es el primero en ser eliminado (LIFO: Last-In, First-Out).

			Se utilizan para realizar operaciones como deshacer/rehacer, seguimiento de llamadas de funciones y otras situaciones en las que el último elemento agregado es el más relevante.


		Árboles/Trees: 

			Es una estructura de datos no lineal compuesta por nodos. Cada nodo puede tener cero o más nodos hijos.

			Se utilizan en muchas aplicaciones, como estructuras de búsqueda, representación de jerarquías y algoritmos de recorrido.


		Grafos/Graph: 

			Es una estructura de datos compuesta por vértices y aristas que conectan los vértices. 

			Los grafos se utilizan para representar relaciones y conexiones entre elementos.


		Clases/Class: 

			Es una plantilla para la creación de objetos de datos según un modelo predefinido. 

			Las clases se utilizan como representación abstracta de conceptos, incluyen campos como los registros y operaciones que pueden consultar el valor de los campos o cambiar sus valores.


	Python: 

		Tiene una jerarquía estandarizada de tipos de datos: 

		Es una estructura de clasificación o relación entre los diferentes tipos de datos disponibles en el lenguaje. 

		Se basa en la relación de herencia entre los tipos de datos y cómo se relacionan entre sí y comportamiento entre los diferentes tipos. 

		Además, esta jerarquía permite la conversión entre tipos, la realización de operaciones específicas de cada tipo y el uso de funciones y métodos comunes disponibles para los tipos de datos en cada nivel de la jerarquía.

		    1. Object (Objeto): La clase base de todos los objetos en Python. Todos los tipos de datos en Python son subclases directas o indirectas de la clase object. Proporciona métodos y funcionalidades comunes a todos los objetos, como __str__, __repr__, __eq__, etc.

		    2. Tipos numéricos: Python tiene varios tipos numéricos, incluyendo int (entero), float (coma flotante) y complex (complejo). Estos tipos están relacionados entre sí y se pueden convertir entre sí según las reglas de conversión definidas.

		    3. Tipos secuenciales: Los tipos de datos secuenciales incluyen str (cadena de caracteres), list (lista) y tuple (tupla). Estos tipos de datos se utilizan para almacenar y manipular conjuntos de valores ordenados.

		    4. Tipos de mapeo: El tipo de dato dict (diccionario) es un tipo de mapeo que almacena pares clave-valor. Los diccionarios se utilizan para asociar y acceder a valores utilizando una clave.

		    5. Tipos de conjuntos: Los tipos de datos de conjuntos incluyen set (conjunto) y frozenset (conjunto inmutable). Estos tipos de datos se utilizan para almacenar conjuntos de elementos únicos.


			Vacio/None: 

				None (class: Nonetype)


			Numeros/Numbers:  

				Enteros/Integral:

					Enteros/Integer (class: int)

					Booleanos/Booleans (class: bool)


				Reales/Real (class: float)


				Complejos/Complex (class: complex)


			Secuencias/Sequences: 

				Inmutables: 

					Strings (class: str) 

					Tuples/registros/rows/celdas (class: tuple)

					Bytes (class: bytes)

				Mutables: 

					List (class: list) 

					Bytes Arrays (class: bytearray)


			Conjuntos/Set types: 

				Sets (class: set)

				Frozen sets (class: frozenset)


			Diccionario/Mapas/Mappings (hash): 

				Dictionaries (class: dict)


			Llamadas/Callable: 

				Functions 

				Methods

				Classes


			Modulos/Modules


		Características: 

			Array/Vector/Matriz: 

				index -> elements 

				0 1 2 -> var, const, etc

				Indexación (index).
				Longitud/tamaño (length/size).
				Proceso de copiar (copying).

				Es bueno para: 
				
					Almacenar (storing) un número fijo de cosas y hacer algo con cada una de esas cosas. 

				Es malo para:
					
					Añadir o quitar elementos.
					Ordenar (sorting) cosas en muchos casos.
					Pensado para POO.


			Stack/Pila: 

				push() pop() -> elements

				característica:
					
					Pushing (entrada).
					Popping (salida).
					Size (tamaño).

				Es bueno para:
				
					Lidiar con un flujo de cosas que necesitan ser manejadas en ciertos grupos.

				Es malo para:

					Almacenamiento a largo plazo y acceso a conjuntos de datos complejos, al igual que apilar cosas de su piso no es un gran sistema de archivo.


			Linked list: 

				elements -> link -> elements

				característica:
					
					Obtener el siguiente elemento (get). 
					Insertar elemento (insert). 
					eliminar elemento (remove). 

				Es bueno para:

					Lidiar con una lista que cambia dinámicamente, es decir, donde puede necesitar insertar o eliminar elementos de cualquier parte de la lista.

				Es malo para:
					
					Es solo una lista. Casi siempre mejor que una matriz.

			Tree: 

				elements -> link -> child elements

				característica:
					
					Obtener "children"
					Insertar child
					Eliminar elemento

				Es bueno para:
					
					Almacenar cosas que pertenecen a los árboles
					crear conjuntos de datos de búsqueda rápida (es decir, árboles de decisión)

				Es malo para:
					
					Es solo una lista. Siempre será mejor que una matriz


		Ejemplos de estructuras de datos en python: 

			1. Listas: 

				Una lista es una colección ordenada y mutable de elementos. Puede contener elementos de diferentes tipos y se define utilizando corchetes ([]). Las listas permiten agregar, eliminar y modificar elementos.

				```python:

					# Definir una lista
					lista = ["manzana", "banana", "naranja"]

					# Acceder a elementos de la lista
					print(lista[0])  # Salida: "manzana"
					print(lista[2])  # Salida: "naranja"

					# Modificar un elemento de la lista
					lista[1] = "pera"
					print(lista)  # Salida: ["manzana", "pera", "naranja"]

					# Agregar elementos a la lista
					lista.append("uva")
					print(lista)  # Salida: ["manzana", "pera", "naranja", "uva"]

					# Eliminar elementos de la lista
					del lista[0]
					print(lista)  # Salida: ["pera", "naranja", "uva"]

					# Obtener la longitud de la lista
					print(len(lista))  # Salida: 3

					# Iterar sobre los elementos de la lista
					for fruta in lista:
					    print(fruta)

					# Comprobar si un elemento está presente en la lista
					print("banana" in lista)  # Salida: False

					# Ordenar la lista
					lista.sort()
					print(lista)  # Salida: ["naranja", "pera", "uva"]

					# Copiar una lista
					copia_lista = lista.copy()
					print(copia_lista)  # Salida: ["naranja", "pera", "uva"]

					# Concatenar listas
					lista2 = ["kiwi", "mango"]
					lista_concatenada = lista + lista2
					print(lista_concatenada)  # Salida: ["naranja", "pera", "uva", "kiwi", "mango"]

				```

				hemos creado una lista llamada lista que contiene tres elementos: "manzana", "banana" y "naranja". 
				Hemos demostrado cómo acceder a elementos individuales utilizando el índice, cómo modificar un elemento de la lista, cómo agregar elementos a la lista utilizando el método append, cómo eliminar elementos de la lista utilizando la instrucción del, cómo obtener la longitud de la lista utilizando la función len, cómo iterar sobre los elementos de la lista utilizando un bucle for, cómo comprobar la existencia de un elemento utilizando el operador in, cómo ordenar la lista utilizando el método sort, cómo copiar una lista utilizando el método copy, y cómo concatenar listas utilizando el operador +.


		   	2. Tuplas: 

		   		Una tupla es similar a una lista, pero es inmutable, lo que significa que no se pueden modificar después de su creación. Se definen utilizando paréntesis (()). Las tuplas se utilizan cuando se necesita una secuencia inmutable de elementos.

		   		

		   		```python:

		   			# Definir una tupla
					tupla = ("manzana", "banana", "naranja")

					# Acceder a elementos de la tupla
					print(tupla[0])  # Salida: "manzana"
					print(tupla[2])  # Salida: "naranja"

					# Intentar modificar un elemento de la tupla generará un error
					tupla[1] = "pera"  # Generará un error TypeError: 'tuple' object does not support item assignment

					# Obtener la longitud de la tupla
					print(len(tupla))  # Salida: 3

					# Iterar sobre los elementos de la tupla
					for fruta in tupla:
					    print(fruta)

					# Comprobar si un elemento está presente en la tupla
					print("banana" in tupla)  # Salida: True

					# Concatenar tuplas
					tupla2 = ("uva", "kiwi")
					tupla_concatenada = tupla + tupla2
					print(tupla_concatenada)  # Salida: ("manzana", "banana", "naranja", "uva", "kiwi")

					# Desempaquetar una tupla
					nombre, edad, ciudad = ("Juan", 30, "Madrid")
					print(nombre, edad, ciudad)  # Salida: "Juan 30 Madrid"

		   		```

		   		Este ejemplo contiene tres elementos: "manzana", "banana" y "naranja". Hemos demostrado cómo acceder a elementos individuales utilizando el índice, cómo obtener la longitud de la tupla utilizando la función len, cómo iterar sobre los elementos de la tupla utilizando un bucle for, y cómo comprobar la existencia de un elemento utilizando el operador in. Además, hemos demostrado cómo concatenar tuplas utilizando el operador + y cómo desempaquetar una tupla para asignar sus elementos a variables individuales.


		    3. Conjuntos: 

		    	Un conjunto es una colección desordenada de elementos únicos. No permite elementos duplicados y se define utilizando llaves ({}). Los conjuntos son útiles para operaciones de conjunto, como unión, intersección y diferencia.

		    	```python: 

		    		# Definir un conjunto (set)
					conjunto = {1, 2, 3, 4, 5}

					# Agregar elementos al conjunto
					conjunto.add(6)
					conjunto.add(7)

					# Mostrar el conjunto
					print(conjunto)  # Salida: {1, 2, 3, 4, 5, 6, 7}

					# Eliminar un elemento del conjunto
					conjunto.remove(3)

					# Verificar la existencia de un elemento en el conjunto
					print(4 in conjunto)  # Salida: True
					print(8 in conjunto)  # Salida: False

					# Obtener la longitud del conjunto
					print(len(conjunto))  # Salida: 6

					# Iterar sobre los elementos del conjunto
					for elemento in conjunto:
					    print(elemento)

					# Realizar operaciones de conjunto
					conjunto1 = {1, 2, 3}
					conjunto2 = {3, 4, 5}

					union = conjunto1.union(conjunto2)
					print(union)  # Salida: {1, 2, 3, 4, 5}

					interseccion = conjunto1.intersection(conjunto2)
					print(interseccion)  # Salida: {3}

					diferencia = conjunto1.difference(conjunto2)
					print(diferencia)  # Salida: {1, 2}

		    	```	

		    	En este ejemplo, hemos definido un conjunto (set) llamado conjunto que contiene los números del 1 al 7.

				Hemos demostrado cómo agregar elementos al conjunto utilizando el método add, cómo eliminar un elemento del conjunto utilizando el método remove, cómo verificar la existencia de un elemento en el conjunto utilizando el operador in, cómo obtener la longitud del conjunto utilizando la función len, y cómo iterar sobre los elementos del conjunto utilizando un bucle for.

				Además, hemos realizado algunas operaciones comunes de conjuntos. Hemos creado dos conjuntos adicionales, conjunto1 y conjunto2, y hemos utilizado los métodos union, intersection y difference para realizar operaciones de unión, intersección y diferencia entre ellos.

				Los conjuntos en Python son colecciones de elementos únicos y no ordenados. Se utilizan para almacenar y operar con conjuntos de elementos distintos. Los conjuntos proporcionan operaciones eficientes para realizar operaciones de conjuntos como uniones, intersecciones y diferencias.
		    	

		    4. Diccionarios: 

		    	Un diccionario es una estructura de datos que almacena pares clave-valor. Cada elemento del diccionario tiene una clave única asociada a un valor. Se definen utilizando llaves ({}). Los diccionarios permiten acceder, agregar y modificar elementos utilizando sus claves.

		    		



		    5. Cadenas de caracteres: 

		    	Una cadena es una secuencia de caracteres. En Python, las cadenas se representan entre comillas simples (') o comillas dobles ("). Las cadenas son inmutables y se utilizan para almacenar texto y manipularlo.

		    6. Pilas (Stacks): 

		    	Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out). Los elementos se agregan y eliminan solo desde el extremo superior de la pila. Puede implementarse utilizando una lista o mediante la clase "deque" del módulo 'collections'.

		    7. Colas (Queues): 

		    	Una cola es una estructura de datos que sigue el principio FIFO (First In, First Out). Los elementos se agregan al final de la cola y se eliminan desde el frente. Puede implementarse utilizando una lista o mediante la clase "deque" del módulo 'collections'.

		    8. Árboles: 

		    	Un árbol es una estructura de datos no lineal compuesta por nodos. Cada nodo puede tener cero o más nodos hijos. Los árboles se utilizan en muchas aplicaciones, como estructuras de búsqueda, representación de jerarquías y algoritmos de recorrido.

		    9. Grafos: 

		    	Un grafo es una estructura de datos compuesta por vértices y aristas que conectan los vértices. Los grafos se utilizan para representar relaciones y conexiones entre elementos.



		Estructuras de datos del modulo collections: 

			1. 
			2. 
			3. 





|| POO