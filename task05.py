# a program that outputs whether or not today is a weekday
# Author: Anna Kozakiewicz

from datetime import datetime
d = datetime(2022, 3, 15);
if d.weekday()>4:
    print ('It is the weekend, yay!')
else:
    print ('Yes, unfortunately today is a weekday')