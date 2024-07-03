import busqueda_b #Importamos el modulo busqueda_b
import busqueda_l#Importamos el modulo busqueda_l
import charts#Importamos el modulo charts
import random #Importamos el modulo random

longitud = int(input("Dame el tamaño de tu lista: ")) #Pedimos el tamaño de la lista. 
valor = int(input("Dime que valor quieres encontrar: ")) #El valor que queremos encontrar en la lista.
lista = sorted([random.randint(0, 100) for i in range(longitud)]) #Con randint y un for, iteramos por cada valor del tamaño de la lista y con randint creamos un número a guardadar en esa lista de forma al azar. 

print(" ") #Salto de linea. 
encontrado_l, iteraciones_l, lista_l = busqueda_l.busqueda_lineal(lista, valor) #Guardamos los valores de retorno de la función en cada variable
print(" ")#Salto de linea. 
encontrado_b, iteraciones_b, lista_b = busqueda_b.busqueda_b(lista, 0, longitud, valor, cont = 0)#Guardamos los valores de retorno de la función en cada variable
print(" ")#Salto de linea. 

print(f"\n{lista}\n") #Imprimimos la lista. 
print(f"\nLa cantidad de iteraciones en la B. Lineal es: {iteraciones_l}")#Imprimimos la cantidad de iteraciones para encontrar el valor. 
print(f"La cantidad de iteraciones en la B. Lineal es: {iteraciones_b}\n")#Imprimimos la cantidad de iteraciones para encontrar el valor. 

print(f"\n La cantidad de iteraciones en el algoritmo lineal: {lista_l}")#Imprimimos la lista con cada valor de iteración
print(f"La cantidad de iteraciones en el algoritmo binario: {lista_b}\n")#Imprimimos la lista con cada valor de iteración

print(f"El elemento en la busqueda lineal {'esta' if encontrado_l else 'no esta'} en la lista. ")#Imprimimos si encontramos el valor en la lista o no. 
print(f"El elemento en la busqueda binaria {'esta' if encontrado_b else 'no esta'} en la lista. ")#Imprimimos si encontramos el valor en la lista o no. 

charts.generar_graf_barra(len(lista), lista_l, lista_b)#Llamamos a la función generar_graf_barra y le damos los valores de la lista de iteración. 