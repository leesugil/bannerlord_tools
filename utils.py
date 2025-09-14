# utils.py

import pyautogui as pa
import pydirectinput as pi
import math

def dist(x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)

def check_rgb(data, tolerance=20):
    x = data['x']
    y = data['y']
    captured_rgb = pa.pixel(x, y)
    supposed_rgb = (data['r'], data['g'], data['b'])
    dist_tolerance = tolerance
    return (dist(captured_rgb, supposed_rgb) < dist_tolerance)

def check_rgbs(data, tolerance=20):
    pi.moveTo(3, 1)
    pi.moveTo(1, 1, duration=0.5)
    output = True
    for check in data:
        if check_rgb(check, tolerance):
            output = (output and True)
        else:
            output = False
    return output

def is_world_map_paused():
    rgbs = [
        { 'x': 613, 'y': 686, 'r': 168, 'g': 168, 'b': 168 },
        { 'x': 638, 'y': 687, 'r': 198, 'g': 198, 'b': 198 },
        { 'x': 677, 'y': 688, 'r': 211, 'g': 211, 'b': 211 },
        ]
    pi.moveTo(1, 1)
    return check_rgbs(rgbs)


def is_game_loaded_fresh():
     rgbs = [
        { 'x': 1123, 'y': 350, 'r': 175, 'g': 9, 'b': 9 },
        { 'x': 1124, 'y': 373, 'r': 175, 'g': 9, 'b': 9 },
        ]
     pi.moveTo(1, 1)
     return check_rgbs(rgbs)
