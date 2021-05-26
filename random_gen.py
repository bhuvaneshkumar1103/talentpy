import random
from typing import get_type_hints
# creating a generator to generate a random number every time it is called.
def values_random():
    yield random.randint(1,99999)
print(next(values_random()))
