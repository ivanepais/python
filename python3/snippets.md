|| BASICOS
	
	# Si no mostras con print(), los cálculos, los valores de las varibles, etc; se van a ejecutar pero vas a ver el resultado del código en el interprete.

	# Error sintácto hace fallar todo el programa.

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

|| FUNCIONES MATEMATICAS

	ORDEN DE OPERACIONES:

		PENDAS:


		igualdad:


	Tenemos que importarlo con una sentencia import:
	>>> import math

	Crea un objeto de módulo llamado math.

		import math   #importar

		print (math)  #verificar
		<module 'math' (built-in)>


|| FUNCIONES
	
	Parámetro: es el nombre de la variable, se usa en la definición.
	
	Argumento: es el valor para la variable/parametro, se usa en la llamada.
	
	definición:	
		
		def sumarMismo (num): #parámetro/nom var
		print (num + num)

	Llamada:	
		
		sumarMismo(2)  #argum de func/valor/variable
		4              #valor retorno

	Return:




	Variables y argumentos locales:




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

|| FLUJO DE EJECUCIÓN
	
	sentencias/def función > sentencias > llamada función (<< sentenc función) > sentencias.

	*leer flujo, no de inicio a fin.


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

		>>> imprimeDoble(’Jamón’*4)
		JamónJamónJamónJamón JamónJamónJamónJamón
		
		>>> imprimeDoble(math.cos(math.pi))
		-1.0 -1.0


|| DEBUGGEAR
	
	Un error sintáctico hace fallar todo el programa.