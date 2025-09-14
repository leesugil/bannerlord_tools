import pyautogui as pa
import pydirectinput as pi
import time
import math
import utils
import gps_module as gps
import navigation_module as nav
import ocr_module as ocr

# state variables
cruising = True
is_in_kingdom_menu = True
has_arrived_to_destination = True
on_war_with_vlandia = True
shops_in_vlandia_closed = True

def print_state():
    print(f"    cruising: {cruising}")
    print(f"    is_in_kingdom_menu: {is_in_kingdom_menu}")
    print(f"    has_arrived_to_destination: {has_arrived_to_destination}")
    print(f"    on_war_with_vlandia: {on_war_with_vlandia}")
    print(f"    shops_in_vlandia_closed: {shops_in_vlandia_closed}")

def set_window_focus_on_game():
    # adjust so that alt-tab switches between Python IDLE and Bannerlord
    # change window to Bannerlord game
    pa.keyDown('alt')
    pa.keyDown('tab')
    pa.keyUp('tab')
    pa.keyDown('tab')
    pa.keyUp('tab')
    pa.keyUp('alt')
    time.sleep(0.5)
    # return to python IDLE Shell
    pa.hotkey('alt', 'tab')
    time.sleep(0.5)
    # change to Bannerlord game
    pa.hotkey('alt', 'tab')
    time.sleep(0.5)
    # add more check conditions as needed
    print("window focused on game")

def load_game():
    pi.press('esc') # open main game menu
    time.sleep(0.5)
    pi.moveTo(630, 470)
    pi.click(630, 470) # click load
    time.sleep(1.5)
    pi.moveTo(300, 715)
    pi.click(300, 715) # click ok
    time.sleep(0.5)
    print("loading new iteration")
    time.sleep(0.5)
    # sometimes the loading is not completely finished,
    # causing the script to click a wrong location to Ostican.
    # make sure a new game is loaded.
    passed = False
    while not passed:
        print("...", end='|')
        if utils.is_game_loaded_fresh():
            passed = True
        else:
            passed = False
        time.sleep(1) # check every one second
    print("Iteration reloaded")
    time.sleep(1)


# main control flow
print("✅ script initiated")
set_window_focus_on_game()
towns = [
    'Ostican',
    'Rovalt',
    'Ocs Hall',
    'Pravend',
    'Galend',
    'Jaculan',
    'Sargot',
    ]
