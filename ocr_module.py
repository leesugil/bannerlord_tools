import pyautogui as pa
import pydirectinput as pi
import pytesseract as tess
from PIL import Image
import time

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# item names in the Trader screen
left = 118
top = 104
right = 298
bottom = 750

def trader_has(item="Legendary"):
    img = pa.screenshot()
    img = img.crop((left, top, right, bottom))
    text = tess.image_to_string(img)
    x = text.find(item)
    if x != -1:
        print(text)
        return True
    else:
        return False

def enter_trader(town, shops_in_vlandia_closed=False):
    print("entering Trader")
    x = town['x_trade']
    y = town['y_trade']
    if shops_in_vlandia_closed:
        print("shop is closed, adjusting UI")
        y += town['y_offset']
    pi.moveTo(x, y, duration=1)
    pi.click(x, y)

def sort_trader_inventory():
    print("sorting Trader inventory")
    pi.moveTo(350, 80, duration=1)
    pi.click(350, 80) # click value -> sorted ascen
    time.sleep(0.3)
    pi.click(350, 80) # click value again -> sorted descen

def leave_trader():
    print("leaving Trader")
    pi.press('esc')

def leave_town(town, shops_in_vlandia_closed=False):
    print("leaving town")
    x = town['x_leave']
    y = town['y_leave']
    if shops_in_vlandia_closed:
        print("shop is closed, adjusting UI")
        y += town['y_offset']
    pi.moveTo(x, y, duration=1)
    pi.click(x, y)
