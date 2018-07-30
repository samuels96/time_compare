from datetime import *
from countryinfo import *
from helpers import *
import time
import sys
from pytz import timezone
from builtins import input


def main():
    tzone = []
    slow_print(bcolors.BOLD+"Enter the name of continent,country or capital city you wish to display time of.\n")
    slow_print("When you are done adding entries, type 'q' or leave the input blank and hit enter\nPress ctrl-c to quit the program anytime.\n")
    slow_print("...\n",0.2),
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print("\n")
    c = 0

    while True:
        x = input()
        if x in ["","q","Q"]:
            break
        else:
            c += 1
            if get_timezone(x) != "Timezone not found":
                if get_timezone(x) in tzone:
                    sys.stdout.write("\033[F")
                    slow_print("{} has been already added\n".format(get_timezone(x)))
                else:
                    tzone.append(get_timezone(x))
                    sys.stdout.write("\033[F")
                    slow_print("{} added\n".format(get_timezone(x)))
            else:
                sys.stdout.write("\033[F")
                slow_print(get_timezone(x)+"\n")


    for _ in range(c+2):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

    slow_print("."*50,0.01),
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    print(bcolors.GREEN+"_"*50+bcolors.ENDC+bcolors.BOLD)


    while True:
        for tz in tzone:
            get_time(tz)
        time.sleep(1)
        for _ in range(len(tzone)):
            sys.stdout.write("\033[F")

if __name__ == "__main__":
    main()
