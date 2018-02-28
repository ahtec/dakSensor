# ================================================
#!/usr/bin/env python
import sys
import datetime
from datetime import timedelta
from dateutil.tz import tzlocal
with open('/proc/uptime', 'r') as f:
uptime_seconds = int(float(f.readline().split()[0]))
uptime_timedelta = timedelta(seconds = uptime_seconds)
uptime_string = str(uptime_timedelta)
today = datetime.datetime.now(tzlocal())
format = "%a %d %b %Y %H:%M:%S %Z"
boot_time = (today - uptime_timedelta).strftime(format)
now = today.strftime(format)
print "Uptime", uptime_string
print "Boot time", boot_time
 # ================================================
