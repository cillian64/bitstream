import time
from rpi_ws281x import ws, Color, Adafruit_NeoPixel


led_count = 30  # Per strip
fps = 60
freq = 800000

# LED strip configuration:
LED_1_COUNT = led_count * 8  # Number of LED pixels.
LED_1_PIN = 12           # GPIO pin connected to the pixels
LED_1_FREQ_HZ = freq     # LED signal frequency in hertz
LED_1_DMA = 10           # DMA channel to use for generating signal
LED_1_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_1_INVERT = False     # True to invert the signal
LED_1_CHANNEL = 0        # 0 or 1
LED_1_STRIP = ws.WS2811_STRIP_GBR

LED_2_COUNT = led_count * 8  # Number of LED pixels.
LED_2_PIN = 13           # GPIO pin connected to the pixels
LED_2_FREQ_HZ = freq     # LED signal frequency in hertz
LED_2_DMA = 10           # DMA channel to use for generating signal
LED_2_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_2_INVERT = False     # True to invert the signal
LED_2_CHANNEL = 1        # 0 or 1
LED_2_STRIP = ws.WS2811_STRIP_GBR


strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ,
                           LED_1_DMA, LED_1_INVERT,
                           LED_1_BRIGHTNESS, LED_1_CHANNEL,
                           LED_1_STRIP)

strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ,
                           LED_2_DMA, LED_2_INVERT,
                           LED_2_BRIGHTNESS, LED_2_CHANNEL,
                           LED_2_STRIP)

strip1.begin()
strip2.begin()

walk_pos = 0


def draw():
    global walk_pos

    for i in range(LED_1_COUNT):
        if (i + walk_pos) % 5 == 0:
            strip1.setPixelColor(i, Color(64, 64, 64))
            strip2.setPixelColor(i, Color(0, 0, 255))
        else:
            strip1.setPixelColor(i, Color(0, 0, 0))
            strip2.setPixelColor(i, Color(0, 0, 0))

    walk_pos += 1

    strip1.show()
    strip2.show()

while True:
    # Render
    draw()

    time.sleep(1.0 / fps)
