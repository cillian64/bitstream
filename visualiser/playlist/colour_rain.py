import random
import colorsys


class ColourRain:
    name = "Colour Rain"

    def generate(self, led_state, transition, tick):
        """ Like standard rain but with occasional colour drops """
        # First, move all the LED positions down by one, shifting in black
        for strip in led_state:
            strip[:] = [(0, 0, 0)] + strip[:-1]

        # Generate a "drip" on some random strips
        density = 4
        for _ in range(density):
            # Every 10 drips should be coloured, otherwise monochrome
            if random.randint(0, 9) == 9:
                # When transition == 0.0 we need to match the normal drops
                # below (i.e. saturation = 0.0 and value = 0.2-0.6) When
                # transition == 1.0 we insert fully saturated colours

                hue = random.random()
                sat = transition
                val = 0.2 * (1 - transition) + \
                    random.random() * (0.4 * (1 - transition)) + \
                    transition

                rgb = colorsys.hsv_to_rgb(hue, sat, val)
                drop_colour = tuple(255 * x for x in rgb)
            else:
                drop_intensity = random.randint(50, 150)
                drop_colour = (drop_intensity, drop_intensity, drop_intensity)

            random.choice(led_state)[0] = drop_colour
