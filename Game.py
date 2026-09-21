import random
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

number = random.randint(1, 6)
sense.show_message(f"Dice rolled: {number}", text_colour = (255,255,255))