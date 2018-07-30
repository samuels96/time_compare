from datetime import *
from countryinfo import countries
from helpers import *
import time
import sys
from pytz import timezone


def get_timezone(inp):
    for x in range(len(countries)):
        if inp[0].upper()+inp[1:].lower() in str(countries[x]):
            return countries[x]["timezones"][0]
    return "Timezone not found"

def get_time(tz):
    get_tz = timezone(tz)
    set_time = datetime.now(get_tz)
    print("{:39}|{:>10} ".format(tz,set_time.strftime('%H:%M:%S')))


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ORANGE = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def slow_print(s,t=0.02):
    for x in s:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(t)
