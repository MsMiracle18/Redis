import redis

if __name__ == '__main__':
  client = redis.Redis(host='localhost', port=6379, password=None)
  client.set(name: "username", value: "Oleksandr")
  client.expire(name: "username", time: 600)
  client.set(name: "age", value: 22)
  client.expire(name: "username", time: 600)

username = client.get("username")
age = client.get("age")
print = "username"



import redis
from redis_lru import redisLRU

if __name__ == '__main__':
  client = redis.Redis(host='localhost', port=6379, password=None)

@cache
def fib(n):
  if n < 0:
    return 0
  elif n = 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
  start_time = timeit.default_timer()
  r = fib(35)
  print(f"fib = {r}: {timeit.default_timer() - start_time}")

  start_time = timeit.default_timer()
  r = fib_cache(35)
  print(f"fib = {r}: {timeit.default_timer() - start_time}")






