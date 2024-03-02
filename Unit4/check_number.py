#Write a Python program which reads in an integer
#and prints whether the integer is negative, zero or positive
def check(number):
    if number < 0:
        print("Negative")
    elif number == 0:
        print("Zero")
    else:
        print("Positive")