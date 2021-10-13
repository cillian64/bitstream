import random


# Drops are more dense and on average brighter near the wave centre
density_away_from_wave = 1 / 15  # Matches baseline rainfall
density_near_wave = 0.35
density_at_wave = 0.45

# Each of these is a range corresponding to arguments to random.randint
intensity_away_from_wave = (25, 75)  # Matches baseline rainfall
intensity_near_wave = (100, 200)
intensity_at_wave = (125, 255)


class RainIntensityWaves:
    name = "Rain Intensity Waves"
    transition_len = 0
    pattern_len = 5000

    def __init__(self):
        if random.randint(0, 1) == 0:
            # Wave from left to right
            self.wave_pos = -5.0
            self.wave_vel = 0.2
        else:
            # Wave from right to left
            self.wave_pos = 20.0
            self.wave_vel = -0.2


    def generate(self, led_state, transition, tick):
        # Move the wave along
        self.wave_pos += self.wave_vel

        # Move all the LED positions down by one, shifting in black
        for strip in led_state:
            strip[:] = [(0, 0, 0)] + strip[:-1]

        # Generate a "drip" on some random strips.  Drips are more dense and
        # brighter around the wave position
        for strip_num, strip in enumerate(led_state):
            # Decide on probability of making a new drop on this strip
            if abs(strip_num - self.wave_pos) < 2.0:
                density = density_at_wave
                intensity = intensity_at_wave
            elif abs(strip_num - self.wave_pos) < 4.0:
                density = density_near_wave
                intensity = intensity_near_wave
            else:
                density = density_away_from_wave
                intensity = intensity_away_from_wave

            if random.random() < density:
                # Generate a drop
                drop_intensity = random.randint(*intensity)
                drop_colour = (drop_intensity, drop_intensity, drop_intensity)
                strip[0] = drop_colour
