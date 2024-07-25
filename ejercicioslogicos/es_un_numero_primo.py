# 
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
# 

import numpy as np

#range_haundred = np.arange(1,100)
range_haundred = range(1, 100)
primos = []

def numero_primo(integer:int, isanprimo:bool=False):
    #Método Iterativo (con ciclo for):
    if primos:
        for i in primos:
            isanprimo = integer % i == 0
        if isanprimo == True:
            primos.append(integer)
    else:
        isanprimo = integer % integer == 0
        if isanprimo == True:
            primos.append(integer)
    
    #Método Recursivo:

if __name__ == '__main__':
    for i in range_haundred:
        numero_primo(i)
    print(primos)