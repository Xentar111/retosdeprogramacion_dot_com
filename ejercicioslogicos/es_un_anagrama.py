"""
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagram(text1:str, text2:str) -> bool:
    if text1 == text2:
        return False
    if text1 != text2:
        text1 = text1.lower()
        text2 = text2.lower()
        
        text2_list = list(text2)
        text1_list = list(text1)
        
        text1_list.sort()
        text2_list.sort()
        
        print(text1_list)
        print(text2_list)
        
        if text1_list == text2_list:
            return True
        else:
            return False
            

def another_anagram(text1:str, text2:str) -> bool:
    text1 = text1.lower()
    text2 = text2.lower()
    
    text2_list = list(text2)
    text1_list = list(text1)
    
    text1_list.sort()
    text2_list.sort()
    
    text1_sorted = "".join(text1_list)
    text2_sorted = "".join(text2_list)
    
    return text1_sorted == text2_sorted

#dict ->

if __name__ == '__main__':
    print(anagram('hola', 'hola'))
    print(anagram('hoLa', 'Hola'))
    print(anagram('hola', 'aloh'))
    print(anagram('hola', 'alohhkjad'))
    #
    print(another_anagram('hola', 'hola'))
    print(another_anagram('hoLa', 'Hola'))
    print(another_anagram('hola', 'aloh'))
    print(another_anagram('hola', 'alohhkjad'))