counter = 1
while True:
    if utils.is_world_map_paused():
        print(f"✅ n-th iteration started: {counter}")
        gps.set_satellite_angle()
        cruising = False
        is_in_kingdom_menu = False
        has_arrived_to_destination = False
        on_war_with_vlandia = False
        shops_in_vlandia_closed = False
        print_state()
        for t in towns:
            #if t == 'Ostican': continue
            #if t == 'Rovalt': continue
            #if t == 'Ocs Hall': continue
            #if t == 'Pravend': continue
            #if t == 'Galend': continue
            #if t == 'Jaculan': continue
            #if t == 'Sargot': continue
            # GPS module
            town = gps.sat_2_coords[t]

            # Navigation module
            cruising = False
            is_in_kingdom_menu = False
            has_arrived_to_destination = False
            while not has_arrived_to_destination:
                if utils.is_world_map_paused():
                    # maybe,
                    # during the while loop,
                    # maybe player character was traveling,
                    # and a few seconds later,
                    # as soon as the chatacter arrived to destination,
                    # this pause condition is flagged
                    # and satellites will try to calibrate
                    # which will never work.
                    if nav.check_arrived_to_destination():
                        print(f"game paused due to arriving to {t}")
                        cruising = False
                        is_in_kingdom_menu = False
                        has_arrived_to_destination = True
                        print_state()
                    else:
                        print("world map time is paused without arriving to the destination, launching a satellite")
                        gps.set_at_gps_satellite_2()
                        nav.start_travel_to_destination(town)
                        cruising = True
                        is_in_kingdom_menu = False
                        print_state()
                print(f"heading to {t}..")
                if not has_arrived_to_destination:
                    cruising = True
                    is_in_kingdom_menu = False
                    print_state()
                while cruising:
                    print(".", end='|')
                    time.sleep(1) # check every 1 second
                    # interruption handling
                    if nav.check_forced_make_peace_with_khuzait():
                        print("forced to make a decision about Khuzait!")
                        cruising = False
                        is_in_kingdom_menu = True
                        print_state()
                        break;
                    if nav.check_forced_make_peace_with_aserai():
                        print("forced to make a decision about Aserai!")
                        cruising = False
                        is_in_kingdom_menu = True
                        print_state()
                        break;
                    if nav.check_forced_ownership_of_onica():
                        print("forced to make a decision about Onica!")
                        cruising = False
                        is_in_kingdom_menu = True
                        print_state()
                        break;
                    if utils.is_world_map_paused():
                        print("game paused while cruising! (arrived to destination? Vlandia declared a war?")
                        cruising = False
                        is_in_kingdom_menu = False
                        print_state()
                        break;
                # that this point, it should be either
                # game in kingdom menu
                # or game paused (in which case either player arrived to destination or Vlandia declared a war
                if nav.check_still_in_kingdom_menu():
                    is_in_kingdom_menu = True
                    has_arrived_to_destination = False
                else:
                    is_in_kingdom_menu = False                                
                    if utils.is_world_map_paused():
                        is_in_kingdom_menu = False
                        has_arrived_to_destination = True if nav.check_arrived_to_destination() else False
                        if has_arrived_to_destination:
                            pass
                        else:
                            print("world map paused without arriving to destination")
                            print("must be Vlandia declaring war")
                            print("opening the kingdom menu to resolve this")
                            nav.open_kingdom_menu()
                            is_in_kingdom_menu = True
                            on_war_with_vlandia = True
                            shops_in_vlandia_closed = True
                    else:
                        print("must be cruising")
                        cruising = True
                print_state()
                # kingdom menu navigation
                while is_in_kingdom_menu:
                    print("..", end='|')
                    time.sleep(1) # buffer
                    if nav.check_forced_make_peace_with_khuzait():
                        nav.resolve_forced_make_peace_with_khuzait()
                        print("forced Make Peace With Khuzait resolved")
                        is_in_kingdom_menu = True
                        has_arrived_to_destination = False
                        print_state()
                        continue
                    if nav.check_forced_make_peace_with_aserai():
                        nav.resolve_forced_make_peace_with_aserai()
                        print("forced Make Peace With Aserai resolved")
                        is_in_kingdom_menu = True
                        has_arrived_to_destination = False
                        print_state()
                        continue
                    if nav.check_forced_ownership_of_onica():
                        nav.resolve_forced_ownership_of_onica()
                        print("forced Ownership of Onica Castle resolved")
                        is_in_kingdom_menu = True
                        has_arrived_to_destination = False
                        print_state()
                        continue
                    if nav.check_voluntary_make_peace_with_khuzait():
                        nav.resolve_voluntary_make_peace_with_khuzait()
                        print("voluntary Make Peace With Khuzait resolved")
                        is_in_kingdom_menu = True
                        has_arrived_to_destination = False
                        print_state()
                        continue
                    if nav.check_voluntary_make_peace_with_aserai():
                        nav.resolve_voluntary_make_peace_with_aserai()
                        print("voluntary Make Peace With Aserai resolved")
                        is_in_kingdom_menu = True
                        has_arrived_to_destination = False
                        print_state()
                        continue
                    if nav.check_voluntary_ownership_of_onica():
                        nav.resolve_voluntary_ownership_of_onica()
                        print("voluntary Ownership of Onica Castle resolved")
                        is_in_kingdom_menu = True
                        has_arrived_to_destination = False
                        print_state()
                        continue
                    if nav.check_in_war_with_vlandia():
                        print("in war with vlandia")
                        nav.make_peace_with_vlandia()
                        on_war_with_vlandia = False
                        shops_in_vlandia_closed = True
                        print("made peace with Vlandia")
                        is_in_kingdom_menu = True
                        has_arrived_to_destination = False
                        on_war_with_vlandia = False
                        print_state()
                    if nav.check_still_in_kingdom_menu():
                        print("detected still remaining in the kingdom menu")
                        nav.close_kingdom_menu()
                        print("closing Kingdom menu")
                        is_in_kingdom_menu = False
                        has_arrived_to_destination = False
                        print_state()
                # end of kingdom menu

                # check if game is still paused (especially after the kingdom menu control flow)
                if utils.is_world_map_paused():
                    if nav.check_arrived_to_destination():
                        print("arrived to destination")
                        has_arrived_to_destination = True
                    else:
                        print("game is paused but the player has not arrived to the destination")
                        print("need to navigate again")
                        has_arrived_to_destination = False
                else:
                    print("game not paused, continue")
                    has_arrived_to_destination = False
                print_state()
            # end of not has_arrived_to_destination
            # town UI navigation
            print("entering town")
            ocr.enter_trader(town, shops_in_vlandia_closed)
            time.sleep(1)
            ocr.sort_trader_inventory()
            time.sleep(1)
            if ocr.trader_has("Legendary"):
                pa.hotkey('alt', 'tab')
                print(f"current iteration count: {counter}")
                input("omg")
                input("omg omg")
                input("are you sure you're skipping this!?")
                pa.hotkey('alt', 'tab')
            ocr.leave_trader()
            time.sleep(1)
            ocr.leave_town(town, shops_in_vlandia_closed)
            time.sleep(1)
        # end of towns loop
        time.sleep(0.5)
        load_game()
        print(f"✅ n-th iteration finished: {counter}")
        counter += 1
        
pa.hotkey('alt', 'tab')
print(f"✅ script ended with {counter} simulated results.")
