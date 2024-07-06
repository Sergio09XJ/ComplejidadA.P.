from bokeh.plotting import figure, show, output_file

def grafica_bokeh(labels, values_l, values_b, circulo): 

    output_file("grafica_variada.html")
    graf = figure(title = "Grafica de Complejidad Algoritmica", x_axis_label = "Eje X", y_axis_label = "Cantidad de pasos: ")

    graf.line(labels, values_l, legend_label = "Lineas", color = "Blue", line_width = 2)
    graf.vbar(x= labels, top= values_b, legend_label="Barras", width=  0.3, bottom= 0, color="Green")
    graf.scatter(labels, circulo, legend_label="Circulos", color="#bb5566", size= 9 )

    show(graf)

if __name__ == "__main__": 
    
    x = [1,2,3,4,5,6,7,8,9,10]
    lineal = [1,4,9,16,25,36,49,64,91,100]
    barras =[1,8,27,64,125,216,343,512,729,1000]
    ciculos = [1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

    grafica_bokeh(x,lineal, barras, ciculos)