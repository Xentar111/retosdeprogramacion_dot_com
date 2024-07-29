# 
# Crea una única función (importante que sólo sea una) que sea capaz
# de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
# 


#Método Iterativo (con ciclo for):
def area_poligono(poligono:tuple):
    if isinstance (poligono, tuple):
        if len(poligono) > 1:
            lado_base = max(poligono)
            
            print(lado_base)
                

if __name__ == '__main__':
    #poligono_elegido = input("Ingresa el poligono que deseas: 1.Triangulo, 2.Cuadrado, 3.Rectangulo ")
    #if poligono_elegido == 1:
    #    input("Ahora los tres lados")
    
    triangulo = (3,2,5)
    area_poligono(triangulo)
#Método Recursivo:
