
import re
#re for regex is built in function
txt = "PROGRAMMING FUNDAMENTALS WITH PYTHON - МАЙ 2022"
x = re.search("\d{3}$", txt)
y = re.findall('MI', txt)
print(x)
print(y)
#we can copy and code generator from regex.101 website
#we can use and pattern from the internet for examples like birthday,driver licenses etc.