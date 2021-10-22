class StripTest:
    name = "Strip Test"
    transition_len = 0
    pattern_len = 60000

    colour = 0  # 0 = red, 1 = green, 2 = blue, 3 = white
    strip = 0   # Ranges 0-14 inclusive
    last_update_tick = 0

    update_ticks = 500  # Update every 1s

    def generate(self, led_state, transition, tick):
        """ Test strips are connected and working correctly """

        # Only update the strips periodically.  First illuminate each strip in
        # order with red, then each strip with green, then each strip with
        # blue.
        if tick - self.last_update_tick > self.update_ticks:
            for i, strip in enumerate(led_state):
                # For each strip, work out what colour it shall be
                if i == self.strip:
                    if self.colour < 3:
                        colour = [0, 0, 0]
                        colour[self.colour] = 255
                        colour = tuple(colour)
                    else:
                        colour = (255, 255, 255)
                else:
                    colour = (0, 0, 0)

                # Update all pixels to that colour
                for j in range(len(strip)):
                    strip[j] = colour

            # Increment illuminated strip and colour
            self.last_update_tick = tick
            self.strip += 1
            if self.strip > 14:
                self.strip = 0
                self.colour += 1
                if self.colour > 3:
                    self.colour = 0
