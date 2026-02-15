import random, threading,time
from threading import current_thread
from time import sleep

sem=threading.BoundedSemaphore(value=10)
class Application(threading.Thread):
    def __init__(self,func):
        super().__init__(target=func)
        self.id=random.randint(789545454,8954549498)
        self.waiting=0
        self.timeout=20
        self.solution_time=random.randint(15,25)
        sleep(2)


# noinspection PyTypeChecker
def testing():
    current: Application = (current_thread())
    start_time=time.time()
    with sem:
        print(f"starting job for {current.name}")
        sleep(current.solution_time)
        print(f"job done for {current.name}")

for i in range(100):
    test=Application(testing)
    test.start()
