
# Create SuperBowl Timer

from datetime import datetime
from datetime import date

td = date.today()

sb = date(2019, 2, 3)

if sb is not td:
    print("Sorry there are still {} until Super Bowl 53".format(str(sb - td)))
else:
    print("TODAY IS SUPERBOWL SUNDAY!!!!!")





