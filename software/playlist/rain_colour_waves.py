import random
import colorsys


# Drops are more dense and on average brighter near the wave centre
density_away_from_wave = 1 / 15  # Matches baseline rainfall
density_near_wave = 4 / 15
density_at_wave = 4 / 15

# Each of these is a range corresponding to arguments to random.randint
intensity_away_from_wave = (25, 75)  # Matches baseline rainfall
intensity_near_wave = (50, 150)
intensity_at_wave = (50, 150)

# What change in hue does a rainbow wave experience from one end to the other
rainbow_hue_range = 0.3


def clip3(val, min=0.0, max=1.0):
    """ Clip a value to within a min and max range """
    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val


class RainWaves:
    """ Generic class covering both rainbow and fixed colour waves """

    def __init__(self, rainbow):
        self.rainbow = rainbow
        if rainbow:
            # For rainbow waves the hue will vary as it moves.  The hue we
            # store here is what is seen at the left edge.  To ensure the
            # rainbow doesn't go out of range we cap the starting hue.
            self.wave_hue = random.random() * (1 - rainbow_hue_range)
        else:
            self.wave_hue = random.random()

        if random.randint(0, 1) == 0:
            # Wave from left to right
            self.wave_pos = -5.0
            self.wave_velocity = 0.1
        else:
            # Wave from right to left
            self.wave_pos = 20.0
            self.wave_velocity = -0.1

    def generate(self, led_state, transition, tick):
        # Move the wave along
        self.wave_pos += self.wave_velocity

        # Move all the LED positions down by one, shifting in black
        for strip in led_state:
            strip[:] = [(0, 0, 0)] + strip[:-1]

        # Generate a "drip" on some random strips.  Drips are more dense and
        # brighter around the wave position
        for strip_num, strip in enumerate(led_state):
            if abs(strip_num - self.wave_pos) < 1.0:
                density = density_at_wave
                intensity = intensity_at_wave
            elif abs(strip_num - self.wave_pos) < 3.0:
                density = density_near_wave
                intensity = intensity_near_wave
            else:
                density = density_away_from_wave
                intensity = intensity_away_from_wave

            if random.random() < density:
                # Generate a drop
                drop_intensity = random.randint(*intensity) / 255

                if abs(strip_num - self.wave_pos) < 5.0:
                    drop_saturation = 1 - abs(strip_num - self.wave_pos) / 5.0
                    drop_saturation = drop_saturation ** 0.5
                else:
                    drop_saturation = 0.0

                if self.rainbow:
                    hue = self.wave_hue + \
                        clip3(self.wave_pos / 15.0) * rainbow_hue_range
                else:
                    hue = self.wave_hue

                drop_hsv = (hue, drop_saturation, drop_intensity)
                rgb = colorsys.hsv_to_rgb(*drop_hsv)
                drop_colour = tuple(255 * x for x in rgb)
                strip[0] = drop_colour


class RainColourWaves(RainWaves):
    name = "Rain Colour Waves"
    transition_len = 0
    pattern_len = 8000

    def __init__(self):
        super().__init__(rainbow=False)


class RainbowWaves(RainWaves):
    name = "Rainbow Waves"
    transition_len = 0
    pattern_len = 8000

    def __init__(self):
        super().__init__(rainbow=True)
