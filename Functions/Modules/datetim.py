from time import perf_counter as my_timer, get_clock_info
import time

print("time():\t\t", time.get_clock_info('time'))
print("perf_counter:\t", time.get_clock_info('perf_counter'))
print("process_time():\t", time.get_clock_info('process_time'))