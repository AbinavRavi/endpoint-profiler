import cProfile
import pstats

def profiler(func):
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        profiler.print_stats()
        # stats = pstats.Stats(profiler).sort_stats('tottime')
        # stats.dump_stats('/profile.csv')
        # stats.print_stats()
        return result
    return wrapper
