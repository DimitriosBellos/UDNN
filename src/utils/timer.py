from __future__ import absolute_import
import time

from torch.utils.trainer.plugins.monitor import Monitor


class Timer(Monitor):
    stat_name = 'time'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('unit', 'ms')
        kwargs.setdefault('precision', 0)
        super(Timer, self).__init__(*args, **kwargs)
        self.last_time = time.time()

    def get_value(self, *args):
        if self.last_time:
            now = time.time()
            duration = now - self.last_time
            #self.last_time = now
            return duration
        else:
            self.last_time = time.time()
            return
