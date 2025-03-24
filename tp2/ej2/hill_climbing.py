
'''Codigo para el problema de los barriles en el juego "Coders of the Caribbean"'''

import sys
import math
import random

def evaluation(ship, barrel):
    return abs(barrel[0] - ship[0]) + abs(barrel[1] - ship[1])

def hill_climbing(ship, barrels):
    distance_min = float('inf')
    current_dist = 0
    best_barrel = ()
    next_position = None

    for barrel in barrels:
        current_dist = evaluation(ship, barrel)
        
        if current_dist < distance_min:  # el barril actual está más cerca
            distance_min = current_dist
            best_barrel = barrel
        elif current_dist == distance_min:
            # si tienen la misma distancia, elegir el barril con más ron
            if barrel[2] > best_barrel[2]:
                best_barrel = barrel

    if not best_barrel:  # no hay barriles, se mueve aleatoriamente
        random_x = random.randint(0, 22)  # randint incluye ambos extremos
        random_y = random.randint(0, 20)
        next_position = (random_x, random_y)
    else:
        next_position = (best_barrel[0], best_barrel[1])

    return next_position

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
        nextPosition = hill_climbing (ship, barrels)
        print(f"MOVE {nextPosition[0]} {nextPosition[1]}")