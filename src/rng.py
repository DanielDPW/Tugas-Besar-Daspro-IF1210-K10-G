import time
import datetime
import os

from . import utils

seed = [int(((time.time() * 1000) * (datetime.datetime.now().microsecond + 1) / (os.getpid() + 1) % 1000000) * 1000 + os.getpid()) % 10000000000]

def rng(lower = None, upper = None, x0 = seed, a = 214013, c = 2531011, m = 2 ** 31) -> int:
    
    x = (a * x0[0] + c) % m
    x0[0] = x

    if lower == None and upper == None:
        return x
    else:
        return int((x / (m - 1)) * abs(upper - lower + 1) + utils.min(lower,upper))