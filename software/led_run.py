import time
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
from playlist import Playlist


led_count = 30
fps = 30

# LED strip configuration:
LED_1_COUNT = led_count  # Number of LED pixels.
LED_1_PIN = 12           # GPIO pin connected to the pixels
LED_1_FREQ_HZ = 700000   # LED signal frequency in hertz
LED_1_DMA = 10           # DMA channel to use for generating signal
LED_1_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_1_INVERT = False     # True to invert the signal
LED_1_CHANNEL = 0        # 0 or 1
LED_1_STRIP = ws.WS2811_STRIP_GBR

LED_2_COUNT = led_count  # Number of LED pixels.
LED_2_PIN = 13           # GPIO pin connected to the pixels
LED_2_FREQ_HZ = 700000   # LED signal frequency in hertz
LED_2_DMA = 11           # DMA channel to use for generating signal
LED_2_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
LED_2_INVERT = False     # True to invert the signal
LED_2_CHANNEL = 1        # 0 or 1
LED_2_STRIP = ws.WS2811_STRIP_GBR


class LedRunner:
    """ Renders to real WS2812b LEDs """

    def __init__(self):
        """ Internal setup, initialise LED strip drivers. """
        self.strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ,
                                        LED_1_DMA, LED_1_INVERT,
                                        LED_1_BRIGHTNESS, LED_1_CHANNEL,
                                        LED_1_STRIP)

        self.strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ,
                                        LED_2_DMA, LED_2_INVERT,
                                        LED_2_BRIGHTNESS, LED_2_CHANNEL,
                                        LED_2_STRIP)
        self.strip1.begin()
        self.strip2.begin()

        self.playlist = Playlist()

    def _draw(self, led_state):
        """ Render to LED strips.  led_state is a list of lists of pygame
        colours representing LED states.  Strips are ordered left to right,
        i.e. alternating back and front. """

        assert len(led_state) == 8 + 7
        for strip in led_state:
            assert len(strip) == led_count

        for i in range(led_count):
            colour = tuple(int(x) for x in led_state[0][i])
            self.strip1.setPixelColor(i, Color(*colour))
            colour = tuple(int(x) for x in led_state[1][i])
            self.strip2.setPixelColor(i, Color(*colour))

        self.strip1.show()
        self.strip2.show()

    def main_loop(self, fps):
        """ Calls this._draw() `fps' times per second until the application
        is terminated. """

        # Initialise LEDs to all black
        led_state = []
        for i in range(8 + 7):
            led_state.append([(0, 0, 0)] * led_count)

        while True:
            # Draw pattern frame from playlist
            millis = time.time() * 1000
            self.playlist.generate(led_state, millis)

            # Render
            self._draw(led_state)

            time.sleep(1.0 / fps)


if __name__ == "__main__":
    led_runner = LedRunner()
    led_runner.main_loop(fps)
