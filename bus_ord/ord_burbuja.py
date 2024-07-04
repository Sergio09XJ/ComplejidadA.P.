import random 

def ordena_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0,n - i -1):

            if lista[j] > lista[j + 1]:
               lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista            

if __name__ == "__main__":
    long = int(input("Dame el tamaño de tu lista: \n"))
    lista = [random.randint(0, 100) for i in range(long)]

    print(f"\nLista antes de ordenar: {lista}")
    print(f"\nLista despues de ordenar: {ordena_burbuja(lista)}")
