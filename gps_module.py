# gps_module.py

import time
import pyautogui as pa
import pydirectinput as pi
import utils

screen_size = pa.size()
x_mid = int(screen_size[0]/2)
y_mid = int(screen_size[1]/2)

def set_satellite_angle():
    pa.moveTo(x_mid, y_mid)
    pa.move(10, 0, duration=0.5)
    pi.mouseDown(button='right')
    for i in range(20):
        pi.move(0, 100)
        time.sleep(0.1)
    pi.mouseUp(button='right')

def launch_satellite():
    print(">> launching the satellite")
    for i in range(50):
        pa.scroll(-10)
        time.sleep(0.1)
    # add more check conditions as needed"
    print("... reached the highest altitute")

def land_satellite():
    print("<< landing the satellite")
    for i in range(50):
        pa.scroll(10)
        time.sleep(0.1)
    print("... landed on the lowest altitute. note that the altitute varies.")

def set_at_gps_satellite_1():
    calibration_complete = False
    pi.moveTo(1, 1)
    test_rgbs = [
        { 'x': 1124, 'y': 448, 'r': 175, 'g': 9, 'b': 9 },
        { 'x': 1124, 'y': 468, 'r': 175, 'g': 9, 'b': 9 },
        ]
    test_rgbs2 = [
        { 'x': 1124, 'y': 449, 'r': 0, 'g': 0, 'b': 0 },
        { 'x': 1125, 'y': 468, 'r': 0, 'g': 0, 'b': 0 },
        ]
    while not calibration_complete:
        # top-left corner
        launch_satellite()
        pi.keyDown('a')
        for i in range(3):
            time.sleep(1)
        pi.keyUp('a')
        pi.keyDown('w')
        for i in range(3):
            time.sleep(1)
        pi.keyUp('w')
        if utils.check_rgbs(test_rgbs):
            calibration_complete = True
        elif utils.check_rgbs(test_rgbs2):
            calibration_complete = True

        else:
            print("sat 1 calibration failed, trying again")
    # add more check conditions as needed
    print("Sat 1 calibration complete")

sat_1_coords = {
    'Pen Cannoc': { 'x': 932, 'y': 721 },
    }

def set_at_gps_satellite_2():
    destination = 'Pen Cannoc'
    calibration_complete = False
    pi.moveTo(1, 1)
    test_rgbs = [
        { 'x': 1165, 'y': 188, 'r': 175, 'g': 9, 'b': 9 },
        { 'x': 1166, 'y': 195, 'r': 175, 'g': 9, 'b': 9 },
        ]
    test_rgbs2 = [
        { 'x': 1165, 'y': 188, 'r': 0, 'g': 0, 'b': 0 },
        { 'x': 1166, 'y': 195, 'r': 0, 'g': 0, 'b': 0 },
        ]
    while not calibration_complete:
        set_at_gps_satellite_1()
        x, y = sat_1_coords[destination]['x'], sat_1_coords[destination]['y']
        pi.moveTo(x, y, duration=0.5)
        pi.click(x, y)
        for i in range(3): # zooming in to Pen Cannoc, giving 4 seconds to your pc
            time.sleep(1)
        launch_satellite()
        if utils.check_rgbs(test_rgbs):
            calibration_complete = True
        elif utils.check_rgbs(test_rgbs2):
            calibration_complete = True
        else:
            print("sat 2 calibration failed, trying again")
    # add more check conditions as needed
    print(f"Sat 2 calibration at {destination} complete")

# from Pan Cannoc
sat_2_coords = {
    'Ostican': {
        'x': 397,
        'y': 207,
        'x_test': 573,
        'y_test': 385,
        'r_test': 28,
        'g_test': 55,
        'b_test': 99,
        'x_zoom': 602,
        'y_zoom': 455,
        'x_trade': 60,
        'y_trade': 481,
        'x_leave': 200,
        'y_leave': 570,
        'y_offset': 0,
        },
    'Rovalt': {
        'x': 590,
        'y': 205,
        'x_test': 598,
        'y_test': 359,
        'r_test': 26,
        'g_test': 52,
        'b_test': 95,
        'x_zoom': 646,
        'y_zoom': 445,
        'x_trade': 60,
        'y_trade': 481,
        'x_leave': 200,
        'y_leave': 570,
        'y_offset': 0,
        },
    'Ocs Hall': {
        'x': 484,
        'y': 302,
        'x_test': 597,
        'y_test': 385,
        'r_test': 28,
        'g_test': 53,
        'b_test': 99,
        'x_zoom': 640,
        'y_zoom': 420,
        'x_trade': 60,
        'y_trade': 428,
        'x_leave': 140,
        'y_leave': 515,
        'y_offset': 0,
        },
    'Pravend': {
        'x': 408,
        'y': 334,
        'x_test': 594,
        'y_test': 385,
        'r_test': 117,
        'g_test': 34,
        'b_test': 20,
        'x_zoom': 628,
        'y_zoom': 430,
        'x_trade': 60,
        'y_trade': 418,
        'x_leave': 140,
        'y_leave': 510,
        'y_offset': -25,
        },
    'Galend': {
        'x': 353,
        'y': 448,
        'x_test': 596,
        'y_test': 386,
        'r_test': 114,
        'g_test': 33,
        'b_test': 20,
        'x_zoom': 682,
        'y_zoom': 432,
        'x_trade': 60,
        'y_trade': 419,
        'x_leave': 140,
        'y_leave': 510,
        'y_offset': -25,
        },
    'Jaculan': {
        'x': 550,
        'y': 473,
        'x_test': 596,
        'y_test': 361,
        'r_test': 123,
        'g_test': 35,
        'b_test': 21,
        'x_zoom': 687,
        'y_zoom': 426,
        'x_trade': 60,
        'y_trade': 453,
        'x_leave': 140,
        'y_leave': 540,
        'y_offset': -25,
        },
    'Sargot': {
        'x': 650,
        'y': 500,
        'x_test': 597,
        'y_test': 360,
        'r_test': 117,
        'g_test': 33,
        'b_test': 20,
        'x_zoom': 637,
        'y_zoom': 330,
        'x_trade': 60,
        'y_trade': 419,
        'x_leave': 140,
        'y_leave': 510,
        'y_offset': -25,
        },
    }
