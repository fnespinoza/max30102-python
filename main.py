from heartrate_monitor import HeartRateMonitor
import time
import argparse
import dash
t = 30

parser = argparse.ArgumentParser(description="Read and print data from MAX30102")
parser.add_argument("-r", "--raw", action="store_true",
                    help="print raw data instead of calculation result")
args = parser.parse_args()

print('sensor starting...')
hrm = HeartRateMonitor()
hrm = HeartRateMonitor(print_raw=args.raw, print_result=(not args.raw))
hrm.start_sensor()

try:
    time.sleep(t)
except KeyboardInterrupt:
    print('keyboard interrupt detected, exiting...')


hrm.stop_sensor()
print('sensor stopped!')