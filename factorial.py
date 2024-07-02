import time #Importamos la libreria time para medir el tiempo de Ejecución
import sys #Importamos la libreria sys para aumentar el limite de iteraciones. 


#Creamos la función factorial de forma normal. 
def facto_n(n): #Acepta un número. 
    resultado = 1 #Variable que será multiplicada por cada dígito, desde n hasta 1.  
    while n > 1: #Ciclo que iterara por cada número para multiplicar. 
       resultado *= n #Multiplicamos resultado por cada número. 
       n -= 1 #Restamos 1 para la siguente iteración. 
    return resultado   #Terminado el ciclo retornamos el resultado.  


#Creamos la función factorial con recursividad. 
def facto_r(n): #Acepta el Número. 
   if n == 1: #Caso base, si n es igual a 1:
      return 1 #Retorna 1
   else: 
    return n * facto_r(n-1) #Si n no es igual a 1 retorna la multiplicación de n por n-1 y así hasta que n sea 1. 
   
if __name__ == "__main__":  #Nos aseguramos de que el archivo funcione como modulo o en este caso como script. 
    
    sys.setrecursionlimit(1000000) #Aumentamos el limite de iteración en la recursión a 1,000,000
    sys.set_int_max_str_digits(1000000) #Aunmentamos el limite de transformar int en str a 1,000,000

    n = 200000 #valor de n. 
    
    comienzo = time.time() #Medimos el tiempo desde el inicio y lo guardamos en comienzo. 
    ((facto_n(n))) #Llamamos a la función normal e imprimimos el resultado
    final = time.time() #Medimos el tiempo despues de llamar a la función
    print(final-comienzo) #Imprimos el tiempo que se tardo en ejecutar toda la función, restando final - comienzo. 
    # 1,000 = 0.000476837158203125
    # 10,000 = 0.03763294219970703
    # 50,000 = 1.0766687393188477
    # 100,000 = 4.484386920928955
    # 200,000 = 18.908496141433716
    


    print("\n") #Salto de Linea. 

    comienzo = time.time() #Medimos el tiempo desde el inicio y lo guardamos en comienzo. 
    ((facto_r(n))) #Llamamos a la función normal e imprimimos el resultado
    final = time.time() #Medimos el tiempo despues de llamar a la función
    print(final-comienzo) #Imprimos el tiempo que se tardo en ejecutar toda la función, restando final - comienzo. 
    # 1,000 = 0.0004680156707763672
    # 10,000 = 0.03763294219970703
    # 50,000 = 0.9654848575592041
    # 100,000 = 4.091000080108643
    # 200,000 = 17.36562991142273
