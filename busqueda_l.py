import random #Importamos el Modulo Random


#Creamos la funcion busqueda_lineal con el objeto buscar un valor en una lista de números. 
def busqueda_lineal(lista, objeto): 
    match = False #Retornaremos este valor con el objetivo de saber si fue encontrado o no. 

    "O(n) Complejidad Algoritmica Lineal."
    for elemento in lista:  #Iteramos cada elemento en la lista. 
        if elemento == objeto:  # Si un elemento es igual al valor del objeto a buscar 
            match = True # Cambiamos el valor de match para True
            break #Rompemos el ciclo para no iterar de mas, si encontramos el valor. 

    return match  #Retornamos match si es True o False. 

#Este if nos sirve para usar el programa sea que un script o un modulo. 
if __name__ == "__main__":
    tamaño_lista  =int(input("De que tamaño es tu lista? ")) #Pedimos el tamaño de la lista
    objeto = int(input("Que número quieres encontrar? ")) #Pedimos el objeto a buscar. 

    lista = [random.randint(0, 100) for i in range(tamaño_lista)] #usamos un list comprehension y la función random.randit para 
    #crear cada número al azar y un for en base al tamaño de la lista. 
    encontrado = busqueda_lineal(lista, objeto) #Llamamos a la función.

    print(lista) #Imprimimos el valor. 
    #Usamos una concatención en print y tambien usamos operadores ternareos(if, else en una sola linea de código).
    print(f"El elemento {objeto} {'esta' if encontrado else 'no esta'} en la lista. ")     