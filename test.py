class App():
    def __init__(self):
        pass

def vector_no(n):
    if (n <= 0) :
        return n
    print(n) 
    return vector_no(n-1)

def vector_on(i,n):
    if (i > n) :
        return 
    print(i)
    return vector_on(i + 1, n)


def fibonacci(n):
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

def fibonacci_bucle(n):
    vect = []

    for i in range(n):
        if (i == 0):
            vect.append(0)
        elif (i == 1):
            vect.append(1)
        else:
            vect.append(vect[i-1]+vect[i-2])

    print(vect)

def factorial(n):
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    return n * factorial(n -1) 

def matriz_nxn(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    for fila in matriz:
        print(fila)

if __name__ == '__main__':
    app = App()
    # for i in range(20):
    #     print(fibonacci(i))

    # fibonacci_bucle(10)
