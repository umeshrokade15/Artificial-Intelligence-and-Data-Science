# Q7. Design a program to continuously input a number from user & print if it is
# positive or negative until the user enters “Quit”.

def user_input():

    while True:
        num = input("Enter a Number :")
        if num == "Quit":
            break
        else:
            num=int(num)
            if num>0:
                print("Number is positive")
            else:
                print("Number is Negative")
user_input()
