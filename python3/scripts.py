#Funciones

#primeras funciones



#...............

#return vs no return



#...............

#funcion, variable, return

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

#...............




#Calcular promedio

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


#...............


# Tupla/Registros en función

def obtener_informacion_persona(nombre, edad, ciudad):
    """
    Obtiene información de una persona y la devuelve como una tupla.
    """
    informacion = (nombre, edad, ciudad)
    return informacion

# Uso de la función

nombre = "Juan"
edad = 30
ciudad = "Madrid"

informacion_persona = obtener_informacion_persona(nombre, edad, ciudad)

# Desempaquetar la tupla
nombre_persona, edad_persona, ciudad_persona = informacion_persona

# Imprimir la información de la persona
print("Nombre:", nombre_persona)
print("Edad:", edad_persona)
print("Ciudad:", ciudad_persona)


"""..........."""


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


#...............





"""..........."""

#Instrucciones



#...............





#...............






"""..........."""

#Estructuras de control





#...............






#...............





"""..........."""

# Estructuras de datos


#caracteres

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


#...............

#listas

frutas = ['manzana', 'banana', 'kiwi', 'naranja']
print(frutas)               # Imprime: ['manzana', 'banana', 'kiwi', 'naranja']
print(frutas[0])            # Imprime: manzana
frutas.append('mango')
print(frutas)               # Imprime: ['manzana', 'banana', 'kiwi', 'naranja', 'mango']


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


# Crear una lista
numeros = [1, 2, 3, 4, 5]

# Acceder a elementos de una lista
print(numeros[0])  # Salida: 1
print(numeros[3])  # Salida: 4

# Modificar elementos de una lista
numeros[2] = 10
print(numeros)  # Salida: [1, 2, 10, 4, 5]

# Iterar sobre una lista
for numero in numeros:
    print(numero)

# Salida:
# 1
# 2
# 10
# 4
# 5

# Obtener la longitud de una lista
print(len(numeros))  # Salida: 5

# Agregar elementos al final de una lista
numeros.append(6)
print(numeros)  # Salida: [1, 2, 10, 4, 5, 6]

# Insertar elementos en una posición específica
numeros.insert(2, 3)
print(numeros)  # Salida: [1, 2, 3, 10, 4, 5, 6]

# Eliminar elementos de una lista
numeros.remove(3)
print(numeros)  # Salida: [1, 2, 10, 4, 5, 6]

# Ordenar una lista
numeros.sort()
print(numeros)  # Salida: [1, 2, 4, 5, 6, 10]

# Revertir el orden de una lista
numeros.reverse()
print(numeros)  # Salida: [10, 6, 5, 4, 2, 1]

# Copiar una lista
copia_numeros = numeros.copy()
print(copia_numeros)  # Salida: [10, 6, 5, 4, 2, 1]

# Convertir una lista en una tupla
numeros_tupla = tuple(numeros)
print(numeros_tupla)  # Salida: (10, 6, 5, 4, 2, 1)



#...............


#tuplas/registros/celdas

coordenadas = (3, 4)
print(coordenadas)          # Imprime: (3, 4)
print(coordenadas[0])       # Imprime: 3


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


# Crear una tupla
frutas = ("manzana", "banana", "cereza")

# Acceder a elementos de una tupla
print(frutas[0])  # Salida: manzana
print(frutas[1])  # Salida: banana

# Iterar sobre una tupla
for fruta in frutas:
    print(fruta)

# Salida:
# manzana
# banana
# cereza

# Obtener la longitud de una tupla
print(len(frutas))  # Salida: 3

# Comprobar si un elemento está presente en una tupla
if "manzana" in frutas:
    print("La manzana está en la tupla")

# Salida: La manzana está en la tupla

# Concatenar tuplas
numeros1 = (1, 2, 3)
numeros2 = (4, 5, 6)
numeros_concatenados = numeros1 + numeros2
print(numeros_concatenados)  # Salida: (1, 2, 3, 4, 5, 6)

# Desempaquetar una tupla
fruta1, fruta2, fruta3 = frutas
print(fruta1)  # Salida: manzana
print(fruta2)  # Salida: banana
print(fruta3)  # Salida: cereza

