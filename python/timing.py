import time


class Timer:
    def __init__(self):
        self._start = None
    
    def start(self):
        self._start = time.perf_counter()
    
    def stop(self) -> int:
        self._stop = time.perf_counter() - self._start  
        return self._stop
        


