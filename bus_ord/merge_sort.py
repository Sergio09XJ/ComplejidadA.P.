import random 

def merge_sort (lista): 
   if len(lista) > 1:  # Checamos que la lista sea mayor a uno para poder dividirla. 
    

      medio = len(lista) // 2  #Dividimos la longitud de la lista a la mitad sin puntos decimales.  
      izquierda = lista[:medio] #Guardamos la primera mitad en izquierda 
      derecha = lista[medio:] #Guardamos la segunda mitad en derecha 
      
      #Usamos recursivdad para dividr la lista hasta que tengan un solo valor 
      merge_sort(izquierda)  
      merge_sort(derecha)


      i = 0 #Iterador de Izquierda 
      j = 0 #Iterador de Derecha
      k = 0 #Iterador Nueva lista 

      while i < len(izquierda) and j < len(derecha):
         if izquierda[i] < derecha[j]: 
           lista[k] = izquierda[i]
           i += 1 
           k += 1
         else:
           lista[k] = derecha[j]
           j += 1 
           k += 1

      while i < len(izquierda):
          lista[k] = izquierda[i]
          i += 1 
          k += 1

      while j < len(derecha): 
          lista[k] = derecha[j]
          j += 1 
          k += 1
      print(lista)     
      print("\n--------- Vuelta -------")
   return lista
   


if __name__ == "__main__": 
   
   lista_s = [random.randint(0, 100) for i in range(10)]

   print(f"La lista antes de ser ordena: {lista_s}\n")
   print(f"La lista  despues de ser ordena: {merge_sort(lista_s)}\n")