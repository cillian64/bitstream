Each pattern implements a class with two members:
 - A `name` field with a human-readable pattern name
 - A `generate` method which draws frames.

The generate method has the following signature:

```
def generate(self, led_state, transition, tick):
```

where:
 - `led_state` is a list of lists of tuples representing the RGB colour of
   each LED pixel (scaled from 0-255),
 - `transition` is a number between 0.0 and 1.0 controlling fade-in and
   fade-out,
 - `tick` is the time since this pattern began (in milliseconds).

Each pattern should appear the same as default rainfall when transition == 0.0
and display the specific pattern when transition == 1.0, with smooth fading
between these two endpoints.  transition will fade from 0.0 to 1.0 during the
transition-in period, stay at 1.0 for the main duration of the pattern, and
fade back to 0.0 during the transition-out period.
