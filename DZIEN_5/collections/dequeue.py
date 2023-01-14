from collections import deque

queue = deque(['imie','nazwisko','wiek','waga'])
print(queue)

queue.append('miasto')
print(queue)

queue.appendleft('id')
print(queue)

#zachownie stosu
queue.pop()
print(queue)

#zachowanie kolejki
queue.popleft()
print(queue)
