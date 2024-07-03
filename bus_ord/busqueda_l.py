


#Creamos la funcion busqueda_lineal con el objeto buscar un valor en una lista de números. 
def busqueda_lineal(lista, objeto): 
    match = False #Retornaremos este valor con el objetivo de saber si fue encontrado o no. 
    cont = 0 # Inicializamos en 0 el contador 
    cont_list = [] #Inicializamos la lista donde iran los contadores
    "O(n) Complejidad Algoritmica Lineal."
    for elemento in lista:  #Iteramos cada elemento en la lista. 
        print(f"Buscando el {objeto} entre {elemento} y {lista[len(lista)-1]}")
        cont += 1 #Sumamos 1 cada vez que itere en la lista. 
        cont_list.append(cont)
        if elemento == objeto:  # Si un elemento es igual al valor del objeto a buscar 
            match = True # Cambiamos el valor de match para True
            break #Rompemos el ciclo para no iterar de mas, si encontramos el valor. 

    return match, cont, cont_list  #Retornamos match si es True o False. 

#Este if nos sirve para usar el programa sea que un script o un modulo. 
if __name__ == "__main__":

  busqueda_lineal()    
  #lista, objeto