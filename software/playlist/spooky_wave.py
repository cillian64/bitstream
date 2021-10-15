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


class SpookyWave:
    """ Generic class covering both rainbow and fixed colour waves """
    name = "Rain Spooky Waves"
    transition_len = 0
    pattern_len = 8000

    def __init__(self):
        if random.randint(0, 1) == 0:
            # Wave from left to right
            self.wave_pos = -5.0
            self.wave_velocity = 0.2
        else:
            # Wave from right to left
            self.wave_pos = 20.0
            self.wave_velocity = -0.2

        if random.randint(0, 1) == 0:
            # Orange wave
            self.wave_hue = (255, 100, 0)
        else:
            # Purple wave
            self.wave_hue = (120, 0, 204)

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

                if abs(strip_num - self.wave_pos) < 3.0:
                    hue = self.wave_hue
                else:
                    hue = (0, 255, 0)

                strip[0] = tuple(x * drop_intensity for x in hue)
