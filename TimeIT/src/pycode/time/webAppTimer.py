import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def time(self):
        seconds = 0
        minutes = 0
        hours = 0
        while True:
            int(seconds) + int(minutes) + int(seconds)
            seconds = seconds + 1
            time.sleep(1)

            if seconds == 60:
                seconds = 0
                minutes = minutes + 1

            if minutes == 60:
                minutes = 0
                hours = hours + 1

    # Add stop
    def stop_time(self):
        input(time.sleep())

    # Add reset
    def reset_time(self):
        pass

    def get_time(self):
        return time.time() - self.start
        self.restart()

    # Add result to object
