import random
import math


strip_height = 30


class Drop:
    strip = 0
    y = 0
    strobing = False
    intensity = 0
    phase = 0
    strobe_amp = 0
    f = 0.30

    def __init__(self, strip, y, strobing, intensity, strobe_amp=0):
        self.strip = strip
        self.y = y
        self.strobing = strobing
        self.intensity = intensity
        self.strobe_amp = strobe_amp

        self.phase = random.randint(0, 20)

    def render(self, led_state):
        if self.strobing:
            self.phase += 1
            sinusoid = math.sin(self.phase * self.f * 2 * math.pi) / 2.0 + 0.5
            amplitude = sinusoid * self.strobe_amp + (1 - self.strobe_amp)
            intensity = self.intensity * amplitude
            colour = (intensity, intensity, intensity)
        else:
            colour = (self.intensity, self.intensity, self.intensity)
        led_state[self.strip][self.y] = colour


class RainStrobe:
    name = "Rain Strobe"
    transition_len = 3000
    pattern_len = 3000

    def generate(self, led_state, transition, tick):
        # The way this pattern works relies on us holding the drops as separate
        # objects then being able to render them rather than just rendering
        # them all at time of creation and just moving the canvas down.
        if not hasattr(self, "drops"):
            self.drops = []
            for strip_idx, strip in enumerate(led_state):
                for y, pixel in enumerate(strip):
                    if pixel != (0, 0, 0):
                        assert pixel[0] == pixel[1]
                        assert pixel[0] == pixel[2]
                        self.drops.append(Drop(strip_idx, y, False, pixel[0]))
                    strip[y] = (0, 0, 0)

        # Move all the drops
        for drop in self.drops:
            drop.y += 1

        # Filter out any drops below the bottom of the strips
        self.drops = [drop for drop in self.drops if drop.y < strip_height]

        # Clear the LED state
        for strip in led_state:
            strip.clear()
            strip.extend([(0, 0, 0)] * strip_height)

        # Render drops to the LED state:
        for drop in self.drops:
            drop.render(led_state)

        # Generate a "drip" on some random strips
        density = 1
        for _ in range(density):
            drop_intensity = random.randint(25, 75)
            strip = random.randint(0, 14)
            strobing = transition > 0.1
            self.drops.append(Drop(strip, 0, strobing, drop_intensity,
                transition))
