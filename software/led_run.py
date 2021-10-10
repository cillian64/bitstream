import time
from rpi_ws281x import ws, Color, Adafruit_NeoPixel
from playlist import Playlist


led_count = 30  # Per strip
target_fps = 30
freq = 700000
brightness = 128

# LED strip configuration:
LED_1_COUNT = led_count * 8     # Number of LED pixels.
LED_1_PIN = 12                  # GPIO pin connected to the pixels
LED_1_FREQ_HZ = freq            # LED signal frequency in hertz
LED_1_DMA = 10                  # DMA channel to use for generating signal
LED_1_BRIGHTNESS = brightness   # Set to 0 for darkest and 255 for brightest
LED_1_INVERT = False            # True to invert the signal
LED_1_CHANNEL = 0               # 0 or 1
LED_1_STRIP = ws.WS2812_STRIP

LED_2_COUNT = led_count * 8     # Number of LED pixels.
LED_2_PIN = 13                  # GPIO pin connected to the pixels
LED_2_FREQ_HZ = freq            # LED signal frequency in hertz
LED_2_DMA = 10                  # DMA channel to use for generating signal
LED_2_BRIGHTNESS = brightness   # Set to 0 for darkest and 255 for brightest
LED_2_INVERT = False            # True to invert the signal
LED_2_CHANNEL = 1               # 0 or 1
LED_2_STRIP = ws.WS2812_STRIP


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

        for strip_num in range(8):
            for pix_num in range(led_count):
                colour = tuple(int(x) for x in led_state[2 * strip_num][pix_num])
                self.strip1.setPixelColor(strip_num * led_count + pix_num, Color(*colour))

                if strip_num < 7:
                    colour = tuple(int(x) for x in led_state[2 * strip_num + 1][pix_num])
                    self.strip2.setPixelColor(strip_num * led_count + pix_num, Color(*colour))

        self.strip1.show()
        self.strip2.show()

    def blank_leds(self):
        for i in range(240):
            self.strip1.setPixelColor(i, Color(0, 0, 0))
            self.strip2.setPixelColor(i, Color(0, 0, 0))
        self.strip1.show()
        self.strip2.show()

    def main_loop(self, target_fps):
        """ Calls this._draw() `target_fps' times per second until the
        application is terminated. """

        # Initialise LEDs to all black
        led_state = []
        for i in range(8 + 7):
            led_state.append([(0, 0, 0)] * led_count)

        last_frame = time.time()  # Time in s of last frame
        while True:
            # Draw pattern frame from playlist
            millis = time.time() * 1000
            self.playlist.generate(led_state, millis)

            # Render
            self._draw(led_state)

            next_frame = last_frame + 1.0 / target_fps
            now = time.time()
            time_to_sleep = next_frame - now

            if time_to_sleep > 0.0:
                time.sleep(time_to_sleep)
            else:
                actual_fps = 1.0 / (now - last_frame)
                print("Warning: dropping below {} target_fps (actual {})"
                    .format(target_fps, actual_fps))

            last_frame = now


if __name__ == "__main__":
    print("Starting up")
    led_runner = LedRunner()
    try:
        led_runner.main_loop(target_fps)
    except KeyboardInterrupt:
        print("\nBlanking strips")
        led_runner.blank_leds()
        print("Done")
