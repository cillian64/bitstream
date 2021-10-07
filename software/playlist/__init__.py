from playlist.colour_rain import ColourRain
from playlist.rainfall import Rainfall
from playlist.stars import Stars
from playlist.rain_intensity_waves import RainIntensityWaves
from playlist.rain_colour_waves import RainColourWaves
from playlist.colour_wipes import ColourWipes


# Playlist of pattern classes.  A fresh pattern object is created from each
# class when the pattern starts to help make a clean state.
patterns = [
#    RainIntensityWaves,
#    RainColourWaves,
#    ColourRain,
#    Stars,
    ColourWipes,
    Rainfall,
]

transition_len = 10 * 1000  # 10 seconds

# Time in pattern body, not including transitions
pattern_len = 10 * 1000  # 10 seconds

# total pattern length including transitions:
total_len = pattern_len + 2 * transition_len


class Playlist:
    def __init__(self):
        self.pattern_ptr = 0
        self.pattern_start_tick = 0
        self.current_pattern = patterns[0]()
        print("Starting with pattern number {} named {}".format(
            self.pattern_ptr, self.current_pattern.name))

    def _gen_transition(self, tick_in_pattern):
        """ Work out the transition proportion. `tick_in_pattern` is the time
        since the pattern began and `length` is the length of the pattern, both
        in milliseconds. """

        # Handle transitions into and out of the pattern.  We do this by
        # working out a `transition` number between 0.0 and 1.0.  transition
        # starts at 0.0 and smoothly moves to 1.0 during the fade-in.  It stays
        # at 1.0 for the main duration of the pattern.  Then it fades back to
        # 0.0 during the outward transition.

        if tick_in_pattern < transition_len:
            transition = tick_in_pattern / transition_len
        elif tick_in_pattern < total_len - transition_len:
            transition = 1.0
        else:
            transition = (total_len - tick_in_pattern) / transition_len

        return transition

    def generate(self, led_state, tick):
        """ Run patterns from the playlist with transitions, updating
        led_state.  `tick` is an absolute time in milliseconds.
        """

        # Start a new pattern if needed
        if tick - self.pattern_start_tick > total_len:
            self.pattern_start_tick = tick
            self.pattern_ptr = (self.pattern_ptr + 1) % len(patterns)
            self.current_pattern = patterns[self.pattern_ptr]()
            print("Started new pattern number {} named {}".format(
                self.pattern_ptr, self.current_pattern.name))

        tick_in_pattern = tick - self.pattern_start_tick
        transition = self._gen_transition(tick_in_pattern)
        self.current_pattern.generate(led_state, transition, tick_in_pattern)
