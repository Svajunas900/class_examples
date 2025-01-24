def singleton(cls):
  instances = {}
  def wrapper(*args, **kwargs):
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]
  return wrapper


@singleton
class Singleton:
  pass


class Singleton2:
  pass


single = Singleton()  

single2 = Singleton()
single3 = Singleton2()

print(single is single2)
print(single == single2)
print(single2 is single3)