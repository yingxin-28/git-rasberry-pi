from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
while True:
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
 
    print(f"Temperature {temperature:.2f} C")
    print(f"Pressure {pressure:.2f} hPa")
    print(f"Humidity {humidity:.2f} %rH")
    if temperature>30:
        weather = "Hot"
        colour = [255,0,0]
    else:
        weather = "Cold"
        colour = [0,0,255]
    sense.show_message(f"{weather}, {temperature:.2f}C", text_colour = colour)
    sense.show_message(f"Pressure: {pressure:.2f} hPa", text_colour = (255,255,255))
  
    if humidity>60:
        colour=[255,0,0]
    elif humidity<30:
        colour = [0,0,255]
    else:
        colour = [0,255,0]
    sense.show_message(f"Humidity: {humidity:.2f} %rH", text_colour = colour)
sense.clear()
