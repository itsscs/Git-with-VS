def find_even_or_odd(number):
    if number != 0:
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Zero"

number = int(input("Enter a number: "))
result = find_even_or_odd(number)
print(f"The number {number} is {result}.")
print("Great Work!")
if result == "Even":
    print("😊")
if result == "Odd":
        print("😁")