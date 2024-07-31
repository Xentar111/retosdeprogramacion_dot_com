# 
# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
# 

#Método Iterativo (con ciclo for):
import math
def area_poligono(poligono:tuple):
    #print(type(poligono))
    if isinstance (poligono, tuple):
        if len(poligono) > 1:
            hipotenusa = max(poligono)
            lado_minimo = min(poligono)
            
            if len(poligono) > 2:
                numeros_borrar = [hipotenusa, lado_minimo]
                
                lado_restante = list(poligono)
                for lado in numeros_borrar:
                    while lado in lado_restante:
                        lado_restante.remove(lado)
                #print(type(lado_restante))
                lado_restante = lado_restante[0]
                
                #extraer_numeros = {lado_minimo, hipotenusa}
                #lado_restante = tuple(x for i, x in enumerate(poligono) if i not in extraer_numeros)
                #lado_restante = tuple(x for x in poligono not in (hipotenusa, lado_minimo))
                
                area = lado_minimo * lado_restante / 2
                
                #print(hipotenusa)
                #print(lado_minimo)
                #print(lado_restante)#L
                
                #pass
                print("Area de un triangulo: ", int(area))
                #print(math.sqrt(altura))
            elif len(poligono) < 3 and len(poligono) > 1:
                #Es un isoseles
                lado_maximo = max(poligono)
                lado_minimo = min(poligono)
                area = lado_maximo * lado_minimo
                print("Area de un Rectangulo: ", area)
            else:
                pass
            
        elif len(poligono) < 2:
            lado_minimo = min(poligono)
            area = lado_minimo  **2
            print("Area de un cuadrado: ", area)
                

if __name__ == '__main__':
    #poligono_elegido = input("Ingresa el poligono que deseas: 1.Triangulo, 2.Cuadrado, 3.Rectangulo ")
    #if poligono_elegido == 1:
    #    input("Ahora los tres lados")
    
    rectangulo = (10, 6, 8)#Mal entendido pense que era rectangulo triangulo
    triangulo_equilatero = (2, 5)#Pasa a ser el rectangulo
    cuadrado = (5,)#Este es cuadrado
    area_poligono(rectangulo)
    area_poligono(cuadrado)
    area_poligono(triangulo_equilatero)

#Método Recursivo:
