import random
import pprint
from constants import *

def build_routine():
    current_movement = START_END_POSITION
    routine = [START_END_POSITION]
    for x in range(ROUTINE_LENGTH):
        new_movement = {
            'body_direction': get_body_direction(current_movement['body_direction']),
            'num_feet': get_num_feet(current_movement['num_feet']),
            'attributes': {}
        }

        if new_movement['num_feet'] == ONE_FOOT:
            new_movement['attributes']['ground_foot'] = get_leg()
            new_movement['attributes']['is_in_air'] = get_active_leg()
            new_movement['attributes']['air_direction'] = get_a_terre_position()
            if new_movement['attributes']['is_in_air'] == 'EN_LAIR':
                new_movement['attributes']['air_position'] = get_en_lair_position()

        elif new_movement['num_feet'] == TWO_FEET:
            new_movement['attributes']['front_foot'] = get_leg()
            new_movement['attributes']['ground_postiion'] = get_feet_position()
        else:
            new_movement['attributes']['movement_direction'] = get_movement_direction()

        routine.append(new_movement)
        current_movement = new_movement

    routine.append(START_END_POSITION)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(routine)

def get_body_direction(prev_dir):
    rand_num = random.uniform(0, 1)

    if prev_dir == EFFACE:
        if rand_num < 0.2:
            return ENFACE
        elif rand_num < 0.4:
            return EFFACE
        else:
            return CROISE
    elif prev_dir == ENFACE:
        if rand_num < 0.2:
            return ENFACE
        elif rand_num < 0.5:
            return EFFACE
        else:
            return CROISE
    else:
        if rand_num < 0.3:
            return ENFACE
        else:
            return CROISE

def get_num_feet(prev_pos):
    rand_num = random.uniform(0, 1)

    if prev_pos == ONE_FOOT:
        if rand_num < 0.1:
            return NO_FEET
        elif rand_num < 0.4:
            return ONE_FOOT
        else:
            return TWO_FEET
    elif prev_pos == TWO_FEET:
        if rand_num < 0.3:
            return NO_FEET
        else:
            return ONE_FOOT
    else:
        if rand_num < 0.5:
            return ONE_FOOT
        else:
            return TWO_FEET

def get_leg():
    rand_num = random.uniform(0, 1)
    if rand_num < 0.5:
        return RIGHT
    else:
        return LEFT

def get_movement_direction():
    rand_num = random.uniform(0, 1)

    if rand_num < 0.1:
        return BACKWARD
    elif rand_num < 0.3:
        return LEFT
    elif rand_num < 0.5:
        return BACK
    else:
        return FORWARD

def get_feet_position():
    rand_num = random.uniform(0, 1)
    if rand_num < 0.2:
        return SECOND
    else:
        return FIFTH

def get_active_leg():
    rand_num = random.uniform(0, 1)
    if rand_num < 0.5:
        return EN_LAIR
    else:
        return A_TERRE

def get_a_terre_position():
    rand_num = random.uniform(0, 1)
    if rand_num < 0.33:
        return FRONT
    elif rand_num < 0.66:
        return SIDE
    else:
        return BACK

def get_en_lair_position():
    rand_num = random.uniform(0, 1)
    if rand_num < 0.25:
        return BATTEMENT
    elif rand_num < 0.50:
        return ATTITUDE
    elif rand_num < 0.75:
        return PASSE
    else:
        return COUPE

build_routine()
