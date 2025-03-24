import random
import math

def f(x):
    '''Función a minimizar'''
    return 5 + 0.5 * x**2 - 5 * math.cos(3 * x)

def schedule(t, T0=1000):
    '''Enfriamiento lineal simple'''
    return max(T0 - t, 0)

def simulated_annealing(x0, delta, bound, max_iter=10000):
    '''Simulated annealing para buscar el mínimo de f(x)'''

    current = x0
    best = current
    for t in range(max_iter):
        print(f'Iteracion {t} - x: {current}, f(x): {f(current):.3f}')

        T = schedule(t)
        if T == 0:
            break
    
        # Generar un vecino aleatorio
        neighbor = round(current + random.choice([-delta, delta]), 3)
        if bound[0] <= neighbor <= bound[1]:
            # Evaluar la función objetivo en el vecino
            delta_f = f(neighbor) - f(current)
            print(f'Probabilidad: {math.exp(-delta_f/T):.3f}')
            if delta_f < 0 or random.random() < math.exp(-delta_f/T):
                current = neighbor
                if f(current) < f(best):
                    best = current

    return best

def main():
    '''Funcion principal que ejecuta el algoritmo de simulated annealing'''
    x0 = float(input('Ingrese el valor inicial: '))
    delta = 0.5
    bound = (-5, 5)

    x = simulated_annealing(x0, delta, bound)
    print(f'Solución: x = {x:.3f}, f(x) = {f(x):.3f}')

if __name__ == '__main__':
    main()
