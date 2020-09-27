trend_search_automate_part-2


################################################################
#importing libraries
import pyautogui as p
import time
from datetime import datetime

################################################################
#declarations

def copia_parecer():
    p.moveTo(323,-92,duration=0.3)
    p.click()
    p.dragTo(575,-92, button='left',duration=1)
    p.keyDown('ctrl')
    p.hotkey('c')
    p.keyUp('ctrl')
    print(datetime.now(), ' - parecer copiado')

    
################################################################
#execution

