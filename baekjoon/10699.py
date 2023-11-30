import datetime

utc_dt = datetime.datetime.utcnow()
tz_diff = datetime.timedelta(hours=9)
utc_dt = utc_dt + tz_diff
print(utc_dt.strftime("%Y-%m-%d"))
