from bokeh.plotting import figure, show 

def grafica_bokeh(labels, values_l, values_b): 

    graf = figure(title = "Grafica de Complejidad Algoritmica", x_axis_label = "Eje X", y_axis_label = "Cantidad de pasos: ")

    graf.line(labels, values_l, legend_label = "B. Lineal", color = "Blue", line_width = 2)
    graf.vbar(x= labels, top= values_b, legend_label="B. Binaria", width=  0.3, bottom= 0, color="red")
    

    show(graf)

if __name__ == "__main__": 
    grafica_bokeh()