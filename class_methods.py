class Example:
  counter = 0

  def simple_func(cls):
    cls.counter += 1

  @classmethod
  def class_example(cls):
    cls.counter += 1
    

  @staticmethod
  def static_example(x):
    return x * x

