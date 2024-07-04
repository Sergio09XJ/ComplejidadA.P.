import random #Importamos la función Random para la lista a ordenar. 

"Complejidad Algoritmica Polinomica O(n**2)"
def ordena_burbuja(lista): #Creamos la función para ordenar una lista por el método de la burbuja. 
    n = len(lista) #Guardamos la longitu de la lista en la variable n

    for i in range(n): #Primer ciclo for, itera la cantidad de veces de longitud de la lista.Su función es 
        #iterar varias veces para ordenar los valores que no se ordenaron en la segunda lista. 
        for j in range(0,n - i -1):# Segundo ciclo for, este se encarga de ordenar la lista en base al if. 

            if lista[j] > lista[j + 1]: #Si el valor que itera es mayor que el que le sigue. 
               lista[j], lista[j + 1] = lista[j + 1], lista[j] #Intercambialos en la lista. 
    return lista    #Cuando la lista este lista la retornamos.         

if __name__ == "__main__": #Permite usar el archivo como modulo o como script. 
    long = int(input("Dame el tamaño de tu lista: \n")) #Pedimos el tamaño de la lista. 
    lista = [random.randint(0, 100) for i in range(long)] #Usando random creamos valores para la lista y con el for iteramos para llenarla

    print(f"\nLista antes de ordenar: {lista}") #Imprimimos la lista antes de ser ordenada.
    print(f"\nLista despues de ordenar: {ordena_burbuja(lista)}") #La imprimimos despues de ser ordenada. 
