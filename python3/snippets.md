# Pyton, ayuda rapida, info, anotaciones

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

		Crear variables genericas en el cuerpo de la función, sin valores determinados para pasarles valores en la llamada.

		Así los objetos son diferentes en dimensiones, formas, aspecto, etc.


	diseño de interfaz:

		Explica como se utiliza la función: 

			¿cuáles son los parámetros? 

			¿Qué hace la función? 

			¿Y cuál es el valor de retorno? 

		Una interfaz es “limpia” si permite a la sentencia llamadora hacer lo que quiere sin lidiar con detalles innecesarios.		

	refactorización:

		Reorganizar un programa para mejorar las interfaces y facilitar la reutilización de código. 


	Recursión: Las funciones pueden llamarse a sí mismas, lo que permite la implementación de algoritmos recursivos para problemas que se resuelven de manera iterativa.


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

		A veces resolvemos un problema pero que es para un nivel inicial.

		Pero podemos usar conceptos avanzados: estructuras de control correctas, que el código sea eficiente (complejidad, orden de ejecución), código limpio, legible, modular, estructuras de datos.


	Código complejo: 

		Desestructurarlo en partes más simples.

		Soluciones simples y escalables. Argumentarlas y justificarlas. 



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



|| OPERADORES
	
	Relacionales:

    	==: Comprueba si dos valores son iguales.

    	!=: Comprueba si dos valores son diferentes.

	    <: Comprueba si el valor de la izquierda es menor que el valor de la derecha.

	    >: Comprueba si el valor de la izquierda es mayor que el valor de la derecha.

	    <=: Comprueba si el valor de la izquierda es menor o igual que el valor de la derecha.

	    >=: Comprueba si el valor de la izquierda es mayor o igual que el valor de la derecha.

	    ```python:

	    	x = 10
			y = 5

			print(x == y)  # Salida: False
			print(x != y)  # Salida: True
			print(x < y)   # Salida: False
			print(x > y)   # Salida: True
			print(x <= y)  # Salida: False
			print(x >= y)  # Salida: True

	    ```

	Lógicos:

	    and: Devuelve True si ambas condiciones son verdaderas.
	    
	    or: Devuelve True si al menos una de las condiciones es verdadera.

	    not: Devuelve la negación de la condición.   


	"in": 

		Se utiliza para comprobar si un elemento está presente en una secuencia (como una lista, tupla, cadena o conjunto). 

		Si el elemento está presente, el operador devuelve True; de lo contrario, devuelve False.

		```python: 

			# Ejemplo con lista
			numeros = [1, 2, 3, 4, 5]
			print(3 in numeros)  # Salida: True
			print(6 in numeros)  # Salida: False

			# Ejemplo con cadena
			mensaje = "Hola, mundo"
			print("mundo" in mensaje)  # Salida: True
			print("python" in mensaje)  # Salida: False

		```

	"not in": 

		Es la negación del operador "in". Se utiliza para comprobar si un elemento NO está presente en una secuencia. Si el elemento NO está presente, el operador devuelve True; de lo contrario, devuelve False.

		```python:

			# Ejemplo con lista
			numeros = [1, 2, 3, 4, 5]
			print(6 not in numeros)  # Salida: True
			print(3 not in numeros)  # Salida: False

			# Ejemplo con cadena
			mensaje = "Hola, mundo"
			print("python" not in mensaje)  # Salida: True
			print("mundo" not in mensaje)  # Salida: False


		```




|| INSTRUCCIONES
	
	Son declaraciones que componen el código fuente del programa y le indican a Python qué acciones realizar.

	1. Asignación: 

		Permiten asignar un valor a una variable. Se utilizan para crear y actualizar variables en Python.

		```python: 

			x = 10
			
			nombre = "Juan"

		```


	2. Control de flujo: 

		Permiten controlar el flujo de ejecución del programa y tomar decisiones basadas en condiciones.

		"if": 

			Se utiliza para ejecutar un bloque de código si se cumple una condición.

			```python: 

				edad = 25
				if edad >= 18:
				    print("Eres mayor de edad")

			```

		"else": 

			Se utiliza junto con "if" para ejecutar un bloque de código si la condición no se cumple.

			```python: 

				edad = 15

				if edad >= 18:
				    print("Eres mayor de edad")

				else:
				    print("Eres menor de edad")
								
			```

		"elif": 

			Se utiliza para evaluar múltiples condiciones.

			```python: 

				puntaje = 85

				if puntaje >= 90:
				    print("A")

				elif puntaje >= 80:
				    print("B")

				else:
				    print("C")

			```

		"while": 

			Se utiliza para crear un bucle que se ejecuta mientras se cumpla una condición.

			```python: 

				contador = 1

				while contador <= 5:
				    print(contador)
				    contador += 1

			```

		"for": 

			Se utiliza para iterar sobre una secuencia (por ejemplo, listas, tuplas, diccionarios).

			```python: 

				frutas = ["manzana", "banana", "cereza"]

				for fruta in frutas:
				    print(fruta)

			```


	3. Funciones: 

		Permiten definir funciones, que son bloques de código que pueden ser llamados varias veces en el programa.

		```python: 

			def saludar(nombre):
			    print("Hola, " + nombre)

			saludar("Juan")

		```


	4. "try-except": 

		Se utiliza para manejar excepciones (errores) que puedan ocurrir durante la ejecución del programa.

		```python: 

			try:
		    resultado = 10 / 0

			except ZeroDivisionError:
		   		print("Error: No se puede dividir entre cero")

		```	


	5. "import": 

		Se utiliza para importar módulos y bibliotecas en Python.

		```python: 

			import math

			raiz_cuadrada = math.sqrt(25)

		```


	6. "return": 

		Se utiliza para devolver un valor desde una función.

		```python: 

			def suma(a, b):
			    return a + b

			resultado = suma(3, 5)  # resultado será igual a 8

		``` 


|| Métodos (=/= fx nativ ^ =/= clases)
	
	Son funciones que se aplican a objetos y realizan operaciones específicas en esos objetos. 

	Cada tipo de dato en Python puede tener sus propios métodos que se utilizan para realizar acciones específicas relacionadas con ese tipo de dato. Los métodos se invocan utilizando la sintaxis de punto, es decir, objeto.metodo().

	
	1. listas:

        append(): Agrega un elemento al final de la lista.

        insert(): Inserta un elemento en una posición específica de la lista.

        remove(): Elimina la primera aparición de un elemento de la lista.

        pop(): Elimina y devuelve el último elemento de la lista (o un índice específico).

        sort(): Ordena la lista en orden ascendente.

        reverse(): Invierte el orden de los elementos en la lista.


    2. Cadenas (strings):

        upper(): Devuelve una copia de la cadena en mayúsculas.

        lower(): Devuelve una copia de la cadena en minúsculas.

        capitalize(): Devuelve una copia de la cadena con el primer carácter en mayúscula.

        count(): Cuenta cuántas veces aparece un subconjunto de caracteres en la cadena.

        split(): Divide la cadena en una lista de subcadenas utilizando un separador específico.


    3. Diccionarios:

        keys(): Devuelve una vista de las claves del diccionario.

        values(): Devuelve una vista de los valores del diccionario.

        items(): Devuelve una vista de los pares clave-valor del diccionario.

        get(): Devuelve el valor asociado con una clave, o un valor predeterminado si la clave no está presente.


   4. Conjuntos (sets):

        add(): Agrega un elemento al conjunto.

        remove(): Elimina un elemento del conjunto. Si el elemento no existe, se produce un error.

        discard(): Elimina un elemento del conjunto. Si el elemento no existe, no se produce un error.

        union(): Devuelve la unión de dos conjuntos.

        intersection(): Devuelve la intersección de dos conjuntos.


    5. Matemáticos:

        abs(): Devuelve el valor absoluto de un número.

        round(): Redondea un número a un número entero o con un número específico de decimales.

        max(): Devuelve el valor más grande de una secuencia.

        min(): Devuelve el valor más pequeño de una secuencia.
	

|| Funciones nativas 
	
	Las funciones integradas, incorporadas, predefinidas o internas son parte del lenguaje Python y están disponibles para su uso directamente sin necesidad de importar ningún módulo adicional.

	1. Funciones de entrada/salida:

    	print(): Imprime un mensaje en la consola.

    	input(): Lee una entrada del usuario desde la consola.

    	```python: 

    		nombre = input("Ingrese su nombre: ")

			print("Hola, " + nombre)

    	```

    2. Funciones de conversión de tipos de datos:

    	int(): Convierte un valor a un número entero.

	    float(): Convierte un valor a un número de punto flotante (decimal).

	    str(): Convierte un valor a una cadena de texto.

	    list(): Convierte un valor a una lista.

	    tuple(): Convierte un valor a una tupla.

	    ```python: 

	    	numero_texto = "10"
			numero_entero = int(numero_texto)
			print(numero_entero)  # Salida: 10
			
			pi = 3.14159
			pi_texto = str(pi)
			print("El valor de pi es: " + pi_texto)  # Salida: El valor de pi es: 3.14159

	    ```

	3. Funciones matemáticas:

	    abs(): Devuelve el valor absoluto de un número.

	    round(): Redondea un número a un número entero o con un número específico de decimales.

	    max(): Devuelve el valor más grande de una secuencia.

	    min(): Devuelve el valor más pequeño de una secuencia.

	    ```python: 

	    	numero = -5
			absoluto = abs(numero)
			print(absoluto)  # Salida: 5

			decimal = 3.14159
			redondeado = round(decimal, 2)
			print(redondeado)  # Salida: 3.14

	    ```

	4. Funciones de secuencias:

   		len(): Devuelve la longitud de una secuencia (cadena, lista, tupla, etc.).

    	range(): Genera una secuencia de números enteros.

    	```python: 

    		texto = "Hola, mundo"
			longitud = len(texto)
			print(longitud)  # Salida: 12

			numeros = list(range(1, 6))
			print(numeros)  # Salida: [1, 2, 3, 4, 5]

    	```

   	5. Funciones de manejo de listas:

    	sorted(): Ordena una lista.

    	sum(): Devuelve la suma de los elementos de una lista.

    	```python: 

    		numeros = [5, 2, 8, 3, 1]
			numeros_ordenados = sorted(numeros)
			print(numeros_ordenados)  # Salida: [1, 2, 3, 5, 8]

			suma = sum(numeros)
			print(suma)  # Salida: 19

    	```



