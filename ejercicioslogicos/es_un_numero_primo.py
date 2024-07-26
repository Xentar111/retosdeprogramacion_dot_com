# 
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
# 

import numpy as np

#range_haundred = np.arange(1,100)
range_haundred = range(1, 101)
primos = []
divisores = []

def numero_primo():
    #Método Iterativo (con ciclo for):
    numero = int(input('Ingresa un numero: '))
    is_an_primo = []
    count = 0
    if isinstance(numero, int):
        if numero > 1:
            for i in range(1, numero):
                is_an_primo.append(numero % i == 0)
            print('Lista is_an_primo: ', len(is_an_primo))
            #print(is_an_primo)
            for condition in is_an_primo:
                if condition == True:
                    count += 1
            #print(count)
            if count < 2:
                print(f'{numero} - Es un primo.')
            elif count > 2:
                print(f'{numero} - No es un numero primo.')
            
        else:
            print(f'{numero} - No es un numero primo')
    else:
        print(f'{numero} - No es un numero')
    #Método Recursivo:
    #numero % 2 == 0

if __name__ == '__main__':
    numero_primo()