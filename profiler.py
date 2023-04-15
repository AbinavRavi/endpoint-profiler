import cProfile
import pstats
import logging


def profiler(func):
    def wrapper():
        profiler = cProfile.Profile()
        profiler.enable()
        result = func()
        profiler.disable()
        profiler.print_stats()
        stats = pstats.Stats(profiler)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        return result
    return wrapper