|| ESTRUCTURAS DE CONTROL
	
	Son componentes que permiten controlar el flujo de ejecución de un programa.

	Determinan el orden en que se ejecutan las instrucciones y permiten tomar decisiones y repetir acciones según ciertas condiciones.

	1. if-else (si, entonces): 

		Permite tomar decisiones en base a una condición. 

		Si la condición es verdadera, se ejecuta un bloque de código; de lo contrario, se ejecuta otro bloque de código.

		```python:

			if condicion:
			    # Bloque de código si la condición es verdadera
			else:
			    # Bloque de código si la condición es falsa

		```

	2. "for" (para):

		Se utiliza para iterar sobre una secuencia de elementos (como una lista, tupla, cadena -tipos de secuencia en python-.) y ejecutar un bloque de código para cada elemento.

		```python: 

			for elemento in secuencia:
    			# Bloque de código a ejecutar para cada elemento

		```

	3. "while" (mientras):
			
		Permite repetir la ejecución de un bloque de código mientras una condición sea verdadera.

		```python: 

			while condicion:
    			# Bloque de código a repetir mientras la condición sea verdadera

		```

	4. "break":
		
		Se utiliza para salir de un bucle de manera prematura cuando se cumple una condición.

		```python:

			for elemento in secuencia:
   			if condicion:
        		break

		```

	5. "continue":
		
		Se utiliza para saltar la ejecución de una iteración en un bucle y pasar a la siguiente iteración.

		```python: 

			for elemento in secuencia:
		    if condicion:
		        continue
		    # Resto del código para la iteración actual

		```

	Ejemplos: 

		1. if-else: 	

			```python: 

				# Ejemplo 1: Verificar si un número es par o impar
				numero = 10

				if numero % 2 == 0:
				    print("El número es par")
				else:
				    print("El número es impar")

				# Salida: El número es par

				# Ejemplo 2: Calificar el rendimiento de un estudiante
				puntaje = 85

				if puntaje >= 90:
				    calificacion = "A"
				elif puntaje >= 80:
				    calificacion = "B"
				elif puntaje >= 70:
				    calificacion = "C"
				elif puntaje >= 60:
				    calificacion = "D"
				else:
				    calificacion = "F"

				print("La calificación es:", calificacion)

				# Salida: La calificación es: B

				# Ejemplo 3: Verificar si una cadena es una vocal o una consonante
				letra = "a"

				if letra.lower() in "aeiou":
				    print("Es una vocal")
				else:
				    print("Es una consonante")

				# Salida: Es una vocal

			```

			En el primer ejemplo, verificamos si un número es par o impar utilizando el operador de módulo (%). Si el resto de la división del número entre 2 es 0, entonces es par; de lo contrario, es impar.

			En el segundo ejemplo, calificamos el rendimiento de un estudiante según su puntaje. Utilizamos múltiples bloques "if-elif-else" para evaluar diferentes condiciones y asignar una calificación correspondiente en función del rango de puntajes.

			En el tercer ejemplo, verificamos si una letra es una vocal o una consonante. Utilizamos el método lower() para convertir la letra a minúscula y luego verificamos si está presente en el conjunto de vocales. Si es así, se imprime que es una vocal; de lo contrario, se imprime que es una consonante.

			Estos ejemplos ilustran cómo utilizar la estructura de control "if-else" para tomar decisiones en base a condiciones y ejecutar diferentes bloques de código en función de los resultados. La estructura "if-else" es una herramienta poderosa para implementar lógica condicional en un programa y permitir que el programa tome diferentes caminos según las condiciones evaluadas.


		2. for: 

			```python: 

				# Ejemplo 1: Iterar sobre una lista
				numeros = [1, 2, 3, 4, 5]

				for numero in numeros:
				    print(numero)

				# Salida:
				# 1
				# 2
				# 3
				# 4
				# 5

				# Ejemplo 2: Iterar sobre una cadena de texto
				mensaje = "Hola, mundo!"

				for caracter in mensaje:
				    print(caracter)

				# Salida:
				# H
				# o
				# l
				# a
				# ,
				#  
				# m
				# u
				# n
				# d
				# o
				# !

				# Ejemplo 3: Iterar sobre un rango de números
				for i in range(1, 6):
				    print(i)

				# Salida:
				# 1
				# 2
				# 3
				# 4
				# 5

				# Ejemplo 4: Utilizar la función enumerate para obtener índices y valores
				frutas = ["manzana", "banana", "cereza"]

				for indice, fruta in enumerate(frutas):
				    print(f"Índice: {indice}, Fruta: {fruta}")

				# Salida:
				# Índice: 0, Fruta: manzana
				# Índice: 1, Fruta: banana
				# Índice: 2, Fruta: cereza

				# Ejemplo 5: Utilizar la estructura "for-else" para buscar un elemento
				numeros = [1, 2, 3, 4, 5]
				buscar = 6

				for numero in numeros:
				    if numero == buscar:
				        print("Número encontrado")
				        break
				else:
				    print("Número no encontrado")

				# Salida: Número no encontrado

			```

			En el primer ejemplo, utilizamos la estructura "for" para iterar sobre una lista de números. En cada iteración, el valor actual se asigna a la variable "numero" y se imprime.

			En el segundo ejemplo, iteramos sobre una cadena de texto, y en cada iteración, se asigna un caracter a la variable "caracter" y se imprime.

			En el tercer ejemplo, utilizamos la función "range" para generar un rango de números del 1 al 5, y luego iteramos sobre ese rango. En cada iteración, el valor actual se asigna a la variable "i" y se imprime.

			En el cuarto ejemplo, utilizamos la función "enumerate" para obtener tanto los índices como los valores de una lista. En cada iteración, la función "enumerate" devuelve una tupla con el índice y el valor correspondiente, que se desempaqueta en las variables "indice" y "fruta" respectivamente, y se imprime.

			En el quinto ejemplo, utilizamos la estructura "for-else" para buscar un elemento en una lista. Si el elemento se encuentra, se imprime "Número encontrado" y se sale del bucle usando "break". Si el bucle se ejecuta hasta el final sin encontrar el número, se ejecuta el bloque "else" y se imprime "Número no encontrado".

			Estos ejemplos demuestran algunas de las aplicaciones de la estructura de control "for" en Python. Esta estructura es muy útil para iterar sobre secuencias de elementos como listas, cadenas, rangos, entre otros. Puedes utilizarla para realizar operaciones en cada elemento de una secuencia, procesar datos, buscar elementos, generar secuencias numéricas y mucho más.


		3. while:

			```python:

				# Ejemplo 1: Contador descendente
				contador = 5

				while contador > 0:
				    print(contador)
				    contador -= 1

				# Salida:
				# 5
				# 4
				# 3
				# 2
				# 1

				# Ejemplo 2: Suma acumulativa
				suma = 0
				numero = 1

				while numero <= 10:
				    suma += numero
				    numero += 1

				print("La suma es:", suma)  # Salida: La suma es: 55

				# Ejemplo 3: Búsqueda de un elemento en una lista
				numeros = [4, 6, 2, 8, 5]
				buscar = 6
				encontrado = False
				indice = 0

				while indice < len(numeros):
				    if numeros[indice] == buscar:
				        encontrado = True
				        break
				    indice += 1

				if encontrado:
				    print("Número encontrado")
				else:
				    print("Número no encontrado")

				# Salida: Número encontrado

				# Ejemplo 4: Validación de entrada de usuario
				contrasena_correcta = "abc123"
				contrasena = input("Ingrese la contraseña: ")

				while contrasena != contrasena_correcta:
				    print("Contraseña incorrecta. Inténtelo nuevamente.")
				    contrasena = input("Ingrese la contraseña: ")

				print("Contraseña correcta. Acceso concedido.")

				# Salida:
				# Ingrese la contraseña: 123
				# Contraseña incorrecta. Inténtelo nuevamente.
				# Ingrese la contraseña: abc123
				# Contraseña correcta. Acceso concedido.

			```

			En el primer ejemplo, utilizamos la estructura "while" para crear un contador descendente. Mientras el contador sea mayor que 0, se imprime su valor y se decrementa en cada iteración.

			En el segundo ejemplo, utilizamos el "while" para realizar una suma acumulativa. Mientras el número sea menor o igual a 10, se suma al total acumulado y se incrementa en cada iteración. Al final, se imprime el resultado de la suma.

			En el tercer ejemplo, utilizamos el "while" para buscar un elemento en una lista. Mientras el índice sea menor que la longitud de la lista, se verifica si el elemento en esa posición coincide con el valor buscado. Si se encuentra, se establece la variable "encontrado" como True y se sale del bucle usando "break".

			En el cuarto ejemplo, utilizamos el "while" para validar la entrada de una contraseña. Mientras la contraseña ingresada por el usuario no coincida con la contraseña correcta, se muestra un mensaje de error y se solicita nuevamente la contraseña. Una vez que se ingresa la contraseña correcta, se imprime un mensaje de acceso concedido.

			La estructura de control "while" es útil cuando se necesita repetir un bloque de código mientras se cumpla una condición. Puedes usarla para realizar operaciones iterativas, contar o decrementar valores, buscar elementos en una lista, validar entradas de usuario y mucho más. Recuerda asegurarte de que la condición cambie en algún momento para evitar bucles infinitos.


		4. break: 

			```python: 

				# Ejemplo 1: Búsqueda de un elemento en una lista
				numeros = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
				buscar = 6

				for numero in numeros:
				    if numero == buscar:
				        print("Número encontrado")
				        break

				# Salida: Número encontrado

				# Ejemplo 2: Salida anticipada de un bucle infinito
				while True:
				    respuesta = input("¿Quieres salir? (s/n): ")

				    if respuesta.lower() == "s":
				        print("Saliendo del bucle...")
				        break

				# Salida:
				# ¿Quieres salir? (s/n): n
				# ¿Quieres salir? (s/n): n
				# ¿Quieres salir? (s/n): s
				# Saliendo del bucle...

			```	

			En el primer ejemplo, utilizamos la estructura "for" para buscar un elemento en una lista. En cada iteración, comparamos el número actual con el valor buscado. Si encontramos una coincidencia, imprimimos un mensaje y salimos del bucle utilizando la sentencia "break". Esto evita que el bucle continúe iterando innecesariamente una vez que se ha encontrado el número buscado.

			En el segundo ejemplo, utilizamos un bucle "while True" para crear un bucle infinito. Solicitamos al usuario que ingrese una respuesta ("s" o "n") y, si la respuesta es "s", imprimimos un mensaje y salimos del bucle usando "break". Esto nos permite tener un bucle infinito hasta que el usuario decida salir ingresando "s".

			La sentencia "break" es utilizada para salir de un bucle de manera prematura. Se puede utilizar en cualquier estructura de control de bucle (como "for" y "while") para detener la ejecución del bucle y continuar con el código que sigue después del bucle. La principal utilidad de "break" es evitar que el bucle continúe ejecutándose una vez que se ha cumplido una condición o se ha alcanzado un resultado deseado.


		5. continue: 

			```python: 

				# Ejemplo 1: Imprimir solo los números pares
				numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

				for numero in numeros:
				    if numero % 2 != 0:
				        continue
				    print(numero)

				# Salida:
				# 2
				# 4
				# 6
				# 8
				# 10

				# Ejemplo 2: Saltear una iteración en un bucle while
				contador = 0

				while contador < 5:
				    contador += 1
				    if contador == 3:
				        continue
				    print(contador)

				# Salida:
				# 1
				# 2
				# 4
				# 5

			```

			En el primer ejemplo, utilizamos la estructura "for" para iterar sobre una lista de números. Usando la sentencia "continue", verificamos si el número es impar. Si es así, se salta la iteración actual y pasa a la siguiente iteración sin ejecutar el código que sigue después del "continue". Esto nos permite imprimir solo los números pares en este caso.

			En el segundo ejemplo, utilizamos un bucle "while" para contar hasta 5. Usando la sentencia "continue", verificamos si el contador es igual a 3. Si es así, se salta la iteración actual y pasa a la siguiente iteración sin imprimir el valor actual del contador. Esto nos permite saltar la iteración cuando el contador es 3.

			La sentencia "continue" se utiliza para saltar la ejecución de una iteración en un bucle y pasar a la siguiente iteración. Puede ser útil cuando se desea omitir ciertas iteraciones según una condición específica, evitando que se ejecuten ciertas líneas de código en esas iteraciones particulares.




