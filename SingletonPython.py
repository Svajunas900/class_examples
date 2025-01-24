class Singleton:
  _instance = None

  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance


class Op:
  pass

single = Singleton()
single1 = Singleton()
op = Op()
op1 = Op()
print(single is single1)
print(op == op1)