# Convertir una tupla en una lista
frutas_lista = list(frutas)
print(frutas_lista)  # Salida: ['manzana', 'banana', 'cereza']

# Convertir una lista en una tupla
frutas_tupla = tuple(frutas_lista)
print(frutas_tupla)  # Salida: ('manzana', 'banana', 'cereza')



#...............


#diccionarios/maps/hash 

persona = {
    'nombre': 'Juan',
    'edad': 30,
    'profesion': 'ingeniero'
}
print(persona)                      # Imprime: {'nombre': 'Juan', 'edad': 30, 'profesion': 'ingeniero'}
print(persona['nombre'])            # Imprime: Juan
persona['edad'] = 31
print(persona)                      # Imprime: {'nombre': 'Juan', 'edad': 31, 'profesion': 'ingeniero'}


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


# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "México"
}

# Acceder a valores de un diccionario
print(persona["nombre"])  # Salida: Juan
print(persona["edad"])  # Salida: 30

# Modificar valores de un diccionario
persona["edad"] = 35
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 35, 'ciudad': 'México'}

# Iterar sobre un diccionario
for clave, valor in persona.items():
    print(clave + ":", valor)

# Salida:
# nombre: Juan
# edad: 35
# ciudad: México

# Obtener las claves de un diccionario
claves = persona.keys()
print(claves)  # Salida: dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener los valores de un diccionario
valores = persona.values()
print(valores)  # Salida: dict_values(['Juan', 35, 'México'])

# Comprobar si una clave está presente en un diccionario
if "nombre" in persona:
    print("La clave 'nombre' está presente")

# Salida: La clave 'nombre' está presente

# Añadir una nueva clave y valor a un diccionario
persona["ocupacion"] = "Programador"
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 35, 'ciudad': 'México', 'ocupacion': 'Programador'}

# Eliminar una clave y su valor de un diccionario
del persona["ciudad"]
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 35, 'ocupacion': 'Programador'}

# Obtener la longitud de un diccionario
longitud = len(persona)
print(longitud)  # Salida: 3




#...............


#conjuntos/sets

numeros = {1, 2, 3, 4, 5}
print(numeros)                  # Imprime: {1, 2, 3, 4, 5}
numeros.add(6)
print(numeros)                  # Imprime: {1, 2, 3, 4, 5, 6}


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


#...............

#colas/queues

import queue

cola = queue.Queue()
cola.put("elemento1")
cola.put("elemento2")
print(cola.get())               # Imprime: elemento1
print(cola.get())               # Imprime: elemento2


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


#...............

#pilas/stacks

pila = []
pila.append("elemento1")
pila.append("elemento2")
print(pila.pop())               # Imprime: elemento2
print(pila.pop())               # Imprime: elemento1


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


#...............


#árbol

class Nodo:
    """
    Clase que representa un nodo en un árbol binario.
    Cada nodo tiene un valor y puede tener hasta dos hijos: izquierdo y derecho.
    """
    def __init__(self, valor):
        """
        Inicializa un nuevo nodo con el valor proporcionado.
        """
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


def insertar(raiz, valor):
    """
    Inserta un nuevo valor en un árbol binario.
    Si el árbol está vacío, el valor se convierte en la raíz.
    Si el valor ya existe en el árbol, no se realiza ninguna acción.
    """
    if raiz is None:
        return Nodo(valor)
    else:
        if valor == raiz.valor:
            return raiz
        elif valor < raiz.valor:
            raiz.izquierdo = insertar(raiz.izquierdo, valor)
        else:
            raiz.derecho = insertar(raiz.derecho, valor)
        return raiz


def buscar(raiz, valor):
    """
    Busca un valor en un árbol binario.
    Devuelve True si el valor se encuentra en el árbol, False en caso contrario.
    """
    if raiz is None or raiz.valor == valor:
        return raiz is not None
    elif valor < raiz.valor:
        return buscar(raiz.izquierdo, valor)
    else:
        return buscar(raiz.derecho, valor)


# Uso del árbol

arbol = None

