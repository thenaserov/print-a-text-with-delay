# github.com/naserrezayi98
# Please don't forget to import time module

import os
import sys
import time

# Here you must introduce a string
text = "Here is how to print a text with delay!"
# Here you must use a for loop including char
for char in text:
    # Here you are telling the system to print chars
    sys.stdout.write(char)
    # Here you are telling the system to print nothing with the time mentioned below
    sys.stdout.flush()
    # The delay time between each "char"
    time.sleep(0.1)