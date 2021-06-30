import time
from datetime import datetime
from random import random
from timeit import timeit
from typing import List

import pandas as pd


def get_dict_data() -> List:
    return {
        "time": time.time(),
        "x": random(),
        "y": random(),
        "z": random(),
    }


def get_array_data() -> List:
    return [
        time.time(),
        random(),
        random(),
        random(),
    ]


def get_series_data():
    return pd.Series(get_dict_data())


DATA_ARRAY = [get_dict_data() for _ in range(100)]


def convert_to_df():
    return pd.DataFrame(DATA_ARRAY)


if __name__ == "__main__":
    result = timeit(datetime.now().timestamp)
    print(f"datetime.timestamp: {result*1e3:.3f} ns per loop")

    result = timeit(time.time)
    print(f"time.time: {result*1e3:.3f} ns per loop")

    result = timeit(random)
    print(f"random: {result*1e3:.3f} ns per loop")

    result = timeit(get_dict_data)
    print(f"get_dict_data: {result*1e3:.3f} ns per loop")

    result = timeit(get_array_data)
    print(f"get_array_data: {result*1e3:.3f} ns per loop")

    result = timeit(get_series_data, number=int(1e4))
    print(f"get_series_data: {result*1e3:.3f} ns per loop")

    result = timeit(convert_to_df, number=int(1e4))
    print(f"convert_to_df: {result*1e3:.3f} ns per loop")
