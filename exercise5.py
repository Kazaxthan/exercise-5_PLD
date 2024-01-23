#exercise5
#Exercise 5: Check if the first and last number of a list is the same
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def first_and_last_same(list):
    first_digit = list[0]
    last_digit = list[-1]

    if first_digit == last_digit:
        return True
    else:
        return False

# Ask the user for input
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the user input into a list of integers
try:
    user_list = [int(x) for x in user_input.split()]
except ValueError:
    print("Invalid input. Please enter a valid list of numbers.")
    exit()

# result
result = first_and_last_same(user_list)

print(f"The first and last numbers in the list are the same: {result}","\n Original numbers:", user_input)
