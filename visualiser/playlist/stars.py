import random


class Stars:
    name = "Stars"

    last_transition = 0.0

    def generate(self, led_state, transition, tick):
        """ Sparkly stars """
        # First, move all the LED positions down by one, shifting in black
        for strip in led_state:
            strip[:] = [(0, 0, 0)] + strip[:-1]

        # Generate a "drip" on some random strips
        density = 4
        for _ in range(density):
            # Slowly fade out the falling rain part
            drop_intensity = random.randint(50, 150) * (1 - transition)
            drop_colour = (drop_intensity, drop_intensity, drop_intensity)
            random.choice(led_state)[0] = drop_colour

        # If we're not in the transition period, render some sparkly stars
        if transition == 1.0:
            # First, blank any previous stars
            for strip in led_state:
                for idx, _ in enumerate(strip):
                    strip[idx] = (0, 0, 0)

            # Now make new stars
            density = 2
            for _ in range(density):
                strip = random.choice(led_state)
                led = random.choice(range(len(strip)))
                strip[led] = (255, 255, 255)

        # Check that we blank all stars when leaving the transition period
        if self.last_transition == 1.0 and transition != 1.0:
            for strip in led_state:
                for idx, _ in enumerate(strip):
                    strip[idx] = (0, 0, 0)
        self.last_transition = transition
