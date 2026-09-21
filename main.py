from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
sense.set_pixel(0,0, 255, 255, 255)
flag=input("Do you want to continue? (Y/N): ")
while flag=="Y":
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()

    print(f"Temperature {temperature:.2f} C")
    print(f"Pressure {pressure:.2f} hPa")
    if temperature>30:
        weather = "Hot"
    else:
        weather = "Cold"
    sense.show_message(f"{weather}")
    flag=input("Do you want to continue? (Y/N): ")