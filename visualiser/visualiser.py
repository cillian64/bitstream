import pygame
from playlist import Playlist


# Colours:
window_bg_colour = (20, 20, 20)  # Dark grey
bar_bg_colour = (50, 50, 0)  # Dark yellowish thing
strip_bg_colour = (0, 0, 0)  # Black

# Display settings
window_size = (800, 600)
fps = 60

# Dimensions
strip_pitch = window_size[0] / 9  # Distance between strips on a pole
strip_height = window_size[1] * 0.6
strip_width = window_size[0] / 150
bar_height = 50  # Distance from top of window to top pole
led_count = int(60 * 0.5)  # LEDs per strip
led_pitch = strip_height / (led_count + 1)  # Distance between LEDs on a strip


class Visualiser:
    """ Uses pygame to render LEDs to a window. """

    def __init__(self, width, height):
        """ Internal setup, create pygame window. """
        self.size = (width, height)
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.playlist = Playlist()

    def _draw_led_strip(self, x, y, strip_colours):
        """ Draw an LED strip with top-left corner at (x, y). """
        strip_rect = pygame.Rect(x, y, strip_width, strip_height)
        pygame.draw.rect(self.screen, strip_bg_colour, strip_rect)

        assert len(strip_colours) == led_count
        for i, led_colour in enumerate(strip_colours):
            led_rect = pygame.Rect(x, y + (1 + i) * led_pitch, strip_width,
                                   strip_width)
            pygame.draw.rect(self.screen, led_colour, led_rect)

    def _draw(self, led_state):
        """ Render the window contents.  led_state is a list of lists of
        pygame colours representing LED states.  Strips are ordered left to
        right, i.e. alternating back and front. """

        assert len(led_state) == 8 + 7
        for strip in led_state:
            assert len(strip) == led_count

        self.screen.fill(window_bg_colour)

        # Render back bar
        rect = pygame.Rect(strip_pitch, 1.5 * bar_height,
                           7 * strip_pitch, strip_width)
        pygame.draw.rect(self.screen, bar_bg_colour, rect)

        # Render back strips
        for i in range(8):
            x = strip_pitch * (1 + i)
            y = 1.5 * bar_height
            self._draw_led_strip(x, y, led_state[i * 2])

        # Render front bar
        rect = pygame.Rect(strip_pitch * 1.5, bar_height,
                           6 * strip_pitch, strip_width)
        pygame.draw.rect(self.screen, bar_bg_colour, rect)

        # Render front strips
        for i in range(7):
            x = strip_pitch * (1.5 + i)
            y = bar_height
            self._draw_led_strip(x, y, led_state[1 + i * 2])

        pygame.display.flip()

    def main_loop(self, fps):
        """ Calls this._draw() 60 times a second.  returns if the window is
        closed or the application is otherwise requested to quit gracefully.
        """
        clock = pygame.time.Clock()

        # Initialise LEDs to all black
        led_state = []
        for i in range(8 + 7):
            led_state.append([(0, 0, 0)] * led_count)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Draw pattern frame from playlist
            self.playlist.generate(led_state, pygame.time.get_ticks())

            # Render
            self._draw(led_state)
            clock.tick(fps)


if __name__ == "__main__":
    visualiser = Visualiser(*window_size)
    visualiser.main_loop(fps)
