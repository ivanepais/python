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

#Ejemplos: 

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



# Casos de uso: 

# Procesamiento de texto
def mayusculas(texto):
    return texto.upper()

mensaje = mayusculas("Hola, mundo!")  # mensaje = "HOLA, MUNDO!"


# Operaciones matemáticas complejas
import math

def area_circulo(radio):
    return math.pi * radio**2

area = area_circulo(5)  # area ≈ 78.54


# Interacción con archivos
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

texto = leer_archivo('archivo.txt')


# Lógica del negocio completa
def calcular_precio_total(productos):
    total = 0
    for producto in productos:
        total += producto.precio
    return total

carrito = [Producto('Laptop', 800), Producto('Teléfono', 300)]
precio_total = calcular_precio_total(carrito)


# Funciones para interactuar con base de datos
import sqlite3

def conectar_base_de_datos():
    conexion = sqlite3.connect("mi_base_de_datos.db")
    return conexion

def ejecutar_consulta(conexion, consulta):
    cursor = conexion.cursor()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado

conexion_db = conectar_base_de_datos()
consulta_sql = "SELECT * FROM empleados"
resultado_consulta = ejecutar_consulta(conexion_db, consulta_sql)




"""......................"""

# Funcion anonima

# Ejemplos

# Ejemplo 1: Definir una función anónima y asignarla a una variable
suma = lambda x, y: x + y
resta = lambda x, y: x - y

resultado1 = suma(5, 3)  # resultado1 = 8
resultado2 = resta(5, 3) # resultado2 = 2


# Ejemplo 2: Usar una función anónima como argumento en una función
numeros = [1, 2, 3, 4, 5]
doble = list(map(lambda x: x * 2, numeros))
# 'map' aplica la función anónima a cada elemento de 'numeros'


# Ejemplo 3: Filtrar elementos usando una función anónima
pares = list(filter(lambda x: x % 2 == 0, numeros))
# 'filter' usa la función anónima para seleccionar elementos que cumplen la condición


# Ejemplo 4: Ordenar una lista de tuplas por el segundo elemento usando una función anónima
tuplas = [(2, 10), (1, 5), (3, 8)]
ordenado = sorted(tuplas, key=lambda x: x[1])
# 'sorted' utiliza la función anónima como criterio de ordenación


# Ejemplo 5: Crear una función anónima para manejar eventos de interfaz de usuario
def crear_boton(etiqueta, accion):
    print(f"Botón '{etiqueta}' clickeado.")
    accion()

boton_guardar = crear_boton("Guardar", lambda: print("Guardando datos..."))



# Casos de uso:

# Ordenamiento personalizado
estudiantes = [("Alice", 25), ("Bob", 20), ("Eve", 22)]

estudiantes_ordenados = sorted(estudiantes, key=lambda estudiante: estudiante[1])
# estudiantes_ordenados = [("Bob", 20), ("Eve", 22), ("Alice", 25)]


# Operaciones matemáticas simples
cuadrado = lambda x: x ** 2
resultado_cuadrado = cuadrado(3)  # resultado_cuadrado = 9


# Filtrado de datos
numeros = [1, 2, 3, 4, 5, 6]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
# numeros_pares = [2, 4, 6]


# Funciones Map
numeros = [1, 2, 3, 4, 5]

numeros_duplicados = list(map(lambda x: x * 2, numeros))
# numeros_duplicados = [2, 4, 6, 8, 10]


# Interfaz de usuario
from tkinter import Tk, Button

root = Tk()
boton = Button(root, text="Clic Me", command=lambda: print("Botón clickeado"))
boton.pack()
root.mainloop()


# Expresiones condicionales
es_par = lambda x: True if x % 2 == 0 else False
resultado = es_par(4)  # resultado = True


#Transformación de texto
palabras = ["hola", "mundo", "python"]

palabras_mayusculas = list(map(lambda palabra: palabra.upper(), palabras))
# palabras_mayusculas = ["HOLA", "MUNDO", "PYTHON"]






"""......................"""

# Funcion Autoinvocada

# Ejemplos: 

