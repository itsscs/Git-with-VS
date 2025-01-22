def find_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
number = int(input("Enter a number: "))
result = find_even_or_odd(number)
print(f"The number {number} is {result}.")
print("Great Work!")