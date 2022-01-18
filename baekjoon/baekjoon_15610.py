# Abbey Courtyard
"""
Bath’s annual Christmas market runs from the 23rd of November 2017 until the 10th of December 2017.
During this time, the market will occupy the entire square courtyard of Bath Abbey.
To brighten things up at night, a single long strand of cheerful festive lights
will be run along all four equally long edges of the courtyard.
You will be in charge of buying the electrical wiring to which the lights will be affixed.
How much will you need to use to outline the whole Christmas market with festive lights?
"""
import sys
n = int(sys.stdin.readline().rstrip())

print((n**0.5)*4)