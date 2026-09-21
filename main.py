from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
sense.clear(255, 0, 0)
sense.clear(0,0,255)
while flag==True:
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
 
    print(f"Temperature {temperature:.2f} C")
    print(f"Pressure {pressure:.2f} hPa")
    if temperature>30:
        weather = "Hot"
        colour = (255,0,0)
    else:
        weather = "Cold"
        colour = [0,0,255]
    sense.show_message(f"{weather}, {temperature:.2f}C", text_colour = colour)
