from datetime import datetime
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print('%s run time: %s' % (func.__name__, (end_time - start_time)))
        return result
    return wrapper
    