# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

# import re
#
# data = '$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19/03/20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|20000|#Bread#19/03/21#40000#'
# foods_pattern1 = r'\#([A-Za-z\sA-za-z]+)\#(\d{2}\/\d{2}\/\d{2})\#(\d+)\#|\|[A-Za-z\sA-za-z]+\|\d{2}\/\d{2}\/\d{2}\|\d+'
#
# result_food1 = re.findall(foods_pattern1, data)
# print(result_food1)
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print(tup)
