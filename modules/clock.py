import time

class Clock():
    """
    Use built-in time module to simply measure computation time.
    example:

    clock = Clock()
    tic()
    -- process you want to measure --
    toc()
    """

    def __init__(self):
        self._start_time = 0
        self._stop_time = 0
        self._elasped_time = 0

    def tic(self):
        """
        Create a start point in time
        """
        self._start_time = time.perf_counter()

    def toc(self):
        """
        Create a stop point in time
        """
        self._stop_time = time.perf_counter()
        self._elasped_time = self._stop_time - self._start_time
        print("Elasped time: %s"  % self._elasped_time)
