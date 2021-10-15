from playlist.colour_rain import ColourRain
from playlist.rainfall import Rainfall
from playlist.rain_intensity_waves import RainIntensityWaves
from playlist.rain_colour_waves import RainColourWaves, RainbowWaves
from playlist.rain_strobe import RainStrobe


# Playlist of pattern classes.  A fresh pattern object is created from each
# class when the pattern starts to help make a clean state.
patterns = [
    Rainfall,
    RainStrobe,
    RainIntensityWaves,
    Rainfall,
    ColourRain,
    Rainfall,
    RainColourWaves,
    Rainfall,
    RainbowWaves,
]

# Length of transition, in milliseconds, for patterns which don't specify
default_transition_len = 10 * 1000

# Length of pattern body (not including transitions), in milliseconds, for
# patterns which don't specify
default_pattern_len = 10 * 1000


class Playlist:
    def __init__(self):
        self.pattern_ptr = None
        self.pattern_start_tick = None
        self.current_pattern = None

    def _pattern_len(self):
        """ How long is the body of the current pattern (excluding transitions)
        in milliseconds """
        if hasattr(patterns[self.pattern_ptr], 'pattern_len'):
            return patterns[self.pattern_ptr].pattern_len
        else:
            return default_pattern_len

    def _transition_len(self):
        if hasattr(patterns[self.pattern_ptr], 'transition_len'):
            return patterns[self.pattern_ptr].transition_len
        else:
            return default_transition_len

    def _total_len(self):
        """ How long is the current pattern, including transitions, in
        milliseconds """
        return self._pattern_len() + 2 * self._transition_len()

    def _gen_transition(self, tick_in_pattern):
        """ Work out the transition proportion. `tick_in_pattern` is the time
        since the pattern began and `length` is the length of the pattern, both
        in milliseconds. """

        # Handle transitions into and out of the pattern.  We do this by
        # working out a `transition` number between 0.0 and 1.0.  transition
        # starts at 0.0 and smoothly moves to 1.0 during the fade-in.  It stays
        # at 1.0 for the main duration of the pattern.  Then it fades back to
        # 0.0 during the outward transition.

        transition_len = self._transition_len()
        total_len = self._total_len()

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

        # Handle first run
        if self.current_pattern is None:
            self.pattern_ptr = 0
            self.pattern_start_tick = tick
            self.current_pattern = patterns[0]()
            print("Starting with pattern number {} named {}".format(
                self.pattern_ptr, self.current_pattern.name))

        # Start a new pattern if needed
        if tick - self.pattern_start_tick > self._total_len():
            self.pattern_start_tick = tick
            self.pattern_ptr = (self.pattern_ptr + 1) % len(patterns)
            self.current_pattern = patterns[self.pattern_ptr]()
            print("Started new pattern number {} named {}".format(
                self.pattern_ptr, self.current_pattern.name))

        tick_in_pattern = tick - self.pattern_start_tick
        transition = self._gen_transition(tick_in_pattern)
        self.current_pattern.generate(led_state, transition, tick_in_pattern)
