from sense_hat import SenseHat
sense = SenseHat()
flag=input("Do you want to continue? (Y/N): ")
while flag=="Y":
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()

    print(f"Temperature {temperature:.2f} C")
    print(f"Pressure {pressure:.2f} hPa")
    flag=input("Do you want to continue? (Y/N): ")