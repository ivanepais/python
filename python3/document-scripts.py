# Versiones




#...............




"""......................"""

# Sintaxis

# Esto es un comentario
print("Hola, mundo")  # Esto también es un comentario


# Identacion
if True:
    print("Este está indentado correctamente")
    print("Este también")

print("Este no está indentado correctamente")  # Generará un error


# Variables y asignacion
mensaje = "Hola, Python"
numero = 42
decimal = 3.14


# Tipos de datos
cadena = "Hola, Python" #inmutable index/accesible/ordenado
entero = 42
decimal = 3.14
lista = [1, 2, 3] # mutable index/accesible/ordenado
tupla = (4, 5, 6) # inmutable index/accesible/ordenado
conjunto = {7, 8, 9} # no duplicados/únicos no index/no accesible/no ordenado
diccionario = {"clave": "valor"} #mutable accesible/indexado/ordenado

"""
Características
Puede ser: 
mutable/agregado/elim -> Array/list dict clave:valor
inmutable/no agregado/elim -> String, tupla/coordenada/fijo/array2
accesible/indexado/ordenado -> Array, tupla/array2, dict clave:valor
no accesible/indexado/ordenado ->  Set/conjunto: si agregado

"""


# Entrada y salida
nombre = input("Ingresa tu nombre: ")
print("Hola,", nombre)


# Estructuras de control 
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Edad desconocida")

for i in range(5):
    print(i)

while contador < 10:
    print(contador)
    contador += 1





"""......................"""

# Variables

# Declaracion y asignacion 
nombre = "Alice"  # Asigna una cadena a la variable "nombre"
edad = 25  # Asigna un número entero a la variable "edad"
altura = 1.75  # Asigna un número de punto flotante a la variable "altura"


# Nombres
nombre = "Alice"  # Correcto
Nombre = "Bob"  # Correcto, pero distinto de "nombre"
_ultimo_nombre = "Smith"  # Correcto
1edad = 25  # Incorrecto, no puede comenzar con un número


# Tipos de variables/valores/datos
nombre = "Alice"  # Cadena
edad = 25  # Entero
altura = 1.75  # Punto flotante
numeros = [1, 2, 3, 4]  # Lista
tupla = (4, 5, 6) 
conjunto = {7, 8, 9} 
diccionario = {"clave": "valor"}


# Reasignación
edad = 25
print(edad)  # Imprimirá 25

edad = 30
print(edad)  # Imprimirá 30


# Operaciones
x = 5
y = 3
suma = x + y  # Suma de variables
producto = x * y  # Multiplicación de variables

nombre = "Alice"
saludo = "Hola, " + nombre  # Concatenación de cadenas


# Convenciones para los nombres

"""
Utiliza nombres en minúsculas para las variables (nombre, edad).
Si el nombre consta de varias palabras, sepáralas con guiones bajos (nombre_completo, puntos_totales).
 Evita nombres que puedan confundirse con palabras clave de Python (if, while, etc.).
"""


# Alcance de variables
variable_global = 10  # Variable global

def mi_funcion():
    variable_local = 5  # Variable local
    print(variable_global)  # Puedo acceder a una variable global aquí

print(variable_global)  # Puedo acceder a una variable global aquí
print(variable_local)  # Esto generará un error, la variable local no es visible aquí






"""......................"""

# Tipos de datos 

# String: inmutable
nombre = "Alice"
mensaje = 'Hola, ¿cómo estás?'


mensaje = "Hola, mundo"
longitud = len(mensaje)  # Devuelve 11


saludo = "Hola, "
nombre = "Alice"
mensaje = saludo + nombre  # Devuelve "Hola, Alice"


palabra = "Python"
primer_caracter = palabra[0]  # Devuelve "P"

# Cortar o segmentar 
mensaje = "Hola, mundo"
subcadena = mensaje[0:5]  # Devuelve "Hola,"


"""
.lower(): Convierte la cadena en minúsculas.
.upper(): Convierte la cadena en mayúsculas.
.strip(): Elimina espacios en blanco al principio y al final de la cadena.
.split(): Divide la cadena en una lista de subcadenas usando un delimitador.
.replace(): Reemplaza una subcadena con otra.
"""

texto = "Hola, Mundo"
texto_min = texto.lower()  # "hola, mundo"
texto_may = texto.upper()  # "HOLA, MUNDO"


# Formato o literales
nombre = "Alice"
edad = 30
saludo = f"Hola, {nombre}. Tienes {edad} años."


nombre = "Alice"
edad = 30
saludo = "Hola, {}. Tienes {} años.".format(nombre, edad)


# Comprobación con not, in 
mensaje = "Hola, mundo"
if "mundo" in mensaje:
    print("La subcadena 'mundo' está presente.")






#...............

# Number int, float

