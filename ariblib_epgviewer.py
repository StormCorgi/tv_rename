from ariblib import tsopen
from ariblib.event import events

import sys

with tsopen(sys.argv[1]) as ts:
    for event in events(ts):
        max_len = max(map(len, event.__dict__.keys()))
        template = "{:%ds}  {}" % max_len
        for key, value in event.__dict__.items():
            print(template.format(key, value))
        print('-' * 80)
