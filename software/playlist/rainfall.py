import random


class Rainfall:
    name = "Rainfall"
    # No need for transitions because this is the vanilla pattern
    transition_len = 0
    pattern_len = 5000

    def generate(self, led_state, transition, tick):
        """ Basic medium-density monochrome rainfall """
        # Because this pattern is a constant steady-state it doesn't depend on
        # transition.

        # First, move all the LED positions down by one, shifting in black
        for strip in led_state:
            strip[:] = [(0, 0, 0)] + strip[:-1]

        # Generate a "drip" on some random strips
        density = 1
        for _ in range(density):
            drop_intensity = random.randint(25, 75)
            drop_colour = (drop_intensity, drop_intensity, drop_intensity)
            random.choice(led_state)[0] = drop_colour
