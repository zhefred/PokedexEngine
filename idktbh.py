import random
import time
from pynput.keyboard import Key, Controller

print("booting up...")

inputs = [  'w',    'a',    's',    'd',        'x',    'z']
DS_KEYS = ["UP",    "LEFT", "DOWN", "RIGHT",    "A",    "B",      "X",       "Y",      "START",   "SELECT"]
action = Controller()

inputs_done = open("backlogInput.txt", "a")


print("Starting project in 5 seconds...")
time.sleep(5)

while(True):
    rng = random.randint(0,0)

    if rng <= 25 :
        next_key = 4
    else:
        next_key = random.randint(0,len(inputs)-1)
    
    key = inputs[next_key]
    action.press(key)
    time.sleep(0.2)
    action.release(key)

    print(DS_KEYS[next_key])
    inputs_done.write(DS_KEYS[next_key] + ", ")
    time.sleep(0.5)

    