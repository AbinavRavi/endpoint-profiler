import cProfile
import pstats
import functools


def profiler(func):
    """profiler decorator function

    Args:
        func (function): any function that needs to be wrapped around

    Returns:
        wrapper of the function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        profiler.print_stats()
        stats = pstats.Stats(profiler)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        return result
    return wrapper