|| ESTRUCTURAS DE DATOS

	Se utilizan para organizar y almacenar información de manera eficiente.

		Cadena/String (cadena de caracter): 

			Una cadena es una secuencia de caracteres. En Python, las cadenas se representan entre comillas simples (') o comillas dobles ("). Las cadenas son inmutables y se utilizan para almacenar texto y manipularlo.


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

				Las listas en Python son estructuras de datos versátiles que permiten almacenar y manipular conjuntos ordenados de elementos. Son mutables, lo que significa que se pueden modificar después de su creación. Las listas son útiles para almacenar colecciones de elementos que pueden cambiar en tamaño o contenido a lo largo del programa.


		   	2. Tuplas/registros/rows/celdas: 

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

		   		Las tuplas son secuencias inmutables en Python, lo que significa que no se pueden modificar después de su creación. Sin embargo, permiten acceder a elementos individuales, realizar iteraciones y otras operaciones básicas. Son útiles cuando se necesita almacenar un conjunto de valores que no cambiarán a lo largo del programa, como coordenadas, días de la semana, información de un punto de datos fijo, entre otros.


		    3. Conjuntos/set: 

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
		    	

		    4. Diccionarios/Mapa/Hash: 

		    	Un diccionario es una estructura de datos que almacena pares clave-valor. Cada elemento del diccionario tiene una clave única asociada a un valor. Se definen utilizando llaves ({}). Los diccionarios permiten acceder, agregar y modificar elementos utilizando sus claves.

		    	```python: 

		    		# Definir un diccionario
					diccionario = {
					    "nombre": "Juan",
					    "edad": 30,
					    "ciudad": "Madrid"
					}

					# Acceder a valores utilizando claves
					print(diccionario["nombre"])  # Salida: "Juan"
					print(diccionario["edad"])  # Salida: 30

					# Modificar valores en el diccionario
					diccionario["edad"] = 31
					print(diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}

					# Agregar nuevos pares clave-valor al diccionario
					diccionario["profesion"] = "Ingeniero"
					print(diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

					# Eliminar un par clave-valor del diccionario
					del diccionario["ciudad"]
					print(diccionario)  # Salida: {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero'}

					# Obtener todas las claves del diccionario
					claves = diccionario.keys()
					print(claves)  # Salida: dict_keys(['nombre', 'edad', 'profesion'])

					# Obtener todos los valores del diccionario
					valores = diccionario.values()
					print(valores)  # Salida: dict_values(['Juan', 31, 'Ingeniero'])

					# Verificar la existencia de una clave en el diccionario
					print("edad" in diccionario)  # Salida: True
					print("ciudad" in diccionario)  # Salida: False

					# Obtener la longitud del diccionario
					print(len(diccionario))  # Salida: 3

					# Iterar sobre las claves y valores del diccionario
					for clave, valor in diccionario.items():
					    print(clave + ":", valor)

		    	```

		    	En este ejemplo, hemos definido un diccionario llamado diccionario que contiene información sobre una persona. Las claves del diccionario son "nombre", "edad" y "ciudad", y los valores correspondientes son "Juan", 30 y "Madrid", respectivamente.

				Hemos demostrado cómo acceder a los valores utilizando las claves, cómo modificar los valores en el diccionario, cómo agregar nuevos pares clave-valor, cómo eliminar un par clave-valor utilizando la instrucción del, cómo obtener las claves y valores del diccionario utilizando los métodos keys y values, cómo verificar la existencia de una clave en el diccionario utilizando el operador in, cómo obtener la longitud del diccionario utilizando la función len, y cómo iterar sobre las claves y valores del diccionario utilizando un bucle for y el método items.

				Los diccionarios en Python son estructuras de datos que permiten almacenar pares de claves y valores. Son útiles para asociar y acceder a información de manera eficiente. Los diccionarios se utilizan ampliamente para representar estructuras de datos como bases de datos en memoria, configuraciones, datos JSON, entre otros.


		    5. Cadenas de caracteres: 

		    	Una cadena es una secuencia de caracteres. En Python, las cadenas se representan entre comillas simples (') o comillas dobles ("). Las cadenas son inmutables y se utilizan para almacenar texto y manipularlo.

		    	```python: 

		    		# Definir una cadena de caracteres
					cadena = "Hola, mundo!"

					# Acceder a caracteres individuales
					print(cadena[0])  # Salida: "H"
					print(cadena[7])  # Salida: "u"

					# Obtener la longitud de la cadena
					print(len(cadena))  # Salida: 12

					# Reemplazar parte de la cadena
					cadena_modificada = cadena.replace("mundo", "Python")
					print(cadena_modificada)  # Salida: "Hola, Python!"

					# Concatenar cadenas
					saludo = "Hola"
					nombre = "Juan"
					mensaje = saludo + ", " + nombre + "!"
					print(mensaje)  # Salida: "Hola, Juan!"

					# Iterar sobre los caracteres de la cadena
					for caracter in cadena:
					    print(caracter)

					# Comprobar si una subcadena está presente en la cadena
					print("mundo" in cadena)  # Salida: True

					# Convertir la cadena en mayúsculas
					cadena_mayusculas = cadena.upper()
					print(cadena_mayusculas)  # Salida: "HOLA, MUNDO!"

					# Convertir la cadena en minúsculas
					cadena_minusculas = cadena.lower()
					print(cadena_minusculas)  # Salida: "hola, mundo!"

					# Dividir la cadena en una lista de palabras
					palabras = cadena.split()
					print(palabras)  # Salida: ["Hola,", "mundo!"]

		    	```

		    	En este ejemplo, hemos definido una cadena de caracteres utilizando comillas dobles. La cadena contiene el texto "Hola, mundo!".

				Hemos demostrado cómo acceder a caracteres individuales utilizando el índice, cómo obtener la longitud de la cadena utilizando la función len, cómo reemplazar parte de la cadena utilizando el método replace, cómo concatenar cadenas utilizando el operador +, cómo iterar sobre los caracteres de la cadena utilizando un bucle for, cómo comprobar la existencia de una subcadena utilizando el operador in, cómo convertir la cadena en mayúsculas o minúsculas utilizando los métodos upper y lower, y cómo dividir la cadena en una lista de palabras utilizando el método split.

				Las cadenas de caracteres en Python son secuencias de caracteres inmutables. Se utilizan para almacenar y manipular texto en un programa. Son ampliamente utilizadas en la manipulación de texto, la entrada y salida de datos, el formateo de cadenas y muchas otras tareas relacionadas con el procesamiento de texto.


		    6. Pilas (Stacks): 

		    	Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out). Los elementos se agregan y eliminan solo desde el extremo superior de la pila. Puede implementarse utilizando una lista o mediante la clase "deque" del módulo 'collections'.

		    	```python: 

		    		class Pila:
					    def __init__(self):
					        self.items = []

					    def esta_vacia(self):
					        """
					        Verifica si la pila está vacía.
					        """
					        return len(self.items) == 0

					    def apilar(self, elemento):
					        """
					        Agrega un elemento a la pila.
					        """
					        self.items.append(elemento)

					    def desapilar(self):
					        """
					        Elimina y devuelve el elemento en la parte superior de la pila.
					        """
					        if not self.esta_vacia():
					            return self.items.pop()

					    def ver_tope(self):
					        """
					        Devuelve el elemento en la parte superior de la pila sin eliminarlo.
					        """
					        if not self.esta_vacia():
					            return self.items[-1]

					    def tamano(self):
					        """
					        Devuelve el número de elementos en la pila.
					        """
					        return len(self.items)


					# Crear una instancia de la clase Pila
					pila = Pila()

					# Verificar si la pila está vacía
					print(pila.esta_vacia())  # Salida: True

					# Apilar elementos en la pila
					pila.apilar(10)
					pila.apilar(20)
					pila.apilar(30)

					# Verificar el tamaño de la pila
					print(pila.tamano())  # Salida: 3

					# Ver el elemento en la parte superior de la pila
					print(pila.ver_tope())  # Salida: 30

					# Desapilar elementos de la pila
					elemento = pila.desapilar()
					print(elemento)  # Salida: 30

					# Verificar el tamaño de la pila nuevamente
					print(pila.tamano())  # Salida: 2

		    	```

		    	En este ejemplo, hemos implementado una pila utilizando una clase llamada Pila. La pila se basa en una lista (self.items) que almacena los elementos.

				Hemos definido métodos como esta_vacia() para verificar si la pila está vacía, apilar() para agregar elementos a la pila, desapilar() para eliminar y devolver el elemento en la parte superior de la pila, ver_tope() para obtener el elemento en la parte superior de la pila sin eliminarlo, y tamano() para obtener el número de elementos en la pila.

				Luego, hemos creado una instancia de la clase Pila llamada pila y hemos realizado varias operaciones con ella. Hemos verificado si la pila está vacía, apilado elementos, obtenido el tamaño de la pila, obtenido el elemento en la parte superior de la pila, y desapilado elementos.

				La pila es una estructura de datos que sigue el principio LIFO (Last In, First Out), lo que significa que el último elemento que se apila es el primero en ser desapilado. Se utiliza ampliamente en diferentes áreas de la programación, como la evaluación de expresiones matemáticas, el manejo de llamadas a funciones y la inversión de cadenas.


		    7. Colas (Queues): 

		    	Una cola es una estructura de datos que sigue el principio FIFO (First In, First Out). Los elementos se agregan al final de la cola y se eliminan desde el frente. Puede implementarse utilizando una lista o mediante la clase "deque" del módulo 'collections'.


		    	```python: 

		    		class Cola:
					    def __init__(self):
					        self.items = []

					    def esta_vacia(self):
					        """
					        Verifica si la cola está vacía.
					        """
					        return len(self.items) == 0

					    def encolar(self, elemento):
					        """
					        Agrega un elemento a la cola.
					        """
					        self.items.append(elemento)

					    def desencolar(self):
					        """
					        Elimina y devuelve el elemento en el frente de la cola.
					        """
					        if not self.esta_vacia():
					            return self.items.pop(0)

					    def ver_frente(self):
					        """
					        Devuelve el elemento en el frente de la cola sin eliminarlo.
					        """
					        if not self.esta_vacia():
					            return self.items[0]

					    def tamano(self):
					        """
					        Devuelve el número de elementos en la cola.
					        """
					        return len(self.items)


					# Crear una instancia de la clase Cola
					cola = Cola()

					# Verificar si la cola está vacía
					print(cola.esta_vacia())  # Salida: True

					# Encolar elementos en la cola
					cola.encolar(10)
					cola.encolar(20)
					cola.encolar(30)

					# Verificar el tamaño de la cola
					print(cola.tamano())  # Salida: 3

					# Ver el elemento en el frente de la cola
					print(cola.ver_frente())  # Salida: 10

					# Desencolar elementos de la cola
					elemento = cola.desencolar()
					print(elemento)  # Salida: 10

					# Verificar el tamaño de la cola nuevamente
					print(cola.tamano())  # Salida: 2

		    	```

		    	En este ejemplo, hemos implementado una cola utilizando una clase llamada Cola. La cola se basa en una lista (self.items) que almacena los elementos.

				Hemos definido métodos como esta_vacia() para verificar si la cola está vacía, encolar() para agregar elementos a la cola, desencolar() para eliminar y devolver el elemento en el frente de la cola, ver_frente() para obtener el elemento en el frente de la cola sin eliminarlo, y tamano() para obtener el número de elementos en la cola.

				Luego, hemos creado una instancia de la clase Cola llamada cola y hemos realizado varias operaciones con ella. Hemos verificado si la cola está vacía, encolado elementos, obtenido el tamaño de la cola, obtenido el elemento en el frente de la cola y desencolado elementos.

				La cola es una estructura de datos que sigue el principio FIFO (First In, First Out), lo que significa que el primer elemento que se encola es el primero en ser desencolado. Se utiliza ampliamente en diferentes áreas de la programación, como el manejo de tareas pendientes, la implementación de algoritmos de búsqueda y el procesamiento de mensajes en sistemas distribuidos.


		    8. Árboles: 

		    	Un árbol es una estructura de datos no lineal compuesta por nodos. Cada nodo puede tener cero o más nodos hijos. Los árboles se utilizan en muchas aplicaciones, como estructuras de búsqueda, representación de jerarquías y algoritmos de recorrido.

		    	```python: 

		    		class Nodo:
					    def __init__(self, valor):
					        self.valor = valor
					        self.izquierda = None
					        self.derecha = None

					class ArbolBinarioBusqueda:
					    def __init__(self):
					        self.raiz = None

					    def insertar(self, valor):
					        """
					        Inserta un valor en el árbol binario de búsqueda.
					        """
					        if self.raiz is None:
					            self.raiz = Nodo(valor)
					        else:
					            self._insertar_recursivo(valor, self.raiz)

					    def _insertar_recursivo(self, valor, nodo_actual):
					        if valor < nodo_actual.valor:
					            if nodo_actual.izquierda is None:
					                nodo_actual.izquierda = Nodo(valor)
					            else:
					                self._insertar_recursivo(valor, nodo_actual.izquierda)
					        elif valor > nodo_actual.valor:
					            if nodo_actual.derecha is None:
					                nodo_actual.derecha = Nodo(valor)
					            else:
					                self._insertar_recursivo(valor, nodo_actual.derecha)
					        else:
					            # Valor duplicado, se ignora
					            pass

					    def buscar(self, valor):
					        """
					        Busca un valor en el árbol binario de búsqueda.
					        Devuelve True si se encuentra, False en caso contrario.
					        """
					        return self._buscar_recursivo(valor, self.raiz)

					    def _buscar_recursivo(self, valor, nodo_actual):
					        if nodo_actual is None:
					            return False
					        elif valor == nodo_actual.valor:
					            return True
					        elif valor < nodo_actual.valor:
					            return self._buscar_recursivo(valor, nodo_actual.izquierda)
					        else:
					            return self._buscar_recursivo(valor, nodo_actual.derecha)

					    def eliminar(self, valor):
					        """
					        Elimina un valor del árbol binario de búsqueda.
					        """
					        self.raiz = self._eliminar_recursivo(valor, self.raiz)

					    def _eliminar_recursivo(self, valor, nodo_actual):
					        if nodo_actual is None:
					            return nodo_actual
					        elif valor < nodo_actual.valor:
					            nodo_actual.izquierda = self._eliminar_recursivo(valor, nodo_actual.izquierda)
					        elif valor > nodo_actual.valor:
					            nodo_actual.derecha = self._eliminar_recursivo(valor, nodo_actual.derecha)
					        else:
					            # Caso 1: El nodo a eliminar es una hoja
					            if nodo_actual.izquierda is None and nodo_actual.derecha is None:
					                nodo_actual = None
					            # Caso 2: El nodo a eliminar tiene un solo hijo
					            elif nodo_actual.izquierda is None:
					                nodo_actual = nodo_actual.derecha
					            elif nodo_actual.derecha is None:
					                nodo_actual = nodo_actual.izquierda
					            # Caso 3: El nodo a eliminar tiene dos hijos
					            else:
					                sucesor = self._encontrar_sucesor(nodo_actual.derecha)
					                nodo_actual.valor = sucesor.valor
					                nodo_actual.derecha = self._eliminar_recursivo(sucesor.valor, nodo_actual.derecha)
					        return nodo_actual

					    def _encontrar_sucesor(self, nodo_actual):
					        while nodo_actual.izquierda is not None:
					            nodo_actual = nodo_actual.izquierda
					        return nodo_actual

					    def imprimir_inorden(self):
					        """
					        Imprime los valores del árbol en orden ascendente (inorden).
					        """
					        self._imprimir_inorden_recursivo(self.raiz)

					    def _imprimir_inorden_recursivo(self, nodo_actual):
					        if nodo_actual is not None:
					            self._imprimir_inorden_recursivo(nodo_actual.izquierda)
					            print(nodo_actual.valor, end=" ")
					            self._imprimir_inorden_recursivo(nodo_actual.derecha)


						# Crear un árbol binario de búsqueda
						arbol = ArbolBinarioBusqueda()

						# Insertar valores en el árbol
						arbol.insertar(50)
						arbol.insertar(30)
						arbol.insertar(70)
						arbol.insertar(20)
						arbol.insertar(40)
						arbol.insertar(60)
						arbol.insertar(80)

						# Imprimir los valores del árbol en orden ascendente
						arbol.imprimir_inorden()  # Salida: 20 30 40 50 60 70 80

						# Buscar un valor en el árbol
						print(arbol.buscar(40))  # Salida: True
						print(arbol.buscar(90))  # Salida: False

						# Eliminar un valor del árbol
						arbol.eliminar(30)

						# Imprimir los valores del árbol nuevamente
						arbol.imprimir_inorden()  # Salida: 20 40 50 60 70 80

		    	```	

		    	En este ejemplo, hemos implementado un árbol binario de búsqueda utilizando dos clases: Nodo y ArbolBinarioBusqueda. La clase Nodo representa un nodo en el árbol y la clase ArbolBinarioBusqueda representa el árbol en sí.

				Hemos definido métodos para insertar valores en el árbol (insertar), buscar un valor en el árbol (buscar), eliminar un valor del árbol (eliminar) e imprimir los valores del árbol en orden ascendente (imprimir_inorden).

				La inserción de valores se realiza siguiendo la regla de un árbol binario de búsqueda, donde los valores menores se colocan en el subárbol izquierdo y los valores mayores en el subárbol derecho.

				La búsqueda de un valor se realiza de forma recursiva, comparando el valor con el valor actual del nodo y navegando hacia la izquierda o la derecha según corresponda.

				La eliminación de un valor se realiza considerando tres casos: cuando el nodo a eliminar es una hoja, cuando tiene un solo hijo o cuando tiene dos hijos.

				La impresión en orden ascendente se realiza siguiendo el recorrido inorden del árbol, que imprime primero los valores del subárbol izquierdo, luego el valor actual del nodo y finalmente los valores del subárbol derecho.

				En este ejemplo, hemos creado un árbol binario de búsqueda, insertado valores, realizado búsquedas, eliminado valores y luego hemos impreso los valores del árbol en orden ascendente.

				Los árboles son estructuras de datos importantes y se utilizan ampliamente en algoritmos de búsqueda, ordenamiento, estructuras de datos más complejas y muchas otras aplicaciones.


		    9. Grafos: 

		    	Un grafo es una estructura de datos compuesta por vértices y aristas que conectan los vértices. Los grafos se utilizan para representar relaciones y conexiones entre elementos.

		    ```python: 
		    	
		    	class Grafo:
				    def __init__(self):
				        self.grafo = {}

				    def agregar_vertice(self, vertice):
				        """
				        Agrega un vértice al grafo.
				        """
				        if vertice not in self.grafo:
				            self.grafo[vertice] = []

				    def agregar_arista(self, vertice1, vertice2):
				        """
				        Agrega una arista entre dos vértices en el grafo.
				        """
				        if vertice1 in self.grafo and vertice2 in self.grafo:
				            self.grafo[vertice1].append(vertice2)
				            self.grafo[vertice2].append(vertice1)

				    def obtener_vertices(self):
				        """
				        Devuelve una lista con todos los vértices del grafo.
				        """
				        return list(self.grafo.keys())

				    def obtener_adyacentes(self, vertice):
				        """
				        Devuelve una lista con los vértices adyacentes a un vértice dado.
				        """
				        if vertice in self.grafo:
				            return self.grafo[vertice]

				    def imprimir_grafo(self):
				        """
				        Imprime el grafo en forma de lista de adyacencia.
				        """
				        for vertice in self.grafo:
				            adyacentes = self.grafo[vertice]
				            print(f"{vertice}: {adyacentes}")


					# Crear un grafo
					grafo = Grafo()

					# Agregar vértices al grafo
					grafo.agregar_vertice("A")
					grafo.agregar_vertice("B")
					grafo.agregar_vertice("C")
					grafo.agregar_vertice("D")
					grafo.agregar_vertice("E")

					# Agregar aristas al grafo
					grafo.agregar_arista("A", "B")
					grafo.agregar_arista("B", "C")
					grafo.agregar_arista("C", "D")
					grafo.agregar_arista("D", "E")
					grafo.agregar_arista("E", "A")

					# Obtener la lista de vértices
					vertices = grafo.obtener_vertices()
					print(vertices)  # Salida: ['A', 'B', 'C', 'D', 'E']

					# Obtener los vértices adyacentes a un vértice dado
					adyacentes = grafo.obtener_adyacentes("B")
					print(adyacentes)  # Salida: ['A', 'C']

					# Imprimir el grafo en forma de lista de adyacencia
					grafo.imprimir_grafo()
					# Salida:
					# A: ['B', 'E']
					# B: ['A', 'C']
					# C: ['B', 'D']
					# D: ['C', 'E']
					# E: ['D', 'A']

		    ```	

		    	En este ejemplo, hemos implementado un grafo no dirigido utilizando una lista de adyacencia. La clase Grafo representa el grafo y contiene métodos para agregar vértices, agregar aristas, obtener los vértices y los vértices adyacentes, y para imprimir el grafo en forma de lista de adyacencia.

				Hemos creado un grafo con cinco vértices (A, B, C, D, E) y hemos agregado aristas para conectar los vértices. Cada vértice se representa como una clave en el diccionario grafo, y el valor asociado a cada vértice es una lista que contiene los vértices adyacentes a él.

				Luego, hemos utilizado los métodos obtener_vertices y obtener_adyacentes para obtener información sobre el grafo. Hemos obtenido la lista de vértices y los vértices adyacentes al vértice "B". Finalmente, hemos utilizado el método imprimir_grafo para imprimir el grafo en forma de lista de adyacencia.

				Los grafos son estructuras de datos utilizadas para representar relaciones entre elementos. Se utilizan en una variedad de aplicaciones, como redes sociales, algoritmos de búsqueda y rutas, sistemas de recomendación, y muchos otros problemas que involucran conexiones y relaciones entre entidades.



		    10. bytes: 

		    	El tipo de dato bytes en Python se utiliza para representar secuencias de bytes inmutables. Se utilizan en situaciones donde se requiere un manejo preciso de datos binarios, como en la lectura y escritura de archivos binarios, el cifrado de datos y la comunicación de datos a través de redes.

		    	```python: 

		    		# Definir una secuencia de bytes
					secuencia_bytes = b'\x41\x42\x43\x44'

					# Acceder a elementos de la secuencia de bytes
					print(secuencia_bytes[0])  # Salida: 65 (valor decimal del byte '\x41')
					print(secuencia_bytes[2])  # Salida: 67 (valor decimal del byte '\x43')

					# Convertir la secuencia de bytes en una cadena hexadecimal
					cadena_hexadecimal = secuencia_bytes.hex()
					print(cadena_hexadecimal)  # Salida: "41424344"

					# Obtener la longitud de la secuencia de bytes
					print(len(secuencia_bytes))  # Salida: 4

					# Iterar sobre los bytes de la secuencia de bytes
					for byte in secuencia_bytes:
					    print(byte)

					# Comprobar si un byte está presente en la secuencia de bytes
					print(b'\x41' in secuencia_bytes)  # Salida: True

					# Convertir la secuencia de bytes en una lista de enteros
					lista_enteros = list(secuencia_bytes)
					print(lista_enteros)  # Salida: [65, 66, 67, 68]

					# Convertir la secuencia de bytes en una cadena de caracteres
					cadena_caracteres = secuencia_bytes.decode('utf-8')
					print(cadena_caracteres)  # Salida: "ABCD"

		    	```

		    	En este ejemplo, hemos definido una secuencia de bytes utilizando el prefijo b. La secuencia de bytes contiene los bytes A (valor decimal 65), B (valor decimal 66), C (valor decimal 67) y D (valor decimal 68).

				Hemos demostrado cómo acceder a elementos individuales de la secuencia de bytes utilizando el índice, cómo convertir la secuencia de bytes en una cadena hexadecimal utilizando el método hex(), cómo obtener la longitud de la secuencia de bytes utilizando la función len, cómo iterar sobre los bytes de la secuencia de bytes utilizando un bucle for, cómo comprobar la existencia de un byte utilizando el operador in, cómo convertir la secuencia de bytes en una lista de enteros, y cómo convertir la secuencia de bytes en una cadena de caracteres utilizando el método decode().


		    11. byte array:

		    	El tipo de dato bytearray en Python es similar a bytes, pero a diferencia de bytes, es mutable. Esto significa que se pueden modificar los elementos individuales del bytearray. Se utilizan en situaciones donde se requiere un manejo y manipulación de datos binarios mutable, como en la manipulación de imágenes, el procesamiento de archivos binarios y la comunicación de datos a través de redes.

		    	```python: 

		    		# Definir un bytearray
					bytearray_objeto = bytearray(b'\x41\x42\x43\x44')

					# Acceder a elementos del bytearray
					print(bytearray_objeto[0])  # Salida: 65 (valor decimal del byte '\x41')
					print(bytearray_objeto[2])  # Salida: 67 (valor decimal del byte '\x43')

					# Modificar un elemento del bytearray
					bytearray_objeto[1] = 66
					print(bytearray_objeto)  # Salida: bytearray(b'ABCD')

					# Agregar bytes al bytearray
					bytearray_objeto.append(69)
					print(bytearray_objeto)  # Salida: bytearray(b'ABCDE')

					# Eliminar bytes del bytearray
					del bytearray_objeto[0]
					print(bytearray_objeto)  # Salida: bytearray(b'BCDE')

					# Convertir el bytearray en una lista de enteros
					lista_enteros = list(bytearray_objeto)
					print(lista_enteros)  # Salida: [66, 67, 68, 69]

					# Convertir el bytearray en una cadena de caracteres
					cadena_caracteres = bytearray_objeto.decode('utf-8')
					print(cadena_caracteres)  # Salida: "BCDE"

		    	```

		    	En este ejemplo, hemos definido un objeto bytearray utilizando el prefijo b. El bytearray contiene los bytes A (valor decimal 65), B (valor decimal 66), C (valor decimal 67) y D (valor decimal 68).

				Hemos demostrado cómo acceder a elementos individuales del bytearray utilizando el índice, cómo modificar un elemento del bytearray, cómo agregar bytes al bytearray utilizando el método append, cómo eliminar bytes del bytearray utilizando la instrucción del, cómo convertir el bytearray en una lista de enteros, y cómo convertir el bytearray en una cadena de caracteres utilizando el método decode().


		    12. frozen set: 

		    	Los frozensets se utilizan cuando se necesita un conjunto inmutable, especialmente en casos donde se requiere que un conjunto sea una clave en un diccionario o un elemento en otro conjunto. A diferencia de los conjuntos normales, los frozensets se pueden utilizar como claves en diccionarios debido a su inmutabilidad.

		    	```python: 

		    		# Definir un frozenset
					conjunto_fijo = frozenset([1, 2, 3, 4, 5])

					# Mostrar el frozenset
					print(conjunto_fijo)  # Salida: frozenset({1, 2, 3, 4, 5})

					# Intentar agregar un elemento al frozenset generará un error
					conjunto_fijo.add(6)  # Generará un error AttributeError: 'frozenset' object has no attribute 'add'

					# Verificar la existencia de un elemento en el frozenset
					print(4 in conjunto_fijo)  # Salida: True
					print(8 in conjunto_fijo)  # Salida: False

					# Obtener la longitud del frozenset
					print(len(conjunto_fijo))  # Salida: 5

					# Iterar sobre los elementos del frozenset
					for elemento in conjunto_fijo:
					    print(elemento)

					# Realizar operaciones de conjunto con frozensets
					conjunto1 = frozenset([1, 2, 3])
					conjunto2 = frozenset([3, 4, 5])

					interseccion = conjunto1.intersection(conjunto2)
					print(interseccion)  # Salida: frozenset({3})

		    	```

		    	En este ejemplo, hemos definido un frozenset llamado conjunto_fijo que contiene los números del 1 al 5.

				Hemos demostrado cómo mostrar el frozenset, cómo verificar la existencia de un elemento en el frozenset utilizando el operador in, cómo obtener la longitud del frozenset utilizando la función len, y cómo iterar sobre los elementos del frozenset utilizando un bucle for.

				Es importante tener en cuenta que un frozenset es una versión inmutable de un conjunto. Esto significa que no se pueden realizar cambios en el frozenset una vez creado, como agregar o eliminar elementos. Sin embargo, se pueden realizar operaciones de conjunto, como intersecciones o uniones, utilizando métodos específicos.


		Estructuras de datos del modulo collections: 

			El módulo collections es un módulo adicional en la biblioteca estándar de Python que proporciona implementaciones adicionales de estructuras de datos especializadas y optimizadas. Estas estructuras de datos van más allá de las estructuras de datos básicas incorporadas, como listas y diccionarios, y ofrecen funcionalidades más avanzadas y específicas para casos de uso comunes.

			1. deque: 

				La clase deque proporciona una implementación eficiente de una cola doble (double-ended queue). Permite agregar y eliminar elementos tanto desde el principio como desde el final de la cola en tiempo constante. Es útil cuando se requiere un acceso rápido tanto al inicio como al final de una colección de elementos.


			2. Counter:

				La clase Counter es útil para contar elementos en una colección. Proporciona una forma rápida y conveniente de contar elementos únicos y generar histogramas.


			3. OrderedDict: 

				La clase OrderedDict es una variante de diccionario que mantiene el orden de inserción de los elementos. A diferencia de un diccionario regular, el OrderedDict recuerda el orden en que se agregaron los elementos y los devuelve en ese mismo orden al iterar sobre ellos.


			4. defaultdict: 

				La clase defaultdict es una subclase de diccionario que permite asignar un valor predeterminado a una clave que no está presente en el diccionario. Cuando se accede a una clave inexistente, se crea automáticamente una entrada para esa clave con el valor predeterminado especificado.


			5. namedtuple: 

				La función namedtuple permite crear tuplas con campos con nombre. Proporciona una forma legible y semántica de trabajar con estructuras de datos que tienen campos específicos.


		Llamadas en Python: 

			Funciones:

				Son objetos que pueden ser llamados para ejecutar un bloque de código.

				Permiten agrupar y reutilizar código de manera eficiente.

				Las funciones en Python son muy flexibles y versátiles, lo que las hace poderosas herramientas para organizar y reutilizar código.

				Ventajas de una función: 

					1. Una función en Python es un bloque de código que realiza una tarea específica y se puede invocar desde cualquier parte del programa.

					2.  Se definen utilizando la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener argumentos.

					3. Los argumentos son valores que se pasan a la función para realizar operaciones específicas.

					4. Pueden devolver un valor utilizando la palabra clave return.

					5. Una vez definida una función, se puede llamar (o invocar) utilizando su nombre y pasando los argumentos necesarios.


				Usos de la función: 

					1. Modularidad y reutilización de código: 

						Las funciones permiten dividir un programa en módulos más pequeños y manejables. Esto hace que el código sea más legible, mantenible y reutilizable.

					2. Abstracción: 

						Las funciones ayudan a ocultar los detalles de implementación y se centran en proporcionar una interfaz clara y simple para realizar una tarea específica.

					3. Estructuración del código: 

						Las funciones facilitan la organización del código en bloques lógicos, lo que mejora la comprensión y facilita el trabajo en equipo.

					4. Resolución de problemas: 

						Las funciones permiten descomponer problemas complejos en tareas más pequeñas y manejables, lo que facilita el proceso de resolución de problemas.

					5. Recursión:

						Las funciones pueden llamarse a sí mismas, lo que permite la implementación de algoritmos recursivos para problemas que se resuelven de manera iterativa.

				```python: 

					def sumar(a, b):
					    """
					    Función que suma dos números.
					    """
					    resultado = a + b
					    return resultado

					# Llamada a la función
					x = 5
					y = 3
					suma = sumar(x, y)

					# Imprimir el resultado
					print(suma)  # Salida: 8

				```

				```python:

					# Definición de una función
					def calcular_promedio(lista):
					    """
					    Calcula el promedio de una lista de números.
					    """
					    if len(lista) == 0:
					        return None  # Retorna None si la lista está vacía
					    
					    total = sum(lista)
					    promedio = total / len(lista)
					    return promedio

					# Llamada a la función
					numeros = [10, 8, 6, 9, 7]
					promedio_resultado = calcular_promedio(numeros)
					print("Promedio:", promedio_resultado)  # Salida: Promedio: 8.0

					# Utilizando argumentos por defecto
					def saludar(nombre, saludo="Hola"):
					    """
					    Saluda a una persona con un saludo por defecto.
					    """
					    mensaje = f"{saludo}, {nombre}!"
					    return mensaje

					print(saludar("Juan"))  # Salida: Hola, Juan!
					print(saludar("María", "Buenos días"))  # Salida: Buenos días, María!

					# Funciones con número variable de argumentos
					def sumar_numeros(*args):
					    """
					    Suma un número variable de argumentos.
					    """
					    total = sum(args)
					    return total

					resultado = sumar_numeros(1, 2, 3, 4, 5)
					print("Suma:", resultado)  # Salida: Suma: 15

					# Funciones con argumentos de palabras clave
					def imprimir_informacion(**kwargs):
					    """
					    Imprime la información proporcionada mediante argumentos de palabras clave.
					    """
					    for clave, valor in kwargs.items():
					        print(f"{clave}: {valor}")

					imprimir_informacion(nombre="Juan", edad=30, ciudad="Madrid")

					# Funciones recursivas
					def factorial(n):
					    """
					    Calcula el factorial de un número utilizando recursión.
					    """
					    if n == 0 or n == 1:
					        return 1
					    else:
					        return n * factorial(n - 1)

					resultado_factorial = factorial(5)
					print("Factorial:", resultado_factorial)  # Salida: Factorial: 120

				```
				En este ejemplo, hemos creado una función llamada calcular_promedio que toma una lista de números como argumento y devuelve el promedio de esos números. La función utiliza una estructura condicional para manejar el caso en que la lista esté vacía y retorna None en ese caso.

				También hemos mostrado cómo utilizar argumentos por defecto en la función saludar, donde el saludo tiene un valor predeterminado de "Hola". Esto permite llamar a la función con o sin proporcionar un saludo específico.

				Además, hemos utilizado el parámetro especial *args en la función sumar_numeros, que permite aceptar un número variable de argumentos y calcular la suma de ellos utilizando la función sum.

				Asimismo, hemos mostrado el uso de argumentos de palabras clave con el parámetro especial **kwargs en la función imprimir_informacion. Esto permite proporcionar información utilizando argumentos de palabras clave y luego imprimir esa información en un bucle for.

				Por último, hemos incluido una función recursiva factorial que calcula el factorial de un número utilizando la recursión. La función verifica el caso base cuando n es 0 o 1, y de lo contrario, llama a sí misma con un valor decreciente hasta alcanzar el caso base.


			Metodos/methods: 

				Son funciones que están asociadas a objetos específicos. A diferencia de las funciones, que son independientes y se pueden invocar de manera global, los métodos están vinculados a un objeto en particular y pueden acceder y manipular los datos dentro de ese objeto.

				Ventajas de los metodos: 

					1. Son funciones que están definidas dentro de una clase. Cada instancia (objeto) de esa clase puede llamar y ejecutar los métodos asociados.

					2. Tienen acceso a los datos internos de un objeto a través del parámetro self, que representa la propia instancia del objeto.

					3. Pueden realizar acciones específicas o realizar operaciones en los datos de un objeto.

					4. Pueden modificar los datos internos del objeto o devolver resultados basados en esos datos.
				
					Los métodos se definen dentro de la clase utilizando la sintaxis def nombre_del_metodo(self, otros_argumentos).

		
			Usos de la metodos: 

				1. Manipulación de datos del objeto: 

					Los métodos pueden acceder a los atributos y datos del objeto en el que están definidos, lo que permite realizar operaciones y modificaciones específicas en esos datos.

			    2. Encapsulación y ocultamiento de datos:

			    	Los métodos pueden controlar el acceso a los atributos de un objeto y garantizar que solo se modifiquen o accedan de manera controlada.

			    3. Implementación de comportamiento específico del objeto: 

			    	Los métodos definen el comportamiento de un objeto y permiten que responda a diferentes acciones o eventos específicos.

			    4. Interacción entre objetos:

			    	Los métodos de un objeto pueden invocar métodos de otros objetos para lograr una interacción y comunicación entre ellos.

			    5. Reutilización de código: 

			    	Los métodos pueden definirse una vez en una clase y luego ser invocados por múltiples instancias de ese objeto, lo que promueve la reutilización de código y mejora la legibilidad y mantenibilidad del programa.


				```python: 

					class Persona:
					    def __init__(self, nombre, edad):
					        self.nombre = nombre
					        self.edad = edad
					    
					    def saludar(self):
					        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
					    
					    def envejecer(self, cantidad_anios):
					        self.edad += cantidad_anios

					# Crear una instancia de la clase Persona
					juan = Persona("Juan", 30)

					# Llamar a los métodos de la instancia
					juan.saludar()  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

					juan.envejecer(5)
					juan.saludar()  # Salida: "Hola, mi nombre es Juan y tengo 35 años."

				```

				En este ejemplo, hemos definido una clase Persona que tiene dos métodos: saludar() y envejecer(). El método saludar() muestra un saludo con el nombre y la edad de la persona. El método envejecer() recibe una cantidad de años y aumenta la edad de la persona en esa cantidad.

				Hemos creado una instancia de la clase Persona llamada juan. Luego, llamamos a los métodos saludar() y envejecer() de esa instancia, lo que nos permite interactuar y modificar los datos específicos de ese objeto.

				Los métodos son una parte fundamental de la programación orientada a objetos, ya que permiten definir el comportamiento y las acciones específicas asociadas a un objeto.


			Clases/Classes: 

				las clases son una parte fundamental de la programación orientada a objetos (POO). 

				Una clase es una plantilla o un plano que define la estructura, los atributos y los comportamientos de los objetos que se crean a partir de ella.


				Paso a paso de las clases: 

					1. Una clase es una estructura de programación que encapsula datos (atributos) y funciones (métodos) relacionadas en un solo objeto.

				    2. Los objetos son instancias de una clase. Cada objeto creado a partir de una clase tiene sus propios atributos y puede ejecutar los métodos definidos en esa clase.

				    3. Las clases se definen utilizando la palabra clave class, seguida del nombre de la clase y dos puntos. El cuerpo de la clase contiene la definición de atributos y métodos.

				    4. Los atributos son variables que almacenan datos asociados a un objeto específico.

				    5. Los métodos son funciones que están definidas dentro de una clase y se aplican a los objetos creados a partir de esa clase.

				    6. Los objetos creados a partir de una clase tienen acceso a los métodos y atributos de esa clase utilizando la sintaxis de punto (objeto.metodo() o objeto.atributo).


			Usos de las clases: 

				1. Modelado de objetos del mundo real: 

					Las clases permiten crear objetos que representan entidades del mundo real y encapsulan sus atributos y comportamientos. Por ejemplo, una clase Persona puede tener atributos como nombre, edad y métodos como saludar.

				2. Reutilización de código:

				 	Las clases permiten definir una estructura común y crear múltiples objetos basados en esa estructura. Esto promueve la reutilización de código y evita la repetición innecesaria.

				3. Abstracción y modularidad: 

					Las clases proporcionan una abstracción de datos y comportamientos complejos, lo que facilita la comprensión y el manejo del código.

				4. Encapsulación y ocultamiento de datos: 

					Las clases permiten controlar el acceso a los datos y protegerlos mediante la ocultación de información interna. Esto ayuda a mantener la integridad y la consistencia de los datos.

				5. Herencia y polimorfismo:

					Las clases pueden heredar atributos y métodos de otras clases, lo que permite la creación de jerarquías y relaciones entre objetos. Además, el polimorfismo permite que diferentes objetos respondan de manera diferente a los mismos métodos.

			```python: 

				class Persona:
				    def __init__(self, nombre, edad):
				        self.nombre = nombre
				        self.edad = edad
				    
				    def saludar(self):
				        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

				# Crear objetos (instancias) de la clase Persona
				juan = Persona("Juan", 30)
				maria = Persona("Maria", 25)

				# Llamar a los métodos de los objetos
				juan.saludar()  # Salida: "Hola, mi nombre es Juan y tengo 30 años."
				maria.saludar()  # Salida: "Hola, mi nombre es Maria y tengo 25 años."

			```

			En este ejemplo, hemos definido una clase Persona con un constructor __init__ y un método saludar(). El constructor inicializa los atributos nombre y edad de un objeto Persona. El método saludar() muestra un saludo utilizando los valores de los atributos del objeto.

			Luego, hemos creado dos objetos (instancias) de la clase Persona llamados juan y maria. Cada objeto tiene su propio conjunto de atributos y puede llamar a los métodos definidos en la clase.

			Las clases son una forma poderosa de estructurar y organizar el código en la programación orientada a objetos. Permiten crear objetos con atributos y comportamientos específicos, lo que facilita la creación de programas más estructurados, flexibles y reutilizables.


		Tipo de dato Modulo o importar código/archivo.py: 

			Un módulo es un archivo que contiene definiciones de variables, funciones y clases que se pueden utilizar en otros programas. 

			Los módulos permiten organizar y reutilizar el código, así como evitar conflictos de nombres y mantener el código ordenado. 

			Características: 

				1. Un módulo en Python es un archivo con extensión .py que contiene código Python.

				2. Los módulos se utilizan para agrupar y organizar el código relacionado en archivos separados.

				3. Los módulos pueden contener variables, funciones, clases u otros elementos definidos por el usuario.

			    4. Para utilizar un módulo en un programa, se debe importar utilizando la palabra clave import.

			    5. Después de importar un módulo, se puede acceder a sus elementos utilizando la sintaxis de punto (modulo.elemento).

			    6. Python proporciona una amplia biblioteca de módulos estándar que cubren una variedad de funcionalidades, como matemáticas, manipulación de archivos, manejo de fechas y horas, y más.


			Usos comunes: 

			    1. Reutilización de código: 

			    	Los módulos permiten definir y organizar el código en archivos separados, lo que promueve la reutilización y el mantenimiento eficiente del código.

			    2. Modularidad: 

			    	Los módulos ayudan a dividir un programa en partes lógicas más pequeñas y manejables, lo que facilita la comprensión y el desarrollo del software.

			    3. Evitar conflictos de nombres: 

			    	Los módulos permiten agrupar elementos con nombres similares sin generar conflictos. Cada módulo tiene su propio espacio de nombres, lo que evita colisiones de nombres de variables, funciones, etc.

			    4. Compartir código: 

			    	Los módulos facilitan el uso y la distribución de código entre diferentes programas y desarrolladores.

			    5. Ampliar la funcionalidad: 

			    	Los módulos estándar de Python proporcionan funcionalidades adicionales, como operaciones matemáticas avanzadas, manipulación de archivos, generación de números aleatorios, interacción con el sistema operativo y mucho más.

				6. Reutilización de código:

					Los módulos permiten definir y organizar el código en archivos separados, lo que promueve la reutilización y el mantenimiento eficiente del código.

			Ejemplo: 

				Tenemos un archivo llamado modulo_ejemplo.py que contiene el siguiente código:

				```python: 

					# modulo_ejemplo.py
					def saludar(nombre):
					    print(f"Hola, {nombre}!")

					PI = 3.14159

				```

				En otro archivo Python, puedes importar y utilizar este módulo de la siguiente manera:

				```python:

					import modulo_ejemplo

					modulo_ejemplo.saludar("Juan")  # Salida: "Hola, Juan!"
					
					print(modulo_ejemplo.PI)  # Salida: 3.14159

				```
				Usamos la función y el número pi directamente


|| POO
	
	Es un paradigma de programación que se basa en el concepto de "objetos" para representar entidades del mundo real y modelar su comportamiento y relaciones.

	En POO, los objetos son instancias de clases, que actúan como plantillas o moldes para crear objetos con características y comportamientos similares.

	La POO se utiliza para organizar y estructurar el código de manera modular y reutilizable, lo que permite desarrollar programas más flexibles, mantenibles y escalables. Algunos de los conceptos clave en la POO son:

	La POO se utiliza para organizar y estructurar el código de manera modular y reutilizable, lo que permite desarrollar programas más flexibles, mantenibles y escalables. 

	Algunos de los conceptos clave en la POO son:

    	1. Clases: 

    		Las clases son estructuras que definen atributos (datos) y métodos (funciones) que describen el comportamiento de los objetos que se crearán a partir de ellas.

    	2. Objetos: 

    		Los objetos son instancias de una clase específica. Cada objeto tiene su propio estado (valores de los atributos) y comportamiento (métodos asociados).

   	 	3. Encapsulación: 

   	 		La encapsulación es un principio que permite ocultar los detalles internos de un objeto y exponer solo la interfaz necesaria para interactuar con él. Esto mejora la modularidad y la seguridad del código.

   		4. Herencia: 

   			La herencia permite crear nuevas clases basadas en una clase existente, heredando sus atributos y métodos. Esto fomenta la reutilización de código y permite establecer relaciones jerárquicas entre las clases.

    	5. Polimorfismo: 

    		El polimorfismo permite que diferentes objetos respondan de manera diferente a una misma función o método. Esto facilita la flexibilidad y la extensibilidad del código.

	La POO tiene diversas aplicaciones y beneficios en el desarrollo de software.

	Algunas de las aplicaciones más comunes son:

    	Modelado de objetos del mundo real: 

    		La POO permite representar entidades del mundo real como objetos, lo que facilita el modelado y la resolución de problemas del mundo real.

    	Reutilización de código: 

    		La herencia y la creación de clases y objetos facilitan la reutilización de código, ya que se pueden heredar atributos y métodos de clases existentes.

    	Modularidad y mantenibilidad: 

    		La POO fomenta la estructuración modular del código en clases y objetos, lo que hace que sea más fácil de entender, mantener y modificar.

    	Programación escalable: 

    		La POO permite construir programas escalables, ya que se pueden agregar nuevas clases y objetos sin afectar el funcionamiento de las existentes.

    	Desarrollo en equipo: 

    		La POO facilita el desarrollo en equipo al permitir la división del trabajo en base a las clases y objetos, lo que mejora la colaboración y la eficiencia.


    Ejemplo: 

    	```python: 

    		class Perro:
			    def __init__(self, nombre, edad):
			        self.nombre = nombre
			        self.edad = edad

			    def ladrar(self):
			        print("¡Woof woof!")

			    def presentarse(self):
			        print("Hola, soy", self.nombre, "y tengo", self.edad, "años.")

			# Crear objetos (instancias) de la clase Perro
			perro1 = Perro("Firulais", 3)
			perro2 = Perro("Max", 5)

			# Acceder a los atributos y llamar a los métodos de los objetos
			print(perro1.nombre)      # Imprime: Firulais
			print(perro2.edad)        # Imprime: 5

			perro1.ladrar()           # Imprime: ¡Woof woof!
			perro2.presentarse()      # Imprime: Hola, soy Max y tengo 5 años.

    	``` 	

    	En este ejemplo, creamos una clase llamada "Perro" que representa a un perro. La clase tiene tres componentes principales:

	    1. El método __init__ es un constructor especial que se ejecuta automáticamente cuando se crea un objeto de la clase. Recibe los argumentos nombre y edad y se encarga de asignarlos a los atributos self.nombre y self.edad respectivamente.

	    2. El método ladrar simplemente imprime el mensaje "¡Woof woof!" cuando se llama.

	    3. El método presentarse muestra el nombre y la edad del perro utilizando los atributos self.nombre y self.edad.

		Después de definir la clase, creamos dos objetos (instancias) de la clase "Perro" llamados perro1 y perro2. Cada objeto tiene su propio conjunto de atributos (nombre y edad).

		Finalmente, accedemos a los atributos y llamamos a los métodos de los objetos perro1 y perro2. Por ejemplo, perro1.nombre devuelve el nombre del perro Firulais, perro2.edad devuelve la edad 5, perro1.ladrar() imprime "¡Woof woof!" y perro2.presentarse() imprime "Hola, soy Max y tengo 5 años.".


	Principios de la POO: 

		Se conocen como los Principios SOLID y proporcionan directrices para escribir código limpio, modular y de alta calidad en el contexto de la programación orientada a objetos. Al seguir estos principios, puedes crear programas más flexibles, mantenibles y escalables.

		1. Principio de Responsabilidad Única (SRP): 

			Cada clase debe tener una única responsabilidad y motivo para cambiar. Esto promueve la cohesión y evita que las clases se vuelvan demasiado complejas o tengan dependencias excesivas.

	    2. Principio de Abierto/Cerrado (OCP): 

	    	Las clases deben estar abiertas para la extensión pero cerradas para la modificación. Esto significa que se pueden agregar nuevas funcionalidades a través de la herencia o la implementación de interfaces sin modificar el código existente.

	    3. Principio de Sustitución de Liskov (LSP): 

	    	Los objetos de una clase derivada deben poder sustituir a los objetos de la clase base sin afectar la integridad del programa. Esto asegura que las clases hijas cumplan con los contratos establecidos por las clases padres.

	    4. Principio de Segregación de Interfaces (ISP): 

	    	Los clientes no deben depender de interfaces que no utilicen. Las interfaces deben ser coherentes y específicas para los clientes que las necesiten, evitando interfaces excesivamente grandes o complejas.

	    5. Principio de Inversión de Dependencia (DIP): 

	    	Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones. Este principio promueve la dependencia hacia interfaces o abstracciones en lugar de implementaciones concretas.

	    6. Encapsulación: 

	    	Ocultar los detalles internos de una clase y proporcionar una interfaz pública clara para interactuar con ella. Esto mejora la seguridad, la modularidad y facilita los cambios en la implementación interna sin afectar a los clientes.

	    7. Reutilización: 

	    	Promover la reutilización de código a través de la herencia, la composición y la creación de componentes independientes y modulares. Esto evita la duplicación y mejora la mantenibilidad del código.

	    8. Coherencia y cohesión: 

	    	Mantener las clases y métodos coherentes en su funcionalidad y asegurar que cada clase tenga una única responsabilidad. Esto mejora la legibilidad y el mantenimiento del código.


	    Ejemplo: 

	    	```python: 

	    		# Principio de Responsabilidad Única (SRP) y Principio de Abierto/Cerrado (OCP)

				class Producto:
				    def __init__(self, nombre, precio):
				        self.nombre = nombre
				        self.precio = precio

				    def obtener_precio(self):
				        return self.precio


				class CarritoCompras:
				    def __init__(self):
				        self.productos = []

				    def agregar_producto(self, producto):
				        self.productos.append(producto)

				    def obtener_total(self):
				        total = 0
				        for producto in self.productos:
				            total += producto.obtener_precio()
				        return total


				# Principio de Segregación de Interfaces (ISP) y Principio de Inversión de Dependencia (DIP)

				class EnviadorCorreo:
				    def enviar_correo(self, destinatario, mensaje):
				        print("Enviando correo a", destinatario, "con el mensaje:", mensaje)


				class Notificador:
				    def __init__(self, enviador):
				        self.enviador = enviador

				    def notificar(self, destinatario, mensaje):
				        self.enviador.enviar_correo(destinatario, mensaje)


				# Uso de las clases

				producto1 = Producto("Camiseta", 20)
				producto2 = Producto("Pantalón", 30)

				carrito = CarritoCompras()
				carrito.agregar_producto(producto1)
				carrito.agregar_producto(producto2)

				total = carrito.obtener_total()
				print("Total de compra:", total)

				enviador_correo = EnviadorCorreo()
				notificador = Notificador(enviador_correo)
				notificador.notificar("ejemplo@example.com", "Su compra ha sido realizada con éxito.")

	    	```

	    	En este ejemplo, se muestran algunos de los principios SOLID aplicados:

		    Principio de Responsabilidad Única (SRP) y Principio de Abierto/Cerrado (OCP): La clase Producto tiene la única responsabilidad de representar un producto y proporcionar su precio. La clase CarritoCompras tiene la responsabilidad de gestionar los productos agregados y calcular el total de la compra. Al separar estas responsabilidades, cada clase tiene una única razón para cambiar y se puede extender sin modificar el código existente.

		    Principio de Segregación de Interfaces (ISP) y Principio de Inversión de Dependencia (DIP): La clase Notificador utiliza el principio de ISP, ya que solo depende de una interfaz (enviar_correo) en lugar de una implementación concreta. Además, se aplica el principio de DIP al inyectar una dependencia (EnviadorCorreo) a través de su constructor. Esto permite que Notificador dependa de abstracciones y no de implementaciones concretas, lo que facilita el cambio o la sustitución de la implementación del enviador de correo sin afectar a Notificador.

			Al crear objetos, se utilizan las clases Producto y CarritoCompras para representar productos y gestionar un carrito de compras. Luego, se calcula el total de la compra mediante el método obtener_total de la clase CarritoCompras.

			También se crea una clase EnviadorCorreo que representa un enviador de correos, y una clase Notificador que utiliza la interfaz del enviador de correo para enviar una notificación por correo electrónico.


|| Programación funcional
	
	Es un paradigma de programación que se centra en el uso de funciones y en el tratamiento de la computación como la evaluación de expresiones matemáticas. En la programación funcional, los programas se construyen mediante la composición y aplicación de funciones sin cambios de estado y sin efectos secundarios.

	La programación funcional se basa en los siguientes conceptos:

    	Funciones puras: 

    		Las funciones puras son funciones que siempre producen el mismo resultado para los mismos argumentos y no tienen efectos secundarios. Esto significa que una función pura no modifica datos externos ni depende de ellos.

    	Inmutabilidad: 

    		Los datos en la programación funcional son inmutables, lo que significa que no se pueden modificar una vez creados. En lugar de modificar datos existentes, se crean nuevos datos mediante transformaciones funcionales.

    	Evaluación de expresiones: 

    		En la programación funcional, las computaciones se realizan evaluando expresiones matemáticas. Se evita el uso de instrucciones y se enfatiza la composición y combinación de funciones.

    	Funciones de orden superior: 

    		Las funciones de orden superior son aquellas que pueden tomar otras funciones como argumentos o devolver funciones como resultado. Esto permite una mayor flexibilidad y modularidad en el diseño de programas.

	La programación funcional se utiliza para:

    	Escribir código más conciso y legible: 

    		Al enfocarse en funciones y expresiones, la programación funcional permite escribir código más conciso y expresivo, lo que facilita la lectura y comprensión del código.

	    Facilitar el razonamiento y depuración: 

	    	Al evitar cambios de estado y efectos secundarios, la programación funcional reduce la complejidad del programa y facilita el razonamiento sobre el comportamiento del código y la depuración de errores.

	    Manejar datos y transformaciones:

	    	La programación funcional es efectiva para manipular y transformar datos, ya que se basa en operaciones inmutables y composición de funciones.

	    Programación concurrente y paralela: 

	    	La programación funcional proporciona una base sólida para la programación concurrente y paralela, ya que las funciones puras son inherentemente seguras para la ejecución simultánea.

	    Procesamiento de datos grandes y algoritmos complejos: 

	    	La programación funcional se aplica en el procesamiento de datos grandes y en la implementación de algoritmos complejos, ya que permite modularidad, reusabilidad y expresividad en el código.

	
	Principios o directrices: 

		1. Inmutabilidad: 

			Los datos en la programación funcional se consideran inmutables, lo que significa que no se pueden modificar una vez creados. En lugar de modificar los datos existentes, se crean nuevos datos mediante transformaciones funcionales. Evitar la mutación de datos mejora la claridad del código y ayuda a prevenir efectos secundarios no deseados.

	    2. Funciones puras: 

	    	Las funciones puras son funciones que no tienen efectos secundarios y producen el mismo resultado para los mismos argumentos. No modifican datos externos ni dependen de ellos. Las funciones puras facilitan la comprensión y el razonamiento sobre el comportamiento del programa, ya que su comportamiento es predecible y no depende de un estado mutable.

	    3. Composición de funciones: 

	    	La composición de funciones es un principio clave en la programación funcional. Permite combinar funciones más pequeñas para formar funciones más complejas y expresivas. Al componer funciones, se evita la necesidad de variables mutables y se fomenta un flujo de datos claro y conciso.

	    4. Recursión: 

	    	La recursión es un enfoque común en la programación funcional para resolver problemas. En lugar de utilizar iteraciones y bucles, se utilizan llamadas recursivas para dividir un problema en subproblemas más pequeños. La recursión es especialmente útil cuando se trabaja con estructuras de datos recursivas o problemas de división y conquista.

	    5. Transparencia referencial: 

	    	La transparencia referencial significa que una función siempre devuelve el mismo resultado para los mismos argumentos, sin importar cuándo o dónde se llame. Esto facilita el razonamiento y la prueba de las funciones, ya que no hay efectos secundarios ocultos ni dependencia del estado externo.

	    6. Evitar el estado mutable compartido: 

	    	En la programación funcional, se evita el uso de variables mutables compartidas entre múltiples funciones. En su lugar, se fomenta el uso de datos inmutables y el paso explícito de argumentos entre funciones. Esto mejora la modularidad y reduce la posibilidad de efectos secundarios inesperados.


	Ejemplo: 


		```python: 

			# Ejemplo de programación funcional

			# Función pura
			def duplicar(numero):
			    return numero * 2

			# Función de orden superior
			def aplicar_funcion(func, lista):
			    return [func(elemento) for elemento in lista]

			# Datos
			numeros = [1, 2, 3, 4, 5]

			# Aplicar función pura a los datos
			resultados = aplicar_funcion(duplicar, numeros)

			# Imprimir resultados
			print(resultados)  # Imprime: [2, 4, 6, 8, 10]

		```	

		En este ejemplo, la programación funcional se muestra mediante el uso de funciones puras y la aplicación de una función de orden superior (aplicar_funcion) para aplicar la función pura a una lista de datos. Se evitan los cambios de estado y los efectos secundarios, y se enfatiza la composición de funciones y la transformación de datos inmutables.




	Diferencias y similitudes entre POO y Funcional:

		Diferencias: 

			Enfoque principal: 

				En la POO, el enfoque principal es en las entidades (objetos) y su interacción, mientras que en la programación funcional, el enfoque se centra en funciones y transformaciones de datos.

		    Cambios de estado: 

		    	En la POO, los objetos pueden tener estados cambiantes y pueden modificar sus propios atributos y datos externos. En la programación funcional, se evita el cambio de estado y se enfatiza la inmutabilidad de los datos.

		    Efectos secundarios: 

		    	En la POO, es común tener efectos secundarios, como modificar datos externos o realizar operaciones de entrada/salida. En la programación funcional, se busca minimizar o eliminar los efectos secundarios para lograr funciones puras.

		    Composición: 

		    	La POO se basa en la composición de objetos, donde los objetos contienen datos y comportamientos relacionados. En la programación funcional, la composición se basa en la combinación de funciones para formar funciones más complejas.

		    Mutabilidad: 

		    	En la POO, es común tener objetos mutables, donde los datos internos pueden cambiar. En la programación funcional, se promueve la inmutabilidad, donde los datos son inmutables y se crean nuevas estructuras de datos mediante transformaciones.


		Similitudes:

		    Abstracción: 

		    	Tanto en la POO como en la programación funcional, se busca la abstracción para modelar y resolver problemas complejos.

		    Reusabilidad: 

		    	Ambos enfoques promueven la reutilización de código, ya sea a través de la herencia y la composición en la POO, o mediante la aplicación de funciones y la composición de funciones en la programación funcional.

		    Modularidad: 

		    	Tanto en la POO como en la programación funcional, se fomenta la modularidad para dividir el código en componentes más pequeños y manejables.

		    Legibilidad y mantenibilidad: 	

		    	Ambos enfoques buscan un código claro y mantenible, aunque pueden tener enfoques diferentes para lograrlo.



|| CÓDIGO LIMPIO
	
	Se refiere a escribir código de manera clara, legible y estructurada, con el objetivo de facilitar su comprensión, mantenimiento y colaboración.


	1. Nombres significativos: 

		Utiliza nombres descriptivos y significativos para las variables, funciones, clases y otros elementos de tu código. Los nombres deben reflejar su propósito y función, lo que hace que el código sea más legible y comprensible.

	2. Estructura y organización: 

		Divide tu código en secciones lógicas y utiliza una estructura clara. Agrupa funciones relacionadas, utiliza comentarios para indicar secciones importantes y organiza tu código de manera que sea fácil de seguir. Esto facilita la navegación y comprensión del código.

	3. Mantenimiento y legibilidad: 

		Escribe código de manera que sea fácil de mantener. Evita líneas demasiado largas y utiliza sangrías adecuadas para mejorar la legibilidad. Separa el código en líneas y bloques lógicos, y utiliza espacios en blanco de manera consistente para hacer que el código sea más claro.

	4. Evita la repetición de código: 

		Si 	encuentras bloques de código repetidos, considera refactorizarlos en funciones o métodos reutilizables. Esto mejora la eficiencia y evita la duplicación innecesaria de código.

	5. Comentarios y documentación: 

		Utiliza comentarios para explicar el propósito y el funcionamiento de secciones de código importantes. Esto ayuda a otros desarrolladores (y a ti mismo en el futuro) a comprender rápidamente lo que hace el código. Además, documenta las funciones y clases con docstrings para proporcionar información sobre su uso y parámetros.

	6. Evita la complejidad excesiva: 

		Intenta mantener tu código simple y directo. Evita construcciones complicadas o algoritmos difíciles de entender, a menos que sean absolutamente necesarios. Un código más simple suele ser más fácil de leer, entender y depurar.

	7. Pruebas y errores: 

		Realiza pruebas unitarias y manejo adecuado de errores en tu código. Las pruebas ayudan a garantizar que el código funcione correctamente, mientras que el manejo de errores ayuda a evitar que el programa se bloquee o se comporte de manera inesperada.


	Ejemplo: 

		```python: 

			# Ejemplo de código limpio

			# Fundamento: Nombres significativos
			def calcular_area_rectangulo(base, altura):
			    area = base * altura
			    return area

			# Fundamento: Estructura y organización
			def main():
			    # Entrada de datos
			    base = float(input("Ingresa la base del rectángulo: "))
			    altura = float(input("Ingresa la altura del rectángulo: "))

			    # Cálculo del área
			    area = calcular_area_rectangulo(base, altura)

			    # Salida de resultados
			    print("El área del rectángulo es:", area)

			# Fundamento: Mantenimiento y legibilidad
			if __name__ == "__main__":
			    main()

		```

		En este ejemplo, se aplican varios fundamentos del código limpio:

		    1. Nombres significativos: 

		    	La función calcular_area_rectangulo tiene un nombre descriptivo y refleja su propósito. La variable area también tiene un nombre claro.

		    2. Estructura y organización:

		    	El código se divide en funciones y secciones lógicas. La función main se encarga de coordinar la ejecución del programa.

		    3. Mantenimiento y legibilidad:

		    	El código utiliza sangrías adecuadas y espacios en blanco para mejorar la legibilidad. También se utiliza una estructura clara con comentarios para indicar las partes importantes del código.

		    4. Evita la repetición de código: 

		    	La función calcular_area_rectangulo se crea para evitar la repetición de código cuando se necesita calcular el área del rectángulo.

		    5. Comentarios y documentación:

		    	Se utilizan comentarios para explicar el propósito y el funcionamiento de secciones importantes del código. Los comentarios ayudan a comprender rápidamente lo que hace cada parte.

		    6. Evita la complejidad excesiva: 

		    	El ejemplo se mantiene simple y directo, sin construcciones complicadas o algoritmos innecesariamente complejos.

		    7. Pruebas y errores: 

		    	Aunque no se muestra explícitamente en este ejemplo, se podrían agregar pruebas unitarias y manejo adecuado de errores para mejorar aún más el código.


