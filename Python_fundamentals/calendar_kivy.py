from datetime import datetime
import calendar
import kivy

kivy.require('1.0.7')

#from kivy.app import App
#from kivy.clock import _classes
#class Clock(App):

 #   def build(self):
  #      return _classes
   # print(kivy.clock)


class _localized_day:
    # January 1, 2001, was a Monday.
    _days = [datetime.date(2001, 1, i + 1).strftime for i in range(7)]

    def __init__(self, format):
        self.format = format

    def __getitem__(self, i):
        funcs = self._days[i]
        if isinstance(i, slice):
            return [f(self.format) for f in funcs]
        else:
            return funcs(self.format)

    def __len__(self):
        return 7
# Full and abbreviated names of weekdays
day_name = _localized_day('%A')
day_abbr = _localized_day('%a')

# Full and abbreviated names of months (1-based arrays!!!)
month_name = _localized_month('%B')
month_abbr = _localized_month('%b')

# Constants for weekdays
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
