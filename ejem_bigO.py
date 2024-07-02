#Ley de la multiplicación 

def f(n): 
    for i in range(n): 

        for j in range(n): 
            print(i, j)

# O(n) * O(n) = O(n * n) = O(n^2)            

f(10)