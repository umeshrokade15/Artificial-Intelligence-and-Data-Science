# Q3. Write a function that prints the digits of a number, .
# For eg: n=312, there are 3 digits in it 3, 1 and 2 & we need to print them.

def PrintDigit(a):
    ans = str(a)
    print(type(ans))
    for digits in ans:
        print(digits)

PrintDigit(312)