# Ejemplo 1: Función autoinvocada simple
resultado = (lambda x, y: x + y)(5, 3)
# La función se define y se ejecuta inmediatamente con los argumentos 5 y 3
# resultado = 8


# Ejemplo 2: Usar una función autoinvocada para crear un ámbito local
def crear_contador():
    contador = 0
    incrementar = (lambda: contador + 1)()
    return incrementar

contador = crear_contador()
print(contador)  # contador = 1


# Ejemplo 3: Crear un módulo con variables privadas usando una función autoinvocada
modulo = (lambda:
    {
        "variable_privada": 42,
        "funcion_privada": lambda x: x * 2
    }
)()

print(modulo["variable_privada"])  # variable_privada = 42
print(modulo["funcion_privada"](5))  # resultado = 10


# Ejemplo 4: Uso avanzado con argumentos
resultado = (lambda x, y, z: x * y + z)(2, 3, 1)
# La función se define y se ejecuta inmediatamente con los argumentos 2, 3 y 1
# resultado = 7



# Casos de uso



"""......................"""

# Funcion Recursiva

# Ejemplos: 

# Ejemplo 1: Cálculo de factorial de un número de forma recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

resultado = factorial(5)  # resultado = 120


# Ejemplo 2: Cálculo de la serie de Fibonacci de forma recursiva
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

