#FirstVariant
#def palindrome_filter(word):
    #if word == word[::-1]:
        #return word

#words = input().split(' ')
#palindrome = input()
#palindrome_list = [word for word in words if palindrome_filter(word)]

#print(palindrome_list)
#print(f'Found palindrome {palindrome_list.count(palindrome)} times')

strings = input().split(" ")
searched_palindrome = input()
palindromes = []

for word in strings:
    if word == "".join(reversed(word)):
        #join method is working with double quotes only ""
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
    # We use the join() method with the reversed() method because reversed() returns an iterator, not a string,
    # so we should make it into one
