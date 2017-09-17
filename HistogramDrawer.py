import matplotlib.pyplot as plt
import numpy as np


class HistogramDrawer:
    def __init__(self, sequence, interval_count = 20):
        self.sequence = sequence
        self.interval_count = interval_count
        self.intervals = None
        self._init_intervals()

    def _init_intervals(self):
        maximum = max(self.sequence)
        minimum = min(self.sequence)
        step = (maximum - minimum) / self.interval_count
        self.intervals = [0 for _ in range(self.interval_count)]

        interval_index = 0
        value_index = 0
        self.sequence.sort()
        interval_max_board = minimum + step

        while interval_index < 20 and value_index < len(self.sequence):
            if self.sequence[value_index] <= interval_max_board:
                self.intervals[interval_index] += 1
                value_index += 1
            else:
                interval_index += 1
                interval_max_board += step

    def draw(self):
        _sum = sum(self.intervals)
        plt.bar(np.arange(self.interval_count),
                list(map(lambda x: x / sum(self.intervals), self.intervals)),
                color='yellow',
                edgecolor='black',
                width=0.8
                )
        plt.xticks(np.arange(self.interval_count), np.arange(self.interval_count))
        plt.show()