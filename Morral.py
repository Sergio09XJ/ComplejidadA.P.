#Problema del Morral 1 -0 knapsack - Problema del Morral

def morral(tamaño, masas, valores, n): 
    #Primera Funcíon Morral - Usando if para compara valores y encontrar el máximo. 
    if tamaño == 0 or n == 0: #Si el tamaño de la mochila es 0 o el iterador llega 0..
        return 0 #retorna 0
    else: #Si no..
        if masas[n-1] > tamaño:  #Si el valor de la masa en la que esta el iterador es mayor a la máxima capacidad de la M. 
          return morral(tamaño, masas, valores, n-1) #Pasa al siguiente valor. 
    
        incluir_v = valores[n-1] + morral(tamaño - masas[n-1], masas, valores, n-1) #En esta varíable guardamos el valor. 
        excluir_v = morral(tamaño, masas, valores, n-1) #Esta deja pasar el valor 
        #Estas 2 llamadas Se usan para guardar los distinos ecenarios en los que puede estar el máximo valor 
        if incluir_v > excluir_v: #Este cóndicional lo usamos para encontra el máximo valor(similar a la f. max)
            return incluir_v #Si incluir_v es mayor a ex. retorna incluir_v. 
        else: 
            return excluir_v #Pero si es el caso contrario retoran excluir_v
          

#Segunda Función Morral - Usando la función max como buscador del máximo valor. 
def morral_2(tamaño, masas, valores, n): #Pedimos el tamaño que puede soportar el morral, una lista de pesos y otra de valores, y n, lo usaremos como iterador en las listas. 
    if n == 0 or tamaño == 0: #Caso base: Cuando n(indice de las listas) sea 0 o el tamaño del morral sea 0(llego a su máxima capacidad)
        return 0 #Retorna 0. 
    if  masas[n-1] > tamaño: #Si la masa por la que estamos pasando, supera el peso de la mochila. 
        return morral_2(tamaño, masas, valores, n-1) #Retorna la función morral pero restale 1 a n para iterar sobre el siguiente valor. 
    #Si no es ninguno de los casos anteriores...
    return max(valores[n-1] + morral_2(tamaño - masas[n-1], masas, valores, n-1), 
               morral_2(tamaño, masas, valores, n-1))
    #Retorna el valor del morral + la función de este pero restando a tamaño la masa y menos 1 a n para el siguiente valor o ...
    #Retorna el morral pero restando 1 a n para seguir iterando. 
    #En este punto se crean dos ramas una donde tomal el valor y otra donde no, max las compara y retorna el máximo valor, sea 1 o la suma de varios. 

if __name__ == "__main__": #Este if lo usamos para permitir al archivo se usado como script o modulo. 
    valores = [100, 120, 60] #Creamos la variable valores. 
    masas  = [20 ,30, 10]#Creamos la variable masas.
    tamaño = 30 #Definimos el tamaño de la mochila. 
    n = len(valores) #N es el iterador y es la longitud de valores. 


    resultado = morral(tamaño, masas, valores, n) #Guardamos en resultado el return de morral. 
    print(f"El valor máximo del algoritmo 1 es:  {resultado}") #Lo imprimimos con una frase. 

    resultado_2 = morral_2(tamaño, masas, valores, n) #Guardamos en resultado  de return de morral_2
    print(f"El valor máximo del algoritmo 2 es:  {resultado_2}") #Lo imprimimos con una frase. 
    
   



