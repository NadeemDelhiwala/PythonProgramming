# Define an isPalindrome function that takes one word in string as input and
# returns True if it is palidrome else return False

# palidrome - words that reads same backward as forwards

# example:
# is_Palidrome("madama") -----> True 
# is_Palidrome("naman") ----->  True
# is_Palidrome("horse")  ---->  False

# Logic (algorithm)

# step 1 --> reverse a string
# step 2 --> compare reversed string with the original string

# approach 1
# def is_Palidrome(word):
#   reserved_word = word[::-1]
#   if word == reserved_word:
#     return True
#   return False


# # approach 2
# def is_Palidrome(word):
#   if word == word[::-1]:
#     return True
#   return False

# # approach 3
def is_Palidrome(word):
  return word == word[::-1]

print(is_Palidrome("madam"))
print(is_Palidrome("naman"))
print(is_Palidrome("horse"))

