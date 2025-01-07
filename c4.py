#Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.(HINT: Review your notes on *args).

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(10,5,10,2))