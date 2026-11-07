# Q9. Write a function la_prime(n)that returns true if is a prime number and
# false otherwise, using a loop

def la_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        else:
            return True
print(la_prime(7))