from sense_hat import SenseHat
sense = SenseHat()
temperature = sense.get_temperature()
pressure = sense.get_pressure()

print("Temperature", temperature, "C")
print("Pressure", pressure, "hPa")