resultado = [fibonacci(i) for i in range(10)]  # resultado = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Ejemplo 3: Búsqueda binaria de un elemento en una lista de forma recursiva
def busqueda_binaria(lista, elemento, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return False

    medio = (inicio + fin) // 2

    if lista[medio] == elemento:
        return True
    elif lista[medio] > elemento:
        return busqueda_binaria(lista, elemento, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, elemento, medio + 1, fin)

lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
encontrado = busqueda_binaria(lista_ordenada, 6)  # encontrado = True


# Ejemplo 4: Cálculo de la suma de elementos en una lista de forma recursiva
def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

lista_numeros = [1, 2, 3, 4, 5]
resultado = suma_lista(lista_numeros)  # resultado = 15


# Casos de uso: 

# Recorrido de Árboles
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def suma_nodos_arbol(nodo):
    if not nodo:
        return 0
    else:
        suma = nodo.valor
        for hijo in nodo.hijos:
            suma += suma_nodos_arbol(hijo)
        return suma

# Crear un árbol
raiz = Nodo(10)
raiz.hijos = [Nodo(5), Nodo(3), Nodo(7)]
raiz.hijos[0].hijos = [Nodo(2), Nodo(1)]

total = suma_nodos_arbol(raiz)  # total = 28


# Torres de Hanoi
def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de torre {origen} a torre {destino}")
        return
    torres_hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de torre {origen} a torre {destino}")
    torres_hanoi(n - 1, auxiliar, destino, origen)

torres_hanoi(3, 'A', 'C', 'B')






"""......................"""

# Funcion Closure

# Ejemplos: 

# Ejemplo 1: Función closure simple que captura una variable del entorno
def crear_incrementador(incremento):
    def incrementar(x):
        return x + incremento
    return incrementar

sumar_cinco = crear_incrementador(5)
resultado = sumar_cinco(10)  # resultado = 15


# Ejemplo 2: Función closure para contar llamadas a una función
def contador_llamadas():
    contador = 0
    def contar():
        nonlocal contador
        contador += 1
        return contador
    return contar

contador = contador_llamadas()
print(contador())  # Resultado: 1
print(contador())  # Resultado: 2


# Ejemplo 3: Función closure para crear funciones personalizadas
def crear_funcion_personalizada(funcion):
    def funcion_personalizada(x, y):
        return funcion(x, y)
    return funcion_personalizada

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

suma_personalizada = crear_funcion_personalizada(suma)
resta_personalizada = crear_funcion_personalizada(resta)

resultado_suma = suma_personalizada(10, 5)  # resultado_suma = 15
resultado_resta = resta_personalizada(10, 5)  # resultado_resta = 5


# Ejemplo 4: Cierre sobre variables mutables (lista)
def crear_acumulador():
    acumulador = []
    def agregar(valor):
        acumulador.append(valor)
        return acumulador
    return agregar

agregar_elemento = crear_acumulador()
print(agregar_elemento(1))  # Resultado: [1]
print(agregar_elemento(2))  # Resultado: [1, 2]



# Casos de uso

# Fábrica de objetos

def crear_persona(nombre, edad):
    def obtener_nombre():
        return nombre

    def obtener_edad():
        return edad

    def cumpleanios():
        nonlocal edad
        edad += 1

    return {
        "nombre": obtener_nombre,
        "edad": obtener_edad,
        "cumpleanios": cumpleanios
    }

persona = crear_persona("Alice", 30)
print(persona["nombre"]())  # "Alice"
print(persona["edad"]())    # 30
persona["cumpleanios"]()
print(persona["edad"]())    # 31


# Crear funciones callbacks
def evento_personalizado(funcion):
    def envolver(*args, **kwargs):
        print("Antes del evento")
        resultado = funcion(*args, **kwargs)
        print("Después del evento")
        return resultado
    return envolver

@evento_personalizado
def funcion_principal():
    print("Ejecutando la función principal")

funcion_principal()


# Gestión de estado
def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

contador1 = contador()
contador2 = contador()

resultado1 = contador1()  # resultado1 = 1
resultado2 = contador1()  # resultado2 = 2
resultado3 = contador2()  # resultado3 = 1


# Funciones fábrica
def crear_sumador(x):
    def sumar(y):
        return x + y
    return sumar

sumar_5 = crear_sumador(5)
resultado = sumar_5(3)  # resultado = 8


# Decoradores
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = funcion(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Alice")  # mensaje = "Hola, Alice!"


# Manejo de estados
def contador_incremetal():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

contar = contador_incremetal()
print(contar())  # 1
print(contar())  # 2


# Funciones de orden superior 
def generar_operador(op):
    def operador(a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        # Otras operaciones
    return operador

suma = generar_operador("+")
resultado = suma(5, 3)  # resultado = 8


# Manejo de eventos GUI
from tkinter import Tk, Button

def crear_handler(mensaje):
    def handler():
        print(mensaje)
    return handler

root = Tk()
boton1 = Button(root, text="Clic Me", command=crear_handler("Botón 1 clickeado"))
boton2 = Button(root, text="Clic Me Too", command=crear_handler("Botón 2 clickeado"))
boton1.pack()
boton2.pack()
root.mainloop()




"""......................"""

# Funcion Callback

# Ejemplo Calculadora

# Ejemplo: Implementación de una función de calculadora con función callback

# Función principal de calculadora
def calculadora(a, b, operacion):
    resultado = operacion(a, b)
    print(f"Resultado: {resultado}")

# Funciones para realizar operaciones matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

# Definición de una función callback para mostrar un mensaje personalizado
def mostrar_mensaje(resultado):
    print(f"El resultado es: {resultado}")

# Usar la calculadora con una función callback
print("Calculadora - Suma:")
calculadora(5, 3, suma)  # Resultado: 8

print("Calculadora - Resta:")
calculadora(5, 3, resta)  # Resultado: 2

print("Calculadora - Multiplicación:")
calculadora(5, 3, multiplicacion)  # Resultado: 15

print("Calculadora - División:")
calculadora(5, 0, division)  # Resultado: Error: división por cero

# Usar la calculadora con la función de callback personalizada
print("Calculadora - Suma con Mensaje:")
resultado = suma(5, 3)
mostrar_mensaje(resultado)  # Resultado: El resultado es: 8



# Casos de uso: 

# Funciones Fábrica
def crear_sumador(x):
    def sumar(y):
        return x + y
    return sumar

sumar_5 = crear_sumador(5)
resultado = sumar_5(3)  # resultado = 8


# Decoradores
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a la función")
        resultado = funcion(*args, **kwargs)
        print("Después de llamar a la función")
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    return f"Hola, {nombre}!"

mensaje = saludar("Alice")  # mensaje = "Hola, Alice!"


# Manejo de Estados
def contador_incremetal():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

contar = contador_incremetal()
print(contar())  # 1
print(contar())  # 2


# Funciones de orden superior
def generar_operador(op):
    def operador(a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        # Otras operaciones
    return operador

suma = generar_operador("+")
resultado = suma(5, 3)  # resultado = 8


# Manejo de Eventos:
from tkinter import Tk, Button

def crear_handler(mensaje):
    def handler():
        print(mensaje)
    return handler

root = Tk()
boton1 = Button(root, text="Clic Me", command=crear_handler("Botón 1 clickeado"))
boton2 = Button(root, text="Clic Me Too", command=crear_handler("Botón 2 clickeado"))
boton1.pack()
boton2.pack()
root.mainloop()


# Manejo de Excepciones
def manejar_error_division_por_cero(e):
    print("Error:", e)

def dividir(a, b, callback_error):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        callback_error(e)
    else:
        return resultado

dividir(5, 0, callback_error=manejar_error_division_por_cero)


# Filtrado de archivos
def procesar_linea(linea):
    return linea.strip().upper()

with open("archivo.txt", "r") as archivo:
    lineas_procesadas = map(procesar_linea, archivo)


# Programación asíncronica
import asyncio

async def tareas_asincronas():
    print("Tarea 1")
    await asyncio.sleep(1)
    print("Tarea 2")

loop = asyncio.get_event_loop()
loop.run_until_complete(tareas_asincronas())


# Funciones como objetos de primera clase
def saludar(nombre):
    return f"Hola, {nombre}!"

def ejecutar_funcion(funcion, argumento):
    resultado = funcion(argumento)
    return resultado

mensaje = ejecutar_funcion(saludar, "Juan")
print(mensaje)  # Salida: "Hola, Juan!"


# Personalización del comportamiento
def saludar(nombre):
    return f"Hola, {nombre}!"

def ejecutar_funcion(funcion, argumento):
    resultado = funcion(argumento)
    return resultado

mensaje = ejecutar_funcion(saludar, "Juan")
print(mensaje)  # Salida: "Hola, Juan!"


# Callbacks anónimos
def operacion_binaria(a, b, funcion):
    return funcion(a, b)

resultado = operacion_binaria(5, 3, lambda x, y: x * y)  # resultado = 15


# Bibliotecas y frameworks
import requests

def procesar_respuesta(respuesta):
    # Personalizar el procesamiento de la respuesta aquí
    pass

url = "https://ejemplo.com/api/datos"
response = requests.get(url, callback=procesar_respuesta)


# Lectura de archivos asíncrono
import asyncio

async def leer_archivo(nombre, callback):
    # Simular una lectura de archivo asincrónica
    await asyncio.sleep(2)
    contenido = "Contenido del archivo"
    callback(contenido)

def procesar_archivo(datos):
    print(f"Datos del archivo: {datos}")

asyncio.run(leer_archivo("archivo.txt", procesar_archivo))


# Peticiones de Red
import requests

def manejar_respuesta(respuesta):
    if respuesta.status_code == 200:
        print("Respuesta exitosa:", respuesta.text)
    else:
        print("Error en la respuesta:", respuesta.status_code)

url = "https://ejemplo.com/api/datos"
requests.get(url, callback=manejar_respuesta)


# Temporizadores y retrasos
import time

def ejecutar_despues_de_delay(segundos, callback):
    time.sleep(segundos)
    callback()

def tarea():
    print("Tarea ejecutada después del retraso")

ejecutar_despues_de_delay(2, tarea)


# Biblioteca GUI (ejemplo simplificado)
class Boton:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.click_handler = None

    def on_click(self, handler):
        self.click_handler = handler

    def click(self):
        if self.click_handler:
            self.click_handler(self.etiqueta)

def guardar_click(etiqueta):
    print(f"Botón '{etiqueta}' clickeado. Guardando datos...")

boton_guardar = Boton("Guardar")
boton_guardar.on_click(guardar_click)
boton_guardar.click()


# Ordenamiento personalizado
numeros = [5, 2, 8, 1, 6]

def ordenar_por_cifra_unidad(numero):
    return numero % 10

numeros_ordenados = sorted(numeros, key=ordenar_por_cifra_unidad)
# números_ordenados = [1, 2, 5, 6, 8]





