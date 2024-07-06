import random 
#Función merge_sort = Ordena una lista por el metodo de mezcla. 
def merge_sort (lista): 
   if len(lista) > 1:  # Checamos que la lista sea mayor a uno para poder dividirla. 
    

      medio = len(lista) // 2  #Dividimos la longitud de la lista a la mitad sin puntos decimales.  
      izquierda = lista[:medio] #Guardamos la primera mitad en izquierda 
      derecha = lista[medio:] #Guardamos la segunda mitad en derecha 
      
      #Usamos recursivdad para dividr la lista hasta que tengan un solo valor 
      #Que es cuando se consideran ordenada una lista por defecto. 
      merge_sort(izquierda)  
      merge_sort(derecha)

      i = 0 #Iterador de Izquierda 
      j = 0 #Iterador de Derecha
      k = 0 #Iterador Nueva lista 
      "Complejidad algoritmica sublineal O(n log n)  "
      #Mientras el valor de los iteradores sea menor a la longitud de la lista itera.. 
      while i < len(izquierda) and j < len(derecha):
         if izquierda[i] < derecha[j]: #Si el valor de la izquierda es menor que el de la derecha. 
           lista[k] = izquierda[i] #Guarda ese valor en la lista. 
           i += 1  #Suma 1 a i 
           k += 1 # y a K 
         else: #En caso contrario 
           lista[k] = derecha[j] #Guarda el valor de la derecha en la lista. 
           j += 1 #Suma un valor a j
           k += 1 #Suma un valor a k 

      while i < len(izquierda): #Si sobraron valores en la lista de la izquierda 
          lista[k] = izquierda[i] #Guardalos en la lista principal 
          i += 1  #Suma uno a i 
          k += 1  #Suma otro a k 

      while j < len(derecha):  #Caso contrario, si sobraron valores en la lista de la derecha 
          lista[k] = derecha[j] #Guardalos en la lista principal. 
          j += 1 #Suma un valor a j
          k += 1 #Suma otro valor a k 
 
   return lista #Retornamos la lista ya ordenada. 
   


if __name__ == "__main__": 
   
   lista_s = [random.randint(0, 100) for i in range(10)]

   print(f"La lista antes de ser ordena: {lista_s}\n")
   print(f"La lista  despues de ser ordena: {merge_sort(lista_s)}\n")