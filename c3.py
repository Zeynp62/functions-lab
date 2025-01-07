#Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(string, substr):
  return string.count(substr)

print(occurances("Hello World","ll"))