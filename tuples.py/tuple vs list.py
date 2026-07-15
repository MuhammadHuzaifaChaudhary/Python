import sys
import time

# Memory comparison
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_data)} bytes")   # ~96 bytes
print(f"Tuple size: {sys.getsizeof(tuple_data)} bytes") # ~80 bytes

# Speed comparison (creation)
start = time.time()
for _ in range(1000000):
    lst = [1, 2, 3, 4, 5]
list_time = time.time() - start

start = time.time()
for _ in range(1000000):
    tpl = (1, 2, 3, 4, 5)
tuple_time = time.time() - start

print(f"List creation: {list_time:.4f} seconds")
print(f"Tuple creation: {tuple_time:.4f} seconds")
print(f"Tuples are {list_time/tuple_time:.2f}x faster!")

# Speed comparison (access)
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

start = time.time()
for _ in range(1000000):
    x = list_data[2]
list_time = time.time() - start

start = time.time()
for _ in range(1000000):
    x = tuple_data[2]
tuple_time = time.time() - start

print(f"List access: {list_time:.4f} seconds")
print(f"Tuple access: {tuple_time:.4f} seconds")
print(f"Tuples are {list_time/tuple_time:.2f}x faster!")