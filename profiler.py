import cProfile
import pstats
import logging


def profiler(func):
    def wrapper(*args, **kwargs):
        logger = logging.getLogger()
        logging.basicConfig(level = logging.DEBUG)
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        logger.info(profiler.print_stats())
        stats = pstats.Stats(profiler).sort_stats('tottime')
        stats.dump_stats('/profile.csv')
        stats.print_stats()
        return result
    return wrapper
