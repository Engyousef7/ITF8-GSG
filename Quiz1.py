def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
def is_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


choice = int(input("Choose an option:\n1. Check if a number is palindrome\n2. Check if a number is even or odd\n"))

if choice == 1:
    num = int(input("Enter a number: "))
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
elif choice == 2:
    num = int(input("Enter a number: "))
    result = is_even_odd(num)
    print(f"{num} is {result}.")
else:
    print("Invalid choice.")