from sense_hat import SenseHat
import random
sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":
            dice = random.randint(1, 6)
            sense.show_message(str(dice), text_colour=(255, 255, 255))


