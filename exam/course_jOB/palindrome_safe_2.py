# The next step in building logical thinking is building the capacity to incorporate numerical values, and combine mathematical logic with operational logic. Although for some people, the idea of doing maths can be quite intimidating, what you’ll find is that if you build up slowly towards using mathematical logic, it’s not as hard as you anticipated. To help you do exactly that - build up slowly - here’s a slightly more difficult puzzle of a similar type to the previous one, but requiring some very simple calculation.
#
# A safe-breaker is attempting to crack a safe with a 7-combination code. So far they have worked out that:
#
# The first digit is double the third digit
# The code is a palindrome (it reads the same if it is reversed)
# The fourth number is 7
# The third number is one less than the sixth number
# The second number is 3 less than the fourth number
#
# Can you advise the safe-breaker on the correct combination?

fourth = 7
sixt = 3

third = sixt -1
first = third * 2
second = 3
sixt = second
seven = first
fifth = third
combination = []
combination.append(first)
combination.append(second)
combination.append(third)
combination.append(fourth)
combination.append(fifth)
combination.append(sixt)
combination.append(seven)
print(combination)