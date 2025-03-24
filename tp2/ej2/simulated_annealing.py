
'''Codigo para el problema de los barriles en el juego "Coders of the Caribbean"'''

import sys
import math
import random

def schedule(t):
    return max(0, t)

def random_position_barrel(barrels):
    '''Se elige un barril de forma aleatoria (vecino aleatorio)'''
    index = random.randint(0, len(barrels) - 1)
    return barrels[index]

def min_distance(position, barrels):
    '''Se determina el barril mas cercano a position'''
    best_barrel = ()
    distance_min = float('inf')

    for barrel in barrels:
        position_barrel = (barrel[0], barrel[1])
        current = distance(position, position_barrel)
        
        if (current < distance_min):
            best_barrel = barrel
            distance_min = current

    return distance_min, best_barrel

def distance(position_1, position_2):
    '''Calcula la distancia de Manhattan'''
    return abs(position_2[0] - position_1[0]) + abs(position_2[1] - position_1[1])

# simulated annealing
def simulated_annealing(position, barrels):
    '''Simulado templado para determinar proxima direccion a moverse'''
    current = position
    new_position = current
    T = schedule(len(barrels))
    
    if (T == 0):
        new_position = position
    else:

        # distancia entre posicion actual del barco y el barril mas proximo
        dist, best_barrel = min_distance(current, barrels)

        next = random_position_barrel(barrels)
        next_position = (next[0], next[1])
        next_distance = distance(current, next_position)
        delta_e = next_distance - dist

        if delta_e < 0:
            new_position = next_position
        elif (random.random() < math.exp(-delta_e / T)):
            new_position = next_position
        else:
            new_position = (best_barrel[0], best_barrel[1])
    
    return new_position

# game loop
while True:
    my_ship_count = int(input())  # the number of remaining ships
    entity_count = int(input())  # the number of entities (e.g. ships, mines or cannonballs)
    barrels = []

    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        x = int(inputs[2])
        y = int(inputs[3])
        arg_1 = int(inputs[4])
        arg_2 = int(inputs[5])
        arg_3 = int(inputs[6])
        arg_4 = int(inputs[7])

        if (entity_type == 'BARREL'):
            rum_amount = arg_1
            barrels.append((x, y, rum_amount))
        elif (entity_type == 'SHIP' and arg_4 == 1):
            ship = (x, y, arg_1, arg_2, arg_3, arg_4)


    for i in range(my_ship_count):
        position = (ship[0], ship[1])
        next_position = simulated_annealing(position, barrels)
        print(f"MOVE {next_position[0]} {next_position[1]}")