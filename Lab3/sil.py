from functools import reduce
silnia = lambda x: reduce(lambda x, y: x * y, range(1, x+1))
