#Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(a_list):
    largest_num=a_list[0]
    for n in range(1,len(a_list)):
        if a_list[n]>largest_num:
            largest_num=a_list[n]
    return largest_num
    

my_list=[1,9,10,60,1000,88,300,500,700]
print(largest(my_list))
