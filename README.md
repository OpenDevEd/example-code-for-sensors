# Raspberry Pi Pico Pin Assignments

This README provides the pin assignments for connecting the Raspberry Pi Pico with the AHT20 sensor, BH1750 sensor, and Pi Inky display.


|                     | Pin  | Pin  |                         |
|---------------------|------|------|-------------------------|
| UART-TX ext         | GP0  | VBUS |
| UART-RX ext         | GP1  | VSYS |
|                     | GND  | GND  |
| SDA                 | GP2  | EN   |
| SCL                 | GP3  | 3V3  |
| DONE                | GP4  | VREF |
| I2S/PDM (BCLK/CLK)  | GP5  | GP28  | I2S/PDM (DOUT/DAT)
|                     | GND  | GND  |
| I2S (LRCL)          | GP6  | GP27 | ADC ext
| Lora-RST            | GP7  | GP26 | Inky Busy
| MISO1 (Lora)        | GP8  | RUN  | Inky Run
| Lora-CS             | GP9  | GP22 | SD-CS
|                     | GND  | GND  |
| SCLK1 (Lora)        | GP10 | GP21 | Inky Reset
| MOSI1 (Lora)        | GP11 | GP20 | Inky D/C
| Inky SWA            | GP12 | GP19 | MOSI0 (Inky, SD-Card)
| Inky SWB            | GP13 | GP18 | SCLK0 (Inky, SD-Card)
|                     | GND  | GND  |
| Inky SWC            | GP14 | GP17 | Inky CS
| Lora-EN             | GP15 | GP16 | MISO0 (Inky, SD-Card)

# Raspberry Pi Zero W Pin Assignments

This TABLE provides the pin assignments for connecting the Raspberry Pi Zero W with the Lora RfM9x.


|                     | Pin  | Pin  |     Radio                    |
|---------------------|------|------|-------------------------|
| Board 3v3           | Pin 1  | VIN | VIN
| Board GND           | Pin 6  | GND |GND
| Board SCK           | Pin 23 | SPI Clock  | SCK
| Board MOSI          | Pin 19 | SPI MOSI   | MOSI
| Board MISO          | Pin 21 | SPI MISO  | MISO
| Board D5            | Pin 29 | GPIO 21 | CS
| Board D6            | Pin 31  | GPIO 22  | RST
