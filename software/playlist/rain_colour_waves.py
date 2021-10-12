import random
import colorsys


# Drops are more dense and on average brighter near the wave centre
density_away_from_wave = 1 / 15  # Matches baseline rainfall
#density_near_wave = 0.35
#density_at_wave = 0.45
density_near_wave = 4 / 15
density_at_wave = 4 / 15

# Each of these is a range corresponding to arguments to random.randint
intensity_away_from_wave = (25, 75)  # Matches baseline rainfall
#intensity_near_wave = (100, 200)
#intensity_at_wave = (125, 255)
intensity_near_wave = (50, 150)
intensity_at_wave = (50, 150)

wave_speed = 0.1
wave_interval = 8000


class RainColourWaves:
    name = "Rain Colour Waves"
    transition_len = 5000
    pattern_len = 33000

    wave_active = False
    wave_pos = -5.0
    wave_hue = 0.0
    last_wave = 0

    def generate(self, led_state, transition, tick):
        # When we aren't in transition, generate a wave every 3s
        if transition == 1.0 and not self.wave_active and \
                (tick - self.last_wave) > wave_interval:
            self.wave_active = True
            self.last_wave = tick
            self.wave_pos = -5.0
            self.wave_hue = random.random()
            print("Starting new wave!")

        # Move the wave along
        if self.wave_active:
            self.wave_pos += wave_speed

        # Once the wave is past the end of the strips, deactivate it
        if self.wave_active and self.wave_pos > 19.0:
            self.wave_active = False
            print("Deactivated wave")

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
#                drop_saturation = (density - density_away_from_wave) / \
#                                  (density_at_wave - density_away_from_wave) \
#                                  * 0.25
                if abs(strip_num - self.wave_pos) < 5.0:
                    drop_saturation = 1 - abs(strip_num - self.wave_pos) / 5.0
                    drop_saturation = drop_saturation ** 0.5
                else:
                    drop_saturation = 0.0

                drop_hsv = (self.wave_hue, drop_saturation, drop_intensity)
                rgb = colorsys.hsv_to_rgb(*drop_hsv)
                drop_colour = tuple(255 * x for x in rgb)
                strip[0] = drop_colour
