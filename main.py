# Сделать декоратор cache, который бы кэшировал данные не больше чем на N секунд. N должно быть параметром декоратора
import functools
import time


def cache(seconds):
	cache_obj = {}  # dict to store cache
	cache_time = {}  # dict to store time

	def decorator(f):
		@functools.wraps(f)
		def wrapper(*args):
			if args not in cache_obj:
				print('calculate', args)
				cache_obj[args] = f(*args)
				cache_time[args] = time.time()
			elif args in cache_obj and time.time() - cache_time[args] <= seconds:  # if cached recently
				print('from cache', args)
			else:
				print('calculate', args)
				cache_obj[args] = f(*args)
				cache_time[args] = time.time()
			return cache_obj[args]
		return wrapper
	return decorator


@cache(0.2)
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)


result = [fibonacci(n) for n in range(10)]
print(result)
