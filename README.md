# Raspberry Pi Pico Pin Assignments

This README provides the pin assignments for connecting the Raspberry Pi Pico with the AHT20 sensor, BH1750 sensor, and Pi Inky display.

## Pinout

### Raspberry Pi Pico

- **PIN_PICO_SCL**: I2C SCL pin (board.GP3)
- **PIN_PICO_SDA**: I2C SDA pin (board.GP2)

### AHT20 Sensor

- **PIN_AHT20_SCL**: I2C SCL pin (board.GP3)
- **PIN_AHT20_SDA**: I2C SDA pin on (board.GP2)
- **PIN_AHT20_VCC**: Power supply pin (e.g., 3.3V)
- **PIN_AHT20_GND**: GND

### BH1750 Sensor

- **PIN_BH1750_SCL**: I2C SCL pin (board.GP3)
- **PIN_BH1750_SDA**: I2C SDA pin on (board.GP2)
- **PIN_BH1750_VCC**: Power supply pin (e.g., 3.3V)
- **PIN_BH1750_GND**: GND

### Pi Inky Display

- **PIN_INKY_CS**: Chip Select pin (board.GP17)
- **PIN_INKY_RST**: Reset pin (board.GP21)
- **PIN_INKY_DC**: Data/Command pin (board.GP20)
- **PIN_INKY_BUSY**: None
- **PIN_INKY_SCL**: SPI SCL pin (board.GP3)
- **PIN_INKY_SDA**: SPI SDA pin (board.GP2)
- **PIN_INKY_VCC**: Power supply pin (e.g., 3.3V)
- **PIN_INKY_GND**: Ground pin
- **PIN_SD_CS**: board.GP17
- **PIN_SD_SCK**: board.GP18
- **PIN_SD_MOSI**: board.GP19
- **PIN_SD_MISO**:  board.GP16

