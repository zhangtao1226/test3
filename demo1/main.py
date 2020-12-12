import threading
import time

def target(second):
    print(f'Threading {threading.current_thread().name} is runing_Fun')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended_Fun')

print(f'Threading {threading.current_thread().name} is running_Main')

for i in [1,5]:
    t = threading.Thread(target = target, args=[i])
    t.start()
    t.join()

print(f'Threading {threading.current_thread().name} is ended_Main')





