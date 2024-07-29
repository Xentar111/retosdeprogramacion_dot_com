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
            lado_minimo = min(poligono)
            
            if len(poligono) > 2:
                #Es un rectangulo
                pass
            
            numeros_borrar = [lado_base, lado_minimo]
            
            lado_restante = list(poligono)
            for lado in numeros_borrar:
                while lado in lado_restante:
                    lado_restante.remove(lado)
            lado_restante = lado_restante[0]
            #extraer_numeros = {lado_minimo, lado_base}
            #lado_restante = tuple(x for i, x in enumerate(poligono) if i not in extraer_numeros)
            #lado_restante = tuple(x for x in poligono not in (lado_base, lado_minimo))
            
            print(lado_base)
            print(lado_minimo)
            print(lado_restante)
                

if __name__ == '__main__':
    #poligono_elegido = input("Ingresa el poligono que deseas: 1.Triangulo, 2.Cuadrado, 3.Rectangulo ")
    #if poligono_elegido == 1:
    #    input("Ahora los tres lados")
    
    triangulo = (3,2,5)
    area_poligono(triangulo)
#Método Recursivo:
