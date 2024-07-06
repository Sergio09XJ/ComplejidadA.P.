from bokeh.plotting import figure, show, output_file
#Importamos la libreria y de esta importamos las funciones. 
import random #Importamos la función random

x = [random.randint(1,100) for i in range(6)] #Creamos los valores para "x" de forma aleatorea y con un limite de 6
y_c = [random.randint(1,100)for i in range(6)] #Creamos los valores para "y 1" de forma aleatorea y con un limite de 6
y_u = [random.randint(1,100)for i in range(6)] #Creamos los valores para "y 2" de forma aleatorea y con un limite de 6
y_d = [random.randint(1,100)for i in range(6)] #Creamos los valores para "y 3" de forma aleatorea y con un limite de 6


figura = figure(title = "Gestion Monetaria en la Empresa_ ", x_axis_label = "Eje X", y_axis_label = "Eje Y")
#Creamos el lienzo sobre el cual se hara la grafica, le ponemos titulo a esta y a los ejes. 

#Creamos las lineas en base a las y´s con titulos, color y anchura. 
figura.line(x, y_c, legend_label = "Ganancias", color = "green", line_width = 2)
figura.line(x, y_u, legend_label = "Perdidas", color = "blue",  line_width = 2)
figura.line(x, y_d, legend_label = "Robos", color = "red",  line_width = 2)


show(figura) #Mostramos la figura. 

