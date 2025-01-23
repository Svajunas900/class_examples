## @classmethod
Class method takes cls as first argument of the method
This method is bound to a class not an instance of a class this means it
can change class attributes and it will be present in all instances of a class

## @staticmethod
Is also bound to a class not an instance, but it cannot modify or access class attributes
It is only used as utility function

## GIL (Global Interpreter lock)
It is a lock that protects access to Python objects in CPython on the execution of Python bytecode. 
This means even in multithreading app python will use only one thread at the time. 
On CPU-bound tasks like multiplication, image processing, it becomes bottleneck because 
it limits the threads to run in parallel.
On I/O-bound tasks it still can achieve concurrency because while I/O task waits for input
other tasks can be executed

## Multithreading
Multithreading is running multiple threads (smaller processes) within a single process.
They share same memory space. They execute independently within the same process.

## Multiprocessing
Multiprocessing is running multiple processes in the same time, each with their own interpreter and memory space.
This is a good usaged for CPU-bound tasks because it uses different interpreters to complete the tasks
