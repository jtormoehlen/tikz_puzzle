import queue as qu

number_queue = qu.Queue()

for i in range(10):
    number_queue.put(i)

while not number_queue.empty():
    print(number_queue.get())