from croniter import croniter
from datetime import datetime

base = datetime.now()
iter = croniter('* * * * *', base)


def check_time():
    h, min, day = input(
        "type time you want to start:\n H M fri,wed,sun\n ").split()

    while True:
        t = iter.get_next()
        now = datetime.now()

        # min hour "*st in month" *  *  day= wed,fri
        if croniter.match("{} {} * * * {}".format(int(min), int(h), day), now):
            return True
