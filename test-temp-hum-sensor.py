import time
import board
import busio
import adafruit_ahtx0

# Create I2C object using specific SDA and SCL pins
i2c = busio.I2C(board.GP3, board.GP2)  # Modify the pins as per your connection
sensor = adafruit_ahtx0.AHTx0(i2c)

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)