# Insertar valores en el árbol
arbol = insertar(arbol, 10)
arbol = insertar(arbol, 5)
arbol = insertar(arbol, 15)
arbol = insertar(arbol, 3)
arbol = insertar(arbol, 7)

# Buscar valores en el árbol
print(buscar(arbol, 10))  # Devuelve True
print(buscar(arbol, 7))   # Devuelve True
print(buscar(arbol, 20))  # Devuelve False


#segundo árbol

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


#................

#grafo

class Grafo:
    """
    Clase que representa un grafo no dirigido.
    Utiliza un diccionario para almacenar los vértices y sus conexiones.
    """
    def __init__(self):
        """
        Inicializa un nuevo grafo vacío.
        """
        self.vertices = {}

    def agregar_vertice(self, vertice):
        """
        Agrega un nuevo vértice al grafo.
        """
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        """
        Agrega una nueva arista (conexión) entre dos vértices en el grafo.
        """
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append(vertice2)
            self.vertices[vertice2].append(vertice1)

    def obtener_conexiones(self, vertice):
        """
        Devuelve una lista de los vértices conectados a un vértice dado.
        """
        if vertice in self.vertices:
            return self.vertices[vertice]
        else:
            return []

    def __str__(self):
        """
        Devuelve una representación de cadena del grafo.
        """
        grafo_str = ""
        for vertice in self.vertices:
            grafo_str += f"{vertice}: "
            grafo_str += ", ".join(str(v) for v in self.vertices[vertice])
            grafo_str += "\n"
        return grafo_str


# Uso del grafo

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

# Obtener conexiones de un vértice
conexiones_A = grafo.obtener_conexiones("A")
print(conexiones_A)  # Devuelve ['B', 'E']

# Imprimir el grafo completo
print(grafo)


#segundo grafo

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


#................

#bytes

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


#................

#bytearray

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


#................

#frozenset

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



"""..........."""

# POO 
# Clases

#constructor init

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



# Uso basico de una clase

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


#............


# Carrito de compras

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


#...............

# Biblioteca: agregar y buscar libros

# Clase abstracta Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_informacion(self):
        raise NotImplementedError("Método obtener_informacion no implementado")


# Clase concreta LibroImpreso que hereda de Libro
class LibroImpreso(Libro):
    def __init__(self, titulo, autor, num_paginas):
        super().__init__(titulo, autor)
        self.num_paginas = num_paginas

    def obtener_informacion(self):
        return f"Libro impreso: {self.titulo} - {self.autor}, {self.num_paginas} páginas"


# Clase concreta LibroDigital que hereda de Libro
class LibroDigital(Libro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato

    def obtener_informacion(self):
        return f"Libro digital: {self.titulo} - {self.autor}, formato: {self.formato}"


# Función para buscar libros por título
def buscar_libro_por_titulo(libros, titulo):
    for libro in libros:
        if libro.titulo.lower() == titulo.lower():
            return libro
    return None


# Uso de la abstracción para administrar la biblioteca
biblioteca = []

# Agregar libros a la biblioteca
libro1 = LibroImpreso("Cien años de soledad", "Gabriel García Márquez", 400)
libro2 = LibroDigital("El principito", "Antoine de Saint-Exupéry", "PDF")
biblioteca.append(libro1)
biblioteca.append(libro2)

# Buscar un libro por título
titulo_buscar = "Cien años de soledad"
libro_encontrado = buscar_libro_por_titulo(biblioteca, titulo_buscar)
if libro_encontrado:
    print(libro_encontrado.obtener_informacion())
else:
    print("Libro no encontrado.")


"""..........."""

#Metodos

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





"""..........."""

# Programación funcional

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


#...............

# Ejemplo de programación funcional

# Función pura
def duplicar(numero):
    return numero * 2

# Función de orden superior
def aplicar_funcion(func, lista):
    return list(map(func, lista))

# Datos
numeros = [1, 2, 3, 4, 5]

# Aplicar función pura a los datos
resultados = aplicar_funcion(duplicar, numeros)

# Imprimir resultados
print(resultados)  # Imprime: [2, 4, 6, 8, 10]


#...............




"""..........."""