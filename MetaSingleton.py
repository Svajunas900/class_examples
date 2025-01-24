class MetaSingleton(type):
  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
    return cls._instances[cls]


class Singleton(metaclass=MetaSingleton):
  pass


class Op():
  pass


single = Singleton()
single1 = Singleton()
single2 = Op()


print(single is single1)
print(single1 is single2)
