# Q10. Letʼs create a “NumberGuessing Game”. Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:
# • "Too High"if the guess is above the number
# • "Too Low"if the guess is below
# • "Correct"if the guess matches

num = 10
while True:
    user_guess = int(input("Enter Your Guess"))
    if user_guess == num:
        print("Guessed")
        break
    elif user_guess<num:
        print("Too Low")
    else:
        print("Too High") 
       
