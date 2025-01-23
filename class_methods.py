class Example:
  counter = 0

  @classmethod
  def class_example(cls):
    cls.counter += 1
    

  @staticmethod
  def static_example(x):
    return x * x

example = Example()
example1 = Example()

print(example.counter)
print(example1.counter)

example.class_example()

print(example.counter)
print(example1.counter)
print(example.static_example(10))