import re
from ryanair import Ryanair
ryanair = Ryanair('EUR')

flights = ryanair.get_flights('PDV', '2022-10-27', '2022-11-03')
''.join([str(flights)])
flight1 = re.findall('[a-zA-Z\d]+', str(flights))
''.join(flight1)
backflights = ryanair.get_return_flights("STN", "2022-10-27", "2022-10-30", "2022-11-01", "2022-11-03")

print(flight1)
print(backflights)