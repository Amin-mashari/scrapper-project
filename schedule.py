from croniter import croniter
from datetime import datetime
from config import read_conf_data

base = datetime.now()
iter = croniter('* * * * *', base)


def check_time():
    print("time logging....")

    while True:
        now = datetime.now()

        if croniter.match((read_conf_data("config.yml")["schedule"]["sch_format"]), now):
            return True
