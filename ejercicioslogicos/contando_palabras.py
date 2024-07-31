# 
# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
#   lo resuelvan automáticamente.
# 


#Método Iterativo (con ciclo for):
texto = 'Hol[a] como {estas.|\\ . '
def count_string(word_to_count:str):
    word_lower = word_to_count.lower().split()
    print(word_lower)
    #word_clean = [x for x in word_lower if not './\\{}[]']
    word_clean = []
    for i in word_lower:
        #print(i.replace('./\\{[]', ''))
        word_clean.append(i.replace(']', ''))
    print(word_clean)

count_string(texto)
#Método Recursivo: