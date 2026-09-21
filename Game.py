import random
from sense_hat import SenseHat, ACTION_PRESSED
sense = SenseHat()
sense.clear()

def roll_dice(event):
    if event.action == ACTION_PRESSED:
        number = random.randint(1, 6)
        sense.show_message(f"Dice rolled: {number}", text_colour = (255,255,255))
        if number==6:
            sense.clear((0,255,0))  
            sense.show_message("Six! One more roll", text_colour = (0,255,0))
sense.stick.direction_middle = roll_dice


