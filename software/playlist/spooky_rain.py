import random


class SpookyRain:
    name = "Spooky Rain"
    transition_len = 0
    pattern_len = 5000

    def generate(self, led_state, transition, tick):
        """ Normal rainfall, but green and spooky """

        for strip in led_state:
            strip[:] = [(0, 0, 0)] + strip[:-1]

        density = 1
        for _ in range(density):
            drop_intensity = random.randint(25, 75)
            drop_colour = (0, drop_intensity, 0)
            random.choice(led_state)[0] = drop_colour