entero = 42
decimal = 3.14


a = 5
b = 3

suma = a + b  # Suma: 8
resta = a - b  # Resta: 2
multiplicacion = a * b  # Multiplicación: 15
division = a / b  # División: 1.666...


#Precisión 
x = 0.1 + 0.1 + 0.1  # Puede no ser exactamente 0.3 debido a la precisión de punto flotante


import math

raiz_cuadrada = math.sqrt(16)  # Raíz cuadrada: 4.0
potencia = math.pow(2, 3)  # Potencia: 8.0


# Redondeo: round(), math.floor() y math.ceil().
x = 3.7
redondeado = round(x)  # Redondeo: 4
truncado = math.floor(x)  # Truncamiento: 3


# Conversion
entero = int(5.3)  # Conversión a entero: 5
decimal = float(10)  # Conversión a decimal: 10.0


# Division entera y resto
division_entera = 7 // 3  # División entera: 2
resto = 7 % 3  # Resto: 1


# Comparaciones <, >, <=, >=, == y !=.
a = 5
b = 3

es_mayor = a > b  # Verdadero
es_igual = a == b  # Falso







#...............

# List: mutable, indexado/accesible
numeros = [1, 2, 3, 4]
nombres = ["Alice", "Bob", "Charlie"]


#Orden
numeros = [1, 2, 3, 4]
primer_numero = numeros[0]  # Devuelve 1


#Agregar .append()
frutas = ["manzana", "banana", "naranja"]
frutas.append("kiwi")  # Agrega "kiwi" al final de la lista


# Modificar elemento
numeros = [1, 2, 3, 4]
numeros[1] = 5  # Cambia el segundo elemento a 5


# Eliminar elemento remove() y .pop().
colores = ["rojo", "verde", "azul"]
colores.remove("verde")  # Elimina "verde" de la lista
ultimo_color = colores.pop()  # Elimina el último elemento y lo devuelve


# Operaciones
"""
.len(): Devuelve la longitud de la lista.
.count(): Cuenta cuántas veces aparece un elemento en la lista.
.index(): Encuentra el índice de un elemento en la lista.
"""
numeros = [1, 2, 3, 2, 4, 5, 2]
longitud = len(numeros)  # Devuelve 7
veces_dos_aparece = numeros.count(2)  # Devuelve 3
indice_cuatro = numeros.index(4)  # Devuelve 4


# Ordenar y revertir .sort(), .reverse()
numeros = [4, 1, 3, 2]
numeros.sort()  # Ordena la lista en orden ascendente
numeros.reverse()  # Revierte el orden de la lista


# Segmentacion por indice
frutas = ["manzana", "banana", "naranja", "kiwi"]
subfrutas = frutas[1:3]  # Devuelve ["banana", "naranja"]






#...............

# Tuple: inmutable

coordenadas = (3, 5)
dias_semana = ("Lunes", "Martes", "Miércoles")


# Inmutabilidad y orden
coordenadas = (3, 5)
primer_elemento = coordenadas[0]  # Devuelve 3


# Indexación y segmentación
mi_tupla = (1, 2, 3, 4, 5)
primer_elemento = mi_tupla[0]  # Devuelve 1
sub_tupla = mi_tupla[1:3]  # Devuelve (2, 3)


# Desempaquetado de Tuplas
punto = (3, 5)
x, y = punto  # x será 3, y será 5


# Concatenación y segmentación
tupla1 = (1, 2)
tupla2 = (3, 4)
tupla_concatenada = tupla1 + tupla2  # Devuelve (1, 2, 3, 4)
tupla_repetida = tupla1 * 3  # Devuelve (1, 2, 1, 2, 1, 2)


# Funciones para Tupla: len(), min(), max() y sum().
mi_tupla = (10, 5, 7, 3)
longitud = len(mi_tupla)  # Devuelve 4
valor_minimo = min(mi_tupla)  # Devuelve 3
valor_maximo = max(mi_tupla)  # Devuelve 10
suma = sum(mi_tupla)  # Devuelve 25







#...............

# Set: elementos únicos/no repetidos, no index/no acceso

frutas = {"manzana", "banana", "naranja"}


# Agregar/Eliminar elementos
colores = {"rojo", "verde", "azul"}
colores.add("amarillo")  # Agrega "amarillo" al conjunto
colores.remove("verde")  # Elimina "verde" del conjunto


# Pertenencia
frutas = {"manzana", "banana", "naranja"}
if "banana" in frutas:
    print("Banana está en el conjunto.")


"""
.union(): Realiza la unión de dos conjuntos.
.intersection(): Realiza la intersección de dos conjuntos.
.difference(): Calcula la diferencia entre dos conjuntos.
.issubset(): Comprueba si un conjunto es un subconjunto de otro.
.issuperset(): Comprueba si un conjunto es un superconjunto de otro.

"""
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)  # Devuelve {1, 2, 3, 4, 5}
interseccion = conjunto1.intersection(conjunto2)  # Devuelve {3}


