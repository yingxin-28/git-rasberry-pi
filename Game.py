from sense_hat import SenseHat
import time
import random

sense = SenseHat()

# Colours
BALL = (255, 255, 255)
PLAYER = (0, 255, 0)
COMPUTER = (255, 0, 0)

# Player and computer paddle positions
player_y = 3
computer_y = 3

# Ball position
ball_x = 3
ball_y = 3

# Ball movement
ball_dx = 1
ball_dy = 1

sense.clear()

while True:

    # Draw player paddle
    sense.set_pixel(0, player_y, PLAYER)
    sense.set_pixel(0, player_y + 1, PLAYER)

    # Draw computer paddle
    sense.set_pixel(7, computer_y, COMPUTER)
    sense.set_pixel(7, computer_y + 1, COMPUTER)

    # Draw ball
    sense.set_pixel(ball_x, ball_y, BALL)

    time.sleep(0.2)

    # Clear screen
    sense.clear()

    # Move ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off top/bottom
    if ball_y <= 0 or ball_y >= 7:
        ball_dy *= -1

    # Player joystick
    for event in sense.stick.get_events():

        if event.action == "pressed":

            if event.direction == "up":
                player_y -= 1

            elif event.direction == "down":
                player_y += 1

    # Keep player paddle inside screen
    player_y = max(0, min(6, player_y))

    # Simple computer movement
    if ball_y > computer_y:
        computer_y += 1
    elif ball_y < computer_y:
        computer_y -= 1

    computer_y = max(0, min(6, computer_y))

    # Player collision
    if ball_x == 1:
        if player_y <= ball_y <= player_y + 1:
            ball_dx = 1

    # Computer collision
    if ball_x == 6:
        if computer_y <= ball_y <= computer_y + 1:
            ball_dx = -1

    # Ball goes past player
    if ball_x < 0:
        sense.show_message("CPU")

        ball_x = 3
        ball_y = 3
        ball_dx = 1

    # Ball goes past computer
    if ball_x > 7:
        sense.show_message("YOU")

        ball_x = 3
        ball_y = 3
        ball_dx = -1