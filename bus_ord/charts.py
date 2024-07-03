import matplotlib.pyplot as plt #Importamso la libreria matplotlib y el modulo pyplot como plt 

def generar_graf_pie(labels, values): #Creamos la función. 
   fig, ax = plt.subplots() #Creamos el fig(lienzo) y el ax(marco) en donde haremos la gráfica. 
   ax.pie(labels, values) #Le decimos el tipo de grafica, los valores y en donde ira(ax - marco)
   plt.show() #la mostramos


def generar_graf_barra(labels, v_lineal, v_binario):  #Creamos la función grafia de barras. 
   fig, ax = plt.subplots()#Creamos el fig(lienzo) y el ax(marco) en donde haremos la gráfica. 

   ax.bar(labels, v_lineal,  color='r', label='Iteraciones Lineal') #Le decimos el tipo de grafica, los valores del eje "x"(values) y del "y"(labels, y en donde ira(ax - marco)
   ax.bar(labels, v_binario, color='b', label='Iteraciones Binario')#Le decimos el tipo de grafica, los valores del eje "x"(values) y del "y"(labels, y en donde ira(ax - marco)


   plt.xlabel("Valores de Eje X")#Titulo del eje x 
   plt.ylabel("Valores de Iteración")#Titulo del eje y 
   plt.title("Comparación de Complejidad Algorimica") #Titulo de la gráfica

   plt.savefig("Graf_comparacion.jpg") #En vez de mostrara con plt.show(), la guardamos en el archivo Graf_comparacion.jpg  con plt.savefig()

#Este if nos sirve para usar el programa sea que un script o un modulo. 
if __name__ == "__main__": 
   
   generar_graf_barra()