import random 

def ord_insert(lista):
  # [21, 79, 0, 0, 21, 70, 86, 54, 18, 29]
  
  "Complejidad Algorítmica de O(n**2)"
  for i in range(1, len(lista)):  #Inicialisamos la lista desde 1 hasta la longitud de la lista. 
    key = lista[i] # En key agregamos el valor la lista pero mas uno, porque inicialisamos la lista un valor despues 
    j = i - 1 # j es i pero menos 1, para compararlo con el valor anterior a el inidice i.

    # Mientras j sea mayor o igual a 0 y key sea menor al valor anterior a estes. 
    while j >= 0 and key < lista[j]: 
       lista[j + 1] = lista[j] #El valor mayor(j) lo pasamos adelante 
       j -= 1 #y restamos 1 a j para la siguiente comparación(iteración en while)
    
    lista[j + 1] = key #En caso de que j sea menor al 0(El primer indice de la lista) o key sea mayor al valor de la lista que le sigue. 
    #Agregamos a j + 1 el valor de key, no sea hace nada o en caso de que j sea menor a 0 le sumamos 1 para poner a k en el primer valor de la lista. 
  return lista #Retornamos la función 
     


if __name__ == "__main__": 
   
   lista_s = [random.randint(0, 100) for i in range(10)]

   print(f"La lista antes de ser ordena: {lista_s}\n")
   print(f"La lista  despues de ser ordena: {ord_insert(lista_s)}\n")


