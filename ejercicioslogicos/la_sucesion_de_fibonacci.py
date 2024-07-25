#* Escribe un programa que imprima los 50 primeros números de la sucesión
#* de Fibonacci empezando en 0.
#* - La serie Fibonacci se compone por una sucesión de números en
#*   la que el siguiente siempre es la suma de los dos anteriores.
#*   0, 1, 1, 2, 3, 5, 8, 13...

def fibbo():
    first_number = 0
    second_number = 1
    
    list_fibo = []
    #Método Iterativo (con ciclo for):
    while len(list_fibo) < 50:
        temp = first_number
        first_number = second_number
        list_fibo.append(temp)
        second_number = temp + second_number
        list_fibo.append(second_number)
    
    print(len(list_fibo))
    print(list_fibo)

    #Método Recursivo:
    
if __name__ == '__main__':
    fibbo()