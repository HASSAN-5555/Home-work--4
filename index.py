print("Hello, what's your name!")
name = input("What's your name? ")
print(f"Hi, {name}! Thanks for sharing your favorite numbers.")

print("Enter three favorite numbers:")

first_number = int(input("Enter your first favorite number: "))
second_number = int(input("Enter your second favorite number: "))
third_number = int(input("Enter your third favorite number: "))

numbers = [first_number, second_number, third_number]
# Create a list of tuples even or odd

check_list_even_odd = []
for number in numbers :
    if number % 2 == 0:
        check_list_even_odd.append((number, "even"))
    else:
        check_list_even_odd.append((number, "odd"))
        
# Print the even/odd
for number, status in check_list_even_odd:
    print(f"{number} is an {status} number.")

# squares
squares_list = []
for number in numbers:
    squares_list.append((number, number ** 2))

# Print squares
print("\nHere are your favorite numbers and their squares:")
for number, square in squares_list:
    print(f"The square of {number} is {square}.")

total_sum = 0
for number in numbers:
    total_sum += number

print(f"\nThe sum of your numbers is {total_sum}.")

print("Great job exploring your numbers!")

# Check the sum is a prime number
is_prime = True
if total_sum <= 1:
    is_prime = False
else:
    if total_sum <= 3:
        is_prime = True
    else:
        if total_sum % 2 == 0 or total_sum % 3 == 0:
            is_prime = False
        else:
            # Use a for loop to check divisibility
            is_prime = True
            for i in range(5, int(total_sum**0.5) + 1, 6):
                if total_sum % i == 0 or total_sum % (i + 2) == 0:
                    is_prime = False
                    break

if is_prime:
    print(f"The sum, {total_sum}, is a prime number!")
else:
    print(f"The sum, {total_sum}, is not a prime number.")