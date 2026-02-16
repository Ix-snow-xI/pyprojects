import random, threading,queue
from threading import current_thread
from time import sleep

q=queue.Queue(maxsize=10)
rlock=threading.RLock()
timeout_thr=[]
sem=threading.BoundedSemaphore(value=10)
class Application(threading.Thread):
    def __init__(self,func,name):
        super().__init__(target=func,name=f"thr-{name}")
        self.id=random.randint(111111,999999)
        self.stop=0
        self.waiting=0
        self.timeout=1
        self.solution_time=random.randint(5,15)
        sleep(1)
#clock() - to set the timeout flag, until i come up with something better
    def clock(self):
        for _ in range(self.timeout):
            self.waiting+=1
            sleep(1)
            if self.waiting==self.timeout:
                timeout_thr.append(self.id)
                self.stop=1
                break

# noinspection PyTypeChecker
def testing():
    current: Application = (current_thread())
    current.clock()
    if not current.stop:
        with sem:
            sleep(current.solution_time)
            print(f"job done for {current.name}")
    else:
        print(f"stopping job for {current.id},because of timeout")

for i in range(1000):
    app = Application(testing,f"{i}")
    if not q.full():
        try:
            q.put(app,timeout=20)
            app.clock()
            print(f"{app.name} is waiting")
            if not sem._value==0:
                q.get(timeout=10)
                print(f"{app.id} started , time{app.solution_time}")
                app.start()
        except queue.Full:
            timeout_thr.append(app.id)
            app.stop=1
        except queue.Empty:
            break
