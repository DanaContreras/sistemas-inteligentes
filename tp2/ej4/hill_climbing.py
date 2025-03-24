import math

def f(x):
    '''Función objetivo (mínimo en x=0)'''
    return 5 + 0.5 * x**2 - 5 * math.cos(3 * x)

def hill_climbing(x0, delta, bound, max_iter=100):
    '''Algoritmo Hill Climbing para minimizar f(x)'''
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        print(f'x: {x:.3f}, f(x): {fx:.3f}')
        
        derecha = x + delta
        izquierda = x - delta
        
        # Verificar que los movimientos estén dentro de los límites
        if bound[0] <= derecha <= bound[1] and f(derecha) < fx:
            x = derecha
        elif bound[0] <= izquierda <= bound[1] and f(izquierda) < fx:
            x = izquierda
        else:
            break  # No hay mejor opción, detenerse
    
    return x

def main():
    '''Función principal'''
    x0 = float(input('Ingrese el valor inicial: '))
    delta = 0.1
    bound = (-5, 5)

    x = hill_climbing(x0, delta, bound)
    print(f'Solución: x = {x:.3f}, f(x) = {f(x):.3f}')

if __name__ == '__main__':
    main()