# Modificar las operaciones anteriores
"""
update(), .intersection_update(), .difference_update(),
En lugar de crear uno nuevo
"""
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
conjunto1.update(conjunto2)  # Modifica conjunto1 a {1, 2, 3, 4, 5}


#...............

# Dict: mutables accesible/indexado/ordenado

persona = {"nombre": "Alice", "edad": 25, "altura": 1.75}
nombre = persona["nombre"]  # Devuelve "Alice"


# Modificar y agregar elementos
persona = {"nombre": "Alice", "edad": 30}
persona["edad"] = 31  # Modifica el valor de "edad"
persona["ciudad"] = "Nueva York"  # Agrega un nuevo par clave-valor


# Eliminar elementos del o método .pop().
persona = {"nombre": "Alice", "edad": 30}
del persona["edad"]  # Elimina el par clave-valor "edad"
ciudad = persona.pop("ciudad")  # Elimina y devuelve el valor asociado a "ciudad"


# Verificación pertenencia in not
persona = {"nombre": "Alice", "edad": 30}
if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario.")


# Obtener claves y valores .keys() y .values()
persona = {"nombre": "Alice", "edad": 30}
claves = persona.keys()  # Devuelve ["nombre", "edad"]
valores = persona.values()  # Devuelve ["Alice", 30]


# Obtener Par clave:valor
persona = {"nombre": "Alice", "edad": 30}
pares = persona.items()  # Devuelve [("nombre", "Alice"), ("edad", 30)]




"""
Características
Puede ser: 
mutable/agregado/elim -> Array/list, dict clave:valor
inmutable/no agregado/elim -> String, tupla/coordenada/fijo/array2
accesible/indexado/ordenado -> Array, tupla/array2, dict clave:valor
no accesible/indexado/ordenado ->  Set/conjunto es agregado/elimin

"""



#...............

# Bool

# Valor constante
verdadero = True
falso = False


# Operaciones 
a = True
b = False

negacion_a = not a  # Falso
conjuncion = a and b  # Falso
disyuncion = a or b  # Verdadero


# Comparaciones
"""
== (igual), != (distinto), < (menor que), > (mayor que), <= (menor o igual que), >= (mayor o igual que).
"""
x = 5
y = 10
es_igual = x == y  # Falso
es_menor = x < y  # Verdadero


# Pertenencia in not
numeros = [1, 2, 3, 4, 5]
tiene_tres = 3 in numeros  # Verdadero


# Control flujo
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Funciones que Retornan Valores Booleanos
"""
startswith() de las cadenas devuelve True si
"""
mensaje = "Hola, mundo"
comienza_con_hola = mensaje.startswith("Hola")  # Verdadero


# Conversión desde Otros Tipos
valor_entero = 5
valor_booleano = bool(valor_entero)  # Verdadero

cadena_vacia = ""
valor_booleano2 = bool(cadena_vacia)  # Falso








#...............

# None no es comparable, ni con none, no es falso

resultado = None

x = None
y = None
es_igual = x == y  # Verdadero


# Asignación inicial
resultado = None


# Valor de Retorno Predeterminado
def funcion_vacia():
    pass  # No tiene un return, por lo tanto, retorna None automáticamente


# Verificación comprobación de valor in not
resultado = realizar_alguna_operacion()
if resultado is None:
    print("La operación no produjo un resultado válido.")


# Comparación con is en lugar de usar ==
valor = None
if valor is None:
    print("El valor es None.")


# Funciones que No Retornan Valores
def funcion_sin_retorno():
    print("Esta función no retorna nada.")

resultado = funcion_sin_retorno()  # resultado será None




"""......................"""

# Comparadores o condicionales

"""
Se utilizan comúnmente en estructuras de control como declaraciones if, bucles y expresiones condicionales. 
"""

"""
Se toman dos valores y los comparan para determinar la relación entre ellos. 
Los valores pueden ser variables, constantes o expresiones.

Resultados Booleanos: siempre devuelven un valor booleano, es decir, True (verdadero) o False (falso), 
dependiendo del resultado de la comparación
"""

"""
Se utilizan en estructuras de control como declaraciones if, bucles while y for, y expresiones condicionales. 
Al combinarlos con operadores lógicos (and, or, not), puedes crear condiciones más complejas para controlar el flujo de tu programa y tomar decisiones 
"""

# Igual (==):
x = 5
y = 5
resultado = x == y  # Verdadero


# Distinto (!=):
x = 5
y = 10
resultado = x != y  # Verdadero


#Mayor que (>):
x = 10
y = 5
resultado = x > y  # Verdadero


