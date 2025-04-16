import sys
import math
import random

width, height = [int(i) for i in input().split()]
directions = [(0,-1), (0,1), (1,0), (-1, 0)]
current_coord = (1,2) #inicial coordenate
current_id = 1 #inicial id ROOT
turn_number = 0

def is_neighbor(coord, x, y):
    '''Function that checks if the coordinate specified by x and y is adjacent to the tuple coord. '''
    dx = abs(x - coord[0])
    dy = abs(y - coord[1])
    
    return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

def h(coord, proteinA_list):
    '''Heuristic function'''
    return min(abs(px - coord[0]) + abs(py - coord[1]) for (px, py) in proteinA_list)

def schedule(turn): #esquema de enfriamiento
    return max(0, 100 - turn)

def simulated_annealing(current_coord, neighbor_list, proteinA_list, turn_number):
    '''Funcion para el simulated annealing'''
    new_coord = ()
    
    temperature = schedule(turn_number) #La temperatura se calcula en base al turno
    print(f'temperature {temperature}', file=sys.stderr, flush=True)
    if temperature == 0:
        new_coord = current_coord #Si la temperatura es 0, devuelvo actual
    
    next = random.choice(neighbor_list) #Elijo uno de los vecinos al azar

    delta_E = h(next, proteinA_list) - h(current_coord, proteinA_list)  #∆E ← VALOR(siguiente) - VALOR(actual)  Siendo VALOR el resultado de la heuristica
    print(f'delta_E {delta_E}', file=sys.stderr, flush=True)
    
    if delta_E < 0:
        new_coord = next
    else:
        probability = math.exp(-delta_E / temperature )
        print(f'probability {probability}', file=sys.stderr, flush=True)
        if (random.random() < probability):
            new_coord = next
    return new_coord

# game loop
while True:
    turn_number = turn_number + 1 #Incremento mi contador de turno

    proteinA_list = []
    neighbor_list = [(current_coord[0] + dx, current_coord[1] + dy) for (dx, dy) in directions]

    entity_count = int(input())
    for i in range(entity_count):
        inputs = input().split()
        x = int(inputs[0])
        y = int(inputs[1])  # grid coordinate
        _type = inputs[2]  # WALL, ROOT, BASIC, TENTACLE, HARVESTER, SPORER, A, B, C, D
        owner = int(inputs[3])  # 1 if your organ, 0 if enemy organ, -1 if neither
        organ_id = int(inputs[4])  # id of this entity if it's an organ, 0 otherwise
        organ_dir = inputs[5]  # N,E,S,W or X if not an organ
        organ_parent_id = int(inputs[6])
        organ_root_id = int(inputs[7])
       
        if (x == current_coord[0] and y == current_coord[1] and owner == 1 and (_type == 'ROOT' or _type == 'BASIC')):
            current_id = organ_id

        if ((_type == 'WALL' or ((_type == 'BASIC' or _type == 'ROOT')  and owner == 1)) and is_neighbor(current_coord, x, y)):
            neighbor_list.remove((x,y))

        if (_type == 'A'):
            proteinA_list.append((x,y))

    # my_d: your protein stock
    my_a, my_b, my_c, my_d = [int(i) for i in input().split()]
    # opp_d: opponent's protein stock
    opp_a, opp_b, opp_c, opp_d = [int(i) for i in input().split()]
    
    required_actions_count = int(input())  # your number of organisms, output an action for each one in any order
    for i in range(required_actions_count):
        print(neighbor_list, file=sys.stderr, flush=True)
        if neighbor_list:
            new_coord = simulated_annealing(current_coord, neighbor_list, proteinA_list, turn_number)
            print(f'new_coord {new_coord}', file=sys.stderr, flush=True)
            if (new_coord == current_coord):
                print(f'WAIT')
            else:
                current_coord = new_coord
                print(f"GROW {current_id} {current_coord[0]} {current_coord[1]} BASIC")
        else:
            print(f'WAIT')
