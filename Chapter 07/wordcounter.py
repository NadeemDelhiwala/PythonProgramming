# word counter
# harshit
d = {'h':2, 'a':1, 'h':3}
print(d)


def wordcounter(s):
  count_chars = {}
  for char in s:
    # key             = value
    count_chars[char] = s.count(char)
  return count_chars


print(wordcounter('harshit'))