# Menor que (<):
x = 5
y = 10
resultado = x < y  # Verdadero


# Mayor o igual que (>=):
x = 10
y = 5
resultado = x >= y  # Verdadero


# Menor o igual que (<=):
x = 5
y = 10
resultado = x <= y  # Verdadero





"""......................"""

# Casting o conversión de tipos

"""
Implicita o coerción:
Es automática cuando Python necesita un tipo de dato en otro para realizar una operación.
"""
x = 5         # int
y = 2.5       # float
resultado = x + y  # Aquí ocurre un casting implícito de int a float


"""
Explicita:
Cambiar deliberadamente el tipo de un objeto de datos utilizando funciones incorporadas.

int(): Convierte un valor a un entero.
float(): Convierte un valor a un número de punto flotante.
str(): Convierte un valor a una cadena.
bool(): Convierte un valor a un valor booleano.
list(): Convierte un valor a una lista.
tuple(): Convierte un valor a una tupla.
"""
valor_entero = 5
valor_flotante = float(valor_entero)  # Convierte a float

cadena_numero = "10"
valor_entero_desde_cadena = int(cadena_numero)  # Convierte a int

booleano = bool(1)  # Convierte a True, ya que 1 es considerado verdadero
#on off





"""......................"""

# Excepciones

"""
Si la lógica del problema/código tiene excepciones que generan errores
Agregamos un bloque para manejarlas
"""

try:
    numero = 10 / 0  # Intenta dividir por cero, lo cual lanza una excepción
except ZeroDivisionError:
    print("Error: División por cero")


try:
    valor = int("texto")  # Intenta convertir una cadena no numérica a entero
except ValueError:
    print("Error: Valor no numérico")
except TypeError:
    print("Error: Tipo incorrecto")


try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("Error: El archivo no existe")
else:
    contenido = archivo.read()
    archivo.close()


try:
    # Código que puede lanzar una excepción
except SomeException:
    # Manejo de la excepción
finally:
    # Código que siempre se ejecutará



"""......................"""

# Funciones 

def saludar(nombre):
    print("Hola,", nombre)


def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(5, 3)  # Llama a la función sumar con los argumentos 5 y 3


def cuadrado(numero):
    return numero ** 2

resultado = cuadrado(4)  # Llama a la función cuadrado y obtiene el valor de retorno


def multiplicar(a, b):
    """
    Esta función multiplica dos números y retorna el resultado.
    :param a: Primer número a multiplicar
    :param b: Segundo número a multiplicar
    :return: Resultado de la multiplicación
    """
    return a * b


# Anónima
cuadrado = lambda x: x ** 2
resultado = cuadrado(3)  # Devuelve 9


# Definición de una función simple
def saludar(nombre):
    """
    Esta función saluda a la persona cuyo nombre se proporciona.
    """
    print("Hola,", nombre)


# Llamada a la función
saludar("Alice")  # Salida: Hola, Alice


# Función con valor de retorno
def sumar(a, b):
    """
    Esta función suma dos números y retorna el resultado.
    """
    resultado = a + b
    return resultado

total = sumar(5, 3)  # total = 8


# Función con parámetros opcionales
def saludar_personalizado(nombre, saludo="Hola"):
    """
    Esta función saluda a la persona con un saludo personalizado.
    """
    print(saludo, nombre)

saludar_personalizado("Bob")  # Salida: Hola Bob
saludar_personalizado("Eve", "¡Hola!")  # Salida: ¡Hola! Eve


# Función con retorno múltiple
def dividir_y_restar(a, b):
    """
    Esta función divide a por b y retorna el cociente y la diferencia entre a y b.
    """
    cociente = a / b
    diferencia = a - b
    return cociente, diferencia

cociente_resultado, diferencia_resultado = dividir_y_restar(10, 2)
# cociente_resultado = 5.0, diferencia_resultado = 8


# Función con docstring
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dada su base y altura.
    :param base: Base del rectángulo.
    :param altura: Altura del rectángulo.
    :return: Área del rectángulo.
    """
    area = base * altura
    return area


# Uso de funciones incorporadas
longitud = len("Hola, mundo")  # longitud = 11


# Función lambda (anónima)
cuadrado = lambda x: x ** 2
resultado_cuadrado = cuadrado(3)  # resultado_cuadrado = 9


# Llamada a funciones en bucles
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    cuadrado_numero = cuadrado(numero)
    print(f"El cuadrado de {numero} es {cuadrado_numero}")


# Manejo de excepciones en función
def dividir(a, b):
    """
    Divide a por b y maneja la excepción si b es cero.
    """
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = "Error: División por cero"
    return resultado

resultado_division = dividir(10, 0)  # resultado_division = "Error: División por cero"






"""......................"""

# Funcion anonima








