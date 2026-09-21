from sense_hat import SenseHat
import random
import time

sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":

            # Dice rolling animation
            for i in range(10):
                dice = random.randint(1, 6)
                sense.show_message(
                    str(dice),
                    text_colour=(255, 255, 255),
                    scroll_speed=0.05
                )
                time.sleep(0.1)

            # Final dice result
            dice = random.randint(1, 6)
            sense.show_message(
                str(dice),
                text_colour=(0, 255, 0)
            )


