#Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num):
    sum=0
    for n in range(1,num+1):
        sum+=n
    return sum
    
print(sum_to(10))