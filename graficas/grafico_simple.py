from bokeh.plotting import figure, output_file, show 
#Importamos la libreria y de esta importamos las funciones. 

if __name__ == "__main__": #Este if nos permite tratar al archivo como un modulo o como un script. 

    output_file("graficado_s.html") #Con esta función llamamos al archivo en el directorio(Le damos el nombre).
    fig = figure(title = "Grafica con inputs", x_axis_label = "Eje X", y_axis_label = "Eje Y") #Creamos el lienzo sobre el cual se hara la grafica, le ponemos titulo a esta y a los ejes. 

    value_t = int(input("Cuantos valores quieres aplicar: ")) #Pedimos el número de valores para los ejes. 
    vals_x = list(range(value_t)) #Esto lo que hace es que con el número de valores crea una lista en forma acendente partiendo desde 0
    vals_y = [] #Creamos la lista de la "y"

    for x in vals_x: 
        vals_y.append(int(input(f"Dame el valor de (y) para {x}: "))) #Pedimos el valor de y para cada valor  de x 

    fig.line(vals_x, vals_y, color = "green", line_width  = 2) #Creamos el grafico en si, con los valores de "x" y "y" y le damos color a la linea y anchura. 
    show(fig)    #Mostramos la figura. 