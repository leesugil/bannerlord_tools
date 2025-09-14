# autonomous_driving_module.py
# you rarely need this part if you control in-game
# interruption-related variables
# such as ruling no kingdom, having no enemies, etc.

import pyautogui as pa
import pydirectinput as pi
import utils
import time
import gps_module as gps

def check_if_coordinates_set_right(dest):
    # work in progress
    output = False
    x = dest['x_test']
    y = dest['y_test']
    r = dest['r_test']
    g = dest['g_test']
    b = dest['b_test']
    # wait, holding right click and scrolling changes angle!
    output = True # under construction
    return output

def start_travel_to_destination(dest):
    # if x, y are player character portrait,
    # instead of zooming into city,
    # x, y will zoom to player,
    # x_zoom, y_zoom will click a nearby place.
    # detect this, and try x_alt, y_alt if it's the case
    x = dest['x']
    y = dest['y']
    pi.moveTo(x, y, duration=1)
    pi.click(x, y)
    for i in range(4):
        time.sleep(1)

    zoomed_in = False
    if check_if_coordinates_set_right(dest):
        zoomed_in = True
        print("...verified that the gps module identified the location correctly")
    else:
        """
        # try x_alt, y_alt
        print("...location verification failed. error.")
        # don't do anything and report failure
        """
        pass # under construction
    if zoomed_in:
        x = dest['x_zoom']
        y = dest['y_zoom']
        pi.moveTo(x, y, duration=1)
        is_clicked = False
        while not is_clicked:
            pi.click(x, y)
            time.sleep(0.5)
            if utils.is_world_map_paused():
                print("... I swear I clicked! but it wasn't registered, doing it again!")
            else:
                is_clicked = True
        pi.press('3')
    else:
        pa.hotkey('alt', 'tab')
        input("Cannot click town names from GPS: maybe some icons are blocking it")

def check_arrived_to_destination():
    rgb_data = [
        { 'x': 70, 'y': 6, 'r': 38, 'g': 38, 'b': 17 },
        { 'x': 487, 'y': 7, 'r': 63, 'g': 65, 'b': 41 },
        { 'x': 4, 'y': 46, 'r': 56, 'g': 51, 'b': 40 },
        { 'x': 1267, 'y': 54, 'r': 58, 'g': 55, 'b': 42 },
        ]
    return utils.check_rgbs(rgb_data)

def check_forced_make_peace_with_khuzait():
    decision_rgbs = [
        { 'x': 601, 'y': 309, 'r': 228, 'g': 197, 'b': 154 },
        { 'x': 641, 'y': 310, 'r': 194, 'g': 166, 'b': 131 },
        { 'x': 653, 'y': 311, 'r': 227, 'g': 196, 'b': 153 },
        { 'x': 681, 'y': 366, 'r': 178, 'g': 172, 'b': 161 },
        { 'x': 687, 'y': 365, 'r': 156, 'g': 149, 'b': 139 },
        { 'x': 711, 'y': 365, 'r': 151, 'g': 144, 'b': 135 },
        ]

    return utils.check_rgbs(decision_rgbs)

def check_forced_make_peace_with_aserai():
    """
    You need to resolve Make Peace With Aserai decision.
    """
    decision_rgbs = [
        { 'x': 600, 'y': 310, 'r': 143, 'g': 122, 'b': 96 },
        { 'x': 641, 'y': 311, 'r': 227, 'g': 196, 'b': 153 },
        { 'x': 593, 'y': 366, 'r': 144, 'g': 137, 'b': 127 },
        { 'x': 623, 'y': 366, 'r': 157, 'g': 151, 'b': 141 },
        { 'x': 662, 'y': 366, 'r': 129, 'g': 125, 'b': 116 },
        { 'x': 683, 'y': 366, 'r': 170, 'g': 164, 'b': 153 },
        ]

    return utils.check_rgbs(decision_rgbs)

