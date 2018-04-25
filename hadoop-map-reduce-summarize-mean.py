#mapper
import sys
import datetime as datetime
for line in sys.stdin:
    data = line.strip().split("\t")
    print data
    if len(data)!=6: continue
    weekday = datetime.strptime(date, '%Y-%m-%d').weekday()
    if weekday == 0: weekday = 'Sunday'
    elif weekday == 1: weekday = 'Monday'
    elif weekday == 2: weekday = 'Tuesday'
    elif weekday == 3: weekday = 'Wednesday'
    elif weekday == 4: weekday = 'Thursday'
    elif weekday == 5: weekday = 'Friday'
    elif weekday == 6: weekday = 'Saturday'
    weekday, time, store, item, cost, payment = data
    print "{0}\t{1}".format(weekday,cost)

#reducer
import sys
import numpy as np
salesArray = []
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisSale = data
    if oldKey and oldKey != thisKey:
      print oldKey, "\t", np.mean(salesArray)
      oldKey = thisKey
      salesArray = []

     oldKey = thisKey
     salesArray.append(thisSale)

 if oldKey != None:
   print oldKey, "\t", np.mean(salesArray)
