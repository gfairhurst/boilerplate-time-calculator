def add_time(start, duration, weekday=False):
  
  start = to_min(start)
  duration = to_min(duration)
  new_time_min = start+duration
  new_time_hour = to_hour(new_time_min,weekday)

  return new_time_hour


def to_min(time_):
  pm=False
  if time_[-2:].lower()=="pm":
    pm = True
    time_=time_[:-3]
  if time_[-2:].lower()=="am":
    time_=time_[:-3] 

  time_=time_.split(":")
  time_ = int(time_[0])*60+int(time_[1])+pm*12*60

  return time_

def to_hour(min_, weekday=False):
  
  days = min_ // (24*60)
  min_ = min_ % (24*60)
  hours = min_ // 60
  minutes = min_ - hours * 60

  if isinstance(weekday, str):
    if weekday.lower() == "monday":
      wd = 0
    if weekday.lower() == "tuesday":
      wd = 1
    if weekday.lower() == "wednesday":
      wd = 2
    if weekday.lower() == "thursday":
      wd = 3
    if weekday.lower() == "friday":
      wd = 4
    if weekday.lower() == "saturday":
      wd = 5
    if weekday.lower() == "sunday":
      wd = 6  
    
    wd=(wd+days)%7

    if wd == 0:
      weekday = ", Monday"
    if wd == 1:
      weekday = ", Tuesday"
    if wd == 2:
      weekday = ", Wednesday"
    if wd == 3:
      weekday = ", Thursday"
    if wd == 4:
      weekday = ", Friday"
    if wd == 5:
      weekday = ", Saturday"
    if wd == 6:
      weekday = ", Sunday"



  if (hours <12) | (hours == 24):
    if hours == 0:
      hours = 12
    AMPMtail = " AM"
  else:
    hours = hours - 12
    if hours == 0:
      hours = 12
    AMPMtail = " PM"

  tail = ""
  if days == 1:
    tail = " (next day)"
  if days >1:
    tail = " ({} days later)".format(days)


  if weekday: 
    return "%d:%02d"%(hours, minutes) + AMPMtail + weekday + tail
  else:
    return "%d:%02d"%(hours, minutes) + AMPMtail + tail