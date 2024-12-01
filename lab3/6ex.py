import time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()  
        print(f"time: {end_time - self.start_time:.2f}")
@contextmanager
def cm_timer_2():
    start_time = time.time()  
    try:
        yield  
    finally:
        end_time = time.time()  
        print(f"time: {end_time - start_time:.2f}") 
if __name__ == "__main__":
    from time import sleep
    
    print("Using cm_timer_1:")
    with cm_timer_1():
        sleep(2)

    print("Using cm_timer_2:")
    with cm_timer_2():
        sleep(2)