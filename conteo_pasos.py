#Este código lo usamos como ejemplo para el conteo de los pasos que tiene. 

def f(x): 
 respuesta = 0 # 1 paso
 
 for i in range(1000):  # 1000 pasos
  respuesta += 1
  
 for i in range(x):  # x pasos
  respuesta += 1 
 
 for i in range(x): # x pasos
    for j in range(x): #x pasos
    #Estos 2 ciclos pueden multiplicar por que por cada ciclo de i se 
    # hacen tantos ciclos de j  
    # x * x = x^2  
      respuesta += 1  #1 pasos
      respuesta += 1   #1 pasos
      
 return respuesta  #1 pasos

print(f(100))