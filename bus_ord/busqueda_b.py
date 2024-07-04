" O(log n) Complejidad Algoritmica Logaritmica"
def busqueda_b(lista, comienzo, final, objetivo, cont = 0, cont_list = []): #Creamos la función busqueda_b 
    
  print(f"Buscando el {objetivo} entre {lista[comienzo]} y {lista[final - 1]}") #Generamos un Print Statement 
  cont +=1 #Sumamos 1 al contador
  cont_list.append(cont) #Agregamos cada valor de cont a cont_list. 
  if comienzo > final: # Si comienzo es mayor a final 
    return False, cont, cont_list #Retornamos false, no esta en la lista el objetivo. 
  medio = (comienzo + final) // 2 #En caso de que cortamos a la mitad la lista 

  if lista[medio] == objetivo:  #Si el objetivo es igual al valor de en medio de la lista
    return True, cont, cont_list #Encontramos el valor y es igual a True 
  elif lista[medio] < objetivo:  #En caso de que el valor de en medio sea menor a el objetivo 
    return busqueda_b(lista, medio + 1, final, objetivo, cont)  #Retornamos todo pero desde el valor de en medio hacia arriba de la lista. 
  else: #Si es el caso contrario, el valor de en medio es mayor que el objetivo
   return busqueda_b(lista, comienzo, medio -1, objetivo, cont ) #Retornamos otra vez la busqueda pero desde el valor de en medio hacia abajo de la lista. 
  
  #Los returns de elif y else son recursividad, por lo que se repetiran constantemente hasta llegar al if principal. 
  #En caso de que no, la lista no tiene el número a buscar. 

if __name__ == '__main__':#Este if nos sirve para usar el programa sea que un script o un modulo. 
 
  busqueda_b()#Llamamos a la función busqueda_b
  #lista, 0, longitud, valor, cont = 0



