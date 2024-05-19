import time
import datetime
import os
from typing import *

from . import utils
from .types import *

seed = [int(((time.time() * 1000) * (datetime.datetime.now().microsecond + 1) / (os.getpid() + 1) % 1000000) * 1000 + os.getpid()) % 10000000000]

def rng(lower : int = None, upper : int = None, x0 : Array = seed, a : int = 214013, c : int = 2531011, m : int = 2 ** 31) -> int:
    
    x = (a * x0[0] + c) % m
    x0[0] = x

    if lower == None and upper == None:
        return x
    else:
        return int((x / (m - 1)) * abs(upper - lower + 1) + utils.min(lower,upper))