#* Escribe un programa que imprima los 50 primeros números de la sucesión
#* de Fibonacci empezando en 0.
#* - La serie Fibonacci se compone por una sucesión de números en
#*   la que el siguiente siempre es la suma de los dos anteriores.
#*   0, 1, 1, 2, 3, 5, 8, 13...

def fibbo():
    first_number = 0
    second_number = 1
    first=True
    list_fibo = []
    
    #Método Iterativo (con ciclo while): (No vale basado en uno que me dio gpt sin while y sin append y sin bool)
    while len(list_fibo) < 50:
        temp = first_number
        if first == True:
            list_fibo.append(first_number)
            first = False
        first_number = second_number
        second_number = second_number + temp
        list_fibo.append(second_number)
    
    print(list_fibo)
    print(len(list_fibo))

    #Método Recursivo:
    
if __name__ == '__main__':
    fibbo()