def check_forced_ownership_of_onica():
    rgb_data = [
        { 'x': 604, 'y': 308, 'r': 226, 'g': 194, 'b': 152 },
        { 'x': 641, 'y': 314, 'r': 202, 'g': 173, 'b': 136 },
        { 'x': 653, 'y': 312, 'r': 185, 'g': 158, 'b': 124 },
        { 'x': 642, 'y': 366, 'r': 177, 'g': 170, 'b': 159 },
        { 'x': 655, 'y': 365, 'r': 166, 'g': 158, 'b': 148 },
        { 'x': 673, 'y': 367, 'r': 177, 'g': 170, 'b': 159 },
        { 'x': 691, 'y': 367, 'r': 168, 'g': 162, 'b': 151 },
        { 'x': 695, 'y': 365, 'r': 148, 'g': 141, 'b': 131 },
        ]
    return utils.check_rgbs(rgb_data)

def open_kingdom_menu():
    # add more conditions as needed
    pi.press('k')

def check_voluntary_make_peace_with_khuzait():
    """
    Do you want to resolve Make Peace With Khuzait decision?
    It will be automatically resolved in x hours.
    """
    decision_rgbs = [
        { 'x': 601, 'y': 303, 'r': 229, 'g': 197, 'b': 154 },
        { 'x': 619, 'y': 308, 'r': 226, 'g': 195, 'b': 153 },
        { 'x': 640, 'y': 303, 'r': 202, 'g': 173, 'b': 136 },
        { 'x': 654, 'y': 303, 'r': 196, 'g': 168, 'b': 132 },
        { 'x': 638, 'y': 360, 'r': 147, 'g': 140, 'b': 130 },
        { 'x': 699, 'y': 361, 'r': 179, 'g': 172, 'b': 161 },
        { 'x': 703, 'y': 358, 'r': 170, 'g': 164, 'b': 153 },
        { 'x': 718, 'y': 361, 'r': 165, 'g': 158, 'b': 148 },
        { 'x': 728, 'y': 357, 'r': 140, 'g': 134, 'b': 124 },
        { 'x': 732, 'y': 361, 'r': 152, 'g': 145, 'b': 136 },
        ]

    return utils.check_rgbs(decision_rgbs)

def check_voluntary_make_peace_with_aserai():
    decision_rgbs = [
        { 'x': 601, 'y': 304, 'r': 228, 'g': 197, 'b': 154 },
        { 'x': 629, 'y': 312, 'r': 224, 'g': 194, 'b': 152 },
        { 'x': 664, 'y': 307, 'r': 214, 'g': 184, 'b': 145 },
        { 'x': 677, 'y': 311, 'r': 223, 'g': 193, 'b': 151 },
        { 'x': 609, 'y': 360, 'r': 171, 'g': 166, 'b': 154 },
        { 'x': 638, 'y': 359, 'r': 155, 'g': 148, 'b': 138 },
        { 'x': 673, 'y': 358, 'r': 118, 'g': 111, 'b': 103 },
        { 'x': 698, 'y': 359, 'r': 182, 'g': 174, 'b': 163 },
        { 'x': 726, 'y': 357, 'r': 127, 'g': 119, 'b': 110 },
        ]

    return utils.check_rgbs(decision_rgbs)

def check_voluntary_ownership_of_onica():
    rgb_data = [
        { 'x': 602, 'y': 308, 'r': 217, 'g': 187, 'b': 146 },
        { 'x': 612, 'y': 305, 'r': 227, 'g': 196, 'b': 153 },
        { 'x': 620, 'y': 307, 'r': 218, 'g': 188, 'b': 148 },
        { 'x': 640, 'y': 305, 'r': 185, 'g': 159, 'b': 124 },
        { 'x': 653, 'y': 303, 'r': 201, 'g': 173, 'b': 135 },
        { 'x': 677, 'y': 308, 'r': 226, 'g': 195, 'b': 153 },
        { 'x': 607, 'y': 360, 'r': 145, 'g': 139, 'b': 130 },
        { 'x': 652, 'y': 358, 'r': 155, 'g': 148, 'b': 136 },
        { 'x': 659, 'y': 359, 'r': 107, 'g': 99, 'b': 92 },
        { 'x': 671, 'y': 357, 'r': 151, 'g': 144, 'b': 134 },
        { 'x': 692, 'y': 359, 'r': 132, 'g': 126, 'b': 117 },
        ]
    return utils.check_rgbs(rgb_data)

def check_still_in_kingdom_menu():
    rgb_data = [
        { 'x': 62, 'y': 12, 'r': 27, 'g': 53, 'b': 95 },
        { 'x': 416, 'y': 4, 'r': 35, 'g': 33, 'b': 21 },
        { 'x': 1200, 'y': 25, 'r': 127, 'g': 147, 'b': 171 },
        ]
    return utils.check_rgbs(rgb_data)

def resolve_make_peace_with_khuzait():
    pi.moveTo(907, 381, duration=1)
    pi.click(907, 381) # choose no
    pi.moveTo(804, 660, duration=0.5)
    pi.click(804, 660) # click Done
    for i in range(7):
        time.sleep(1) # wait until Bannerlord processes the decision

    decision_outcome_rgbs = [
        { 'x': 551, 'y': 305, 'r': 208, 'g': 179, 'b': 140 },
        { 'x': 575, 'y': 308, 'r': 226, 'g': 195, 'b': 153 },
        { 'x': 587, 'y': 309, 'r': 236, 'g': 195, 'b': 152 },
        { 'x': 597, 'y': 311, 'r': 224, 'g': 193, 'b': 151 },
        { 'x': 605, 'y': 304, 'r': 220, 'g': 190, 'b': 149 },
        { 'x': 645, 'y': 301, 'r': 224, 'g': 193, 'b': 150 },
        { 'x': 672, 'y': 305, 'r': 219, 'g': 188, 'b': 148 },
        { 'x': 694, 'y': 307, 'r': 213, 'g': 183, 'b': 144 },
        { 'x': 714, 'y': 307, 'r': 223, 'g': 193, 'b': 152 },
        { 'x': 727, 'y': 310, 'r': 225, 'g': 194, 'b': 152 },
        ]

    while not utils.check_rgbs(decision_outcome_rgbs):
        time.sleep(0.5)

    pi.moveTo(642, 418, duration=0.5)
    pi.click(642, 418) # click Ok

def resolve_voluntary_make_peace_with_khuzait():
    pi.moveTo(726, 424, duration=0.5)
    pi.click(726, 424) # click Ok
    time.sleep(0.5)
    resolve_make_peace_with_khuzait()

def resolve_forced_make_peace_with_khuzait():
    pi.moveTo(636, 417, duration=0.5)
    pi.click(636, 417) # click Ok
    time.sleep(0.5)
    resolve_make_peace_with_khuzait()

def resolve_make_peace_with_aserai():
    pi.moveTo(907, 381, duration=1)
    pi.click(907, 381) # choose no
    pi.moveTo(804, 660, duration=0.5)
    pi.click(804, 660) # click Done
    for i in range(7):
        time.sleep(1) # wait until Bannerlord processes the decision

    decision_outcome_rgbs = [
        { 'x': 551, 'y': 305, 'r': 208, 'g': 179, 'b': 140 },
        { 'x': 575, 'y': 308, 'r': 226, 'g': 195, 'b': 153 },
        { 'x': 587, 'y': 309, 'r': 236, 'g': 195, 'b': 152 },
        { 'x': 597, 'y': 311, 'r': 224, 'g': 193, 'b': 151 },
        { 'x': 605, 'y': 304, 'r': 220, 'g': 190, 'b': 149 },
        { 'x': 645, 'y': 301, 'r': 224, 'g': 193, 'b': 150 },
        { 'x': 672, 'y': 305, 'r': 219, 'g': 188, 'b': 148 },
        { 'x': 694, 'y': 307, 'r': 213, 'g': 183, 'b': 144 },
        { 'x': 714, 'y': 307, 'r': 223, 'g': 193, 'b': 152 },
        { 'x': 727, 'y': 310, 'r': 225, 'g': 194, 'b': 152 },
        ]

    while not utils.check_rgbs(decision_outcome_rgbs):
        time.sleep(0.5)

    pi.moveTo(642, 418, duration=0.5)
    pi.click(642, 418) # click Ok

def resolve_voluntary_make_peace_with_aserai():
    pi.moveTo(726, 424, duration=0.5)
    pi.click(726, 424) # click Ok
    time.sleep(0.5)
    resolve_make_peace_with_aserai()

def resolve_forced_make_peace_with_aserai():
    pi.moveTo(639, 416, duration=0.5)
    pi.click(639, 416) # click Ok
    time.sleep(0.5)
    resolve_make_peace_with_aserai()

def resolve_ownership_of_onica():
    pi.moveTo(728, 422, duration=0.5)
    pi.click(728, 422) # click Ok
    pi.moveTo(569, 356, duration=0.5)
    pi.click(569, 356) # click player's opinion
    pi.moveTo(798, 659, duration=0.5)
    pi.click(798, 659) # click done
    for i in range(7):
        time.sleep(1) # wait until game processes the decision

    decision_outcome_rgbs = [
        { 'x': 592, 'y': 304, 'r': 220, 'g': 190, 'b': 148 },
        { 'x': 603, 'y': 304, 'r': 186, 'g': 160, 'b': 125 },
        { 'x': 644, 'y': 302, 'r': 183, 'g': 157, 'b': 123 },
        { 'x': 651, 'y': 302, 'r': 227, 'g': 195, 'b': 152 },
        { 'x': 672, 'y': 303, 'r': 215, 'g': 185, 'b': 146 },
        ]

    while not utils.check_rgbs(decision_outcome_rgbs):
        time.sleep(0.5)

    pi.moveTo(645, 422, duration=0.5)
    pi.click(645, 422) # click Ok

def resolve_voluntary_ownership_of_onica():
    pi.moveTo(728, 422, duration=0.5)
    pi.click(728, 422) # click Ok
    time.sleep(0.5)
    resolve_ownership_of_onica()

def resolve_forced_ownership_of_onica():
    pi.moveTo(638, 412, duration=0.5)
    pi.click(638, 412) # click Ok
    time.sleep(0.5)
    resolve_ownership_of_onica()

def check_in_war_with_vlandia():
    # inside the kingdom menu
    pi.moveTo(996, 84, duration=0.5)
    pi.click(996, 84) # click Diplomacy
    time.sleep(0.5)
    rgb_data = [
        { 'x': 7, 'y': 7, 'r': 31, 'g': 30, 'b': 23 },
        { 'x': 848, 'y': 10, 'r': 48, 'g': 44, 'b': 34 },
        { 'x': 20, 'y': 353, 'r': 112, 'g': 31, 'b': 19 },
        { 'x': 36, 'y': 376, 'r': 238, 'g': 185, 'b': 65 },
        ]
    return utils.check_rgbs(rgb_data)


def make_peace_with_vlandia():
    # inside the diplomacy screen
    pi.moveTo(205, 376, duration=0.5)
    pi.click(205, 376) # click Vlandia
    pi.move(855, 744, duration=0.5)
    pi.click(855, 744) # click Propose
    pi.moveTo(685, 369, duration=0.5)
    pi.click(685, 369) # click player's proposal
    pi.moveTo(805, 656, duration=0.5)
    pi.click(805, 656) # click Done
    
    # check Decision Outcome pop up
    rgb_data = [
        { 'x': 552, 'y': 295, 'r': 229, 'g': 197, 'b': 154 },
        { 'x': 563, 'y': 296, 'r': 229, 'g': 197, 'b': 154 },
        { 'x': 590, 'y': 296, 'r': 154, 'g': 131, 'b': 103 },
        { 'x': 604, 'y': 296, 'r': 229, 'g': 197, 'b': 154 },
        { 'x': 650, 'y': 294, 'r': 222, 'g': 191, 'b': 149 },
        ]
    while not utils.check_rgbs(rgb_data):
        time.sleep(1)
    pi.moveTo(642, 428, duration=0.5)
    pi.click(642, 428) # click Ok
    time.sleep(0.5)

def close_kingdom_menu():
    pi.moveTo(642, 789)
    pi.click(642, 789) # click Done
