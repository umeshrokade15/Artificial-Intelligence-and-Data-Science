# Q5. Write a function to return the sum of digits of a number, .

sum=0
def sum_of_digits(a):
    while(a>0):
        sum= sum+a%10
        a = a/10
    print(sum)

sum_of_digits(115)
