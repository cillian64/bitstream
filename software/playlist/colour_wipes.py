import random
import colorsys


wipe_velocity = 1
wipe_interval = 2500
wipe_len = 20  # In pixels
leds_per_strip = 30


class ColourWipes:
    name = "Colour Rain"
    strip_hues = []
    last_wipe = 0  # Time in ticks of the start of the last wipe.
    wipe_pos = leds_per_strip + wipe_len  # Start beyond the end of the strip
    wipe_strip = -1  # Index of which strip is wiping
    new_hue = 0  # New hue which we wipe to

    def __init__(self):
        for _ in range(15):
            self.strip_hues.append(random.random())

    def generate(self, led_state, transition, tick):
        if self.wipe_pos > leds_per_strip + 2 * wipe_len:
            # Time to start a new wipe.  First, copy the "new hue" to whatever
            # strip was wiped last time (assuming this isn't the first wipe)
            if self.wipe_strip != -1:
                self.strip_hues[self.wipe_strip] = self.new_hue

            # Now start a new wipe
            old_wipe_strip = self.wipe_strip
            while self.wipe_strip == old_wipe_strip:
                self.wipe_strip = random.randint(0, 14)
            self.wipe_pos = -2 * wipe_len
            self.last_wipe = tick

            # Choose what the new hue will be.  Ensure it is sufficiently
            # different to the old hue
            self.new_hue = random.random()
            while abs(self.new_hue - self.strip_hues[self.wipe_strip]) < 0.15:
                self.new_hue = random.random()

            if False:
                print("New wipe on strip {}, old hue {} new hue {}".format(
                    self.wipe_strip, self.strip_hues[self.wipe_strip],
                    self.new_hue))

        self.wipe_pos += wipe_velocity

        for i, strip in enumerate(led_state):
            if i == self.wipe_strip:
                # The strip being wiped
                old_hsv = (self.strip_hues[i], 1.0, 1.0)
                new_hsv = (self.new_hue, 1.0, 1.0)
                old_rgb = colorsys.hsv_to_rgb(*old_hsv)
                new_rgb = colorsys.hsv_to_rgb(*new_hsv)
                old_colour = tuple(255 * x for x in old_rgb)
                new_colour = tuple(255 * x for x in new_rgb)

                for j in range(len(strip)):
                    if j < self.wipe_pos:
                        # Above (behind) the wipe, use new colour
                        strip[j] = new_colour
                    elif j >= self.wipe_pos:
                        # Below (in front of) the wipe, use old colour
                        strip[j] = old_colour

                    # Pixels near the wipe become white
                    dist_from_wipe = abs(j - self.wipe_pos)
                    closeness_to_wipe = (wipe_len - dist_from_wipe) / wipe_len
                    closeness_to_wipe = max(closeness_to_wipe, 0)

                    strip[j] = tuple(x + closeness_to_wipe * 255
                                     for x in strip[j])
                    strip[j] = tuple(min(x, 255) for x in strip[j])

            else:
                # Boring normal strip
                hsv = (self.strip_hues[i], 1.0, 1.0)
                rgb = colorsys.hsv_to_rgb(*hsv)
                colour = tuple(255 * x for x in rgb)
                for j in range(len(strip)):
                    strip[j] = colour
