import digitalio
import board
import busio
from adafruit_rfm9x import RFM9x
import time

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.D5)  # Assuming you are using GPIO 05 (Pin 29>
reset = digitalio.DigitalInOut(board.D6)  # Assuming you are using GPIO 06 (Pin>

rfm9x = RFM9x(spi, cs, reset, 433.0)

while True:
    # First send a message
    rfm9x.send(bytes("Hello, world!", "utf-8"))
    print("Sent message")
    time.sleep(2)  # Wait for the message to be sent

    # Then wait to receive a message
    print("Waiting for message...")
    packet = rfm9x.receive()
    if packet is not None:
        packet_text = str(packet, "utf-8")
        print("Received: {0}".format(packet_text))
        time.sleep(2)  # Wait before trying to receive again