
class Tahoe:

    def __init__(self):
        self.cwnd = 1       # dimensiunea ferestrei
        self.prag = 30      # sstresh
        self.buffer_pachete = []

    def getCwndSize(self):
        if (self.cwnd < self.prag):
            self.cwnd = self.cwnd*2
        else:
            self.cwnd = self.cwnd + 1

        return self.cwnd

