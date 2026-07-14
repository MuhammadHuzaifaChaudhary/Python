stack = []   
#  first in last out (FILO)

# Push (add to end)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# Pop (remove from end)
top = stack.pop()
print(top)    # 3
print(stack)  # [1, 2]

# Check if empty
if not stack:  # or len(stack) == 0
    print("Stack is empty")

# ===============================================================================================

# queue first in first out (FIFO)

# ===============================================================================================

from collections import deque

# Using deque (efficient)
queue = deque()

# Enqueue (add to end)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

# Dequeue (remove from front)
front = queue.popleft()
print(front)  # 1
print(queue)  # deque([2, 3])

# Using list (less efficient)
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
front = queue.pop(0)  # O(n) - slow!


