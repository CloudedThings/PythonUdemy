import time
import datetime
import pytz

# print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("current timezone is {0} with offset {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight saving time is in effect for this location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
#
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

country = "America/New_York"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("Not time zone defined")