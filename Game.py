from sense_hat import SenseHat
import random
sense = SenseHat()

num1= random.randint(1, 10)
num2= random.randint(1, 10)
ans=num1+num2
sense.show_message(f"{num1}+{num2}", text_colour=(255, 255, 255))

guess=0
for event in sense.stick.get_events():
    if event.action == "pressed" and event.direction == "middle":
        guess+=1
    if event.action == "pressed" and event.direction == "up":
        if guess==ans:
            sense.show_message("Correct!", text_colour=(0, 255, 0))
        else:
            sense.show_message("Incorrect!", text_colour=(255, 0, 0))



