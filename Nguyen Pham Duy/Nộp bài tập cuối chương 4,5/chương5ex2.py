largest = None
smallest = None
while True:
    try:
        line = input("Enter a number: ")
        if line.lower() == 'done':
            break
        number = float(line)
        if smallest is None:
            smallest = number
        elif number < smallest:
            smallest = number
        if largest is None:
            largest = number
        elif number > largest:
            largest = number
    except ValueError:
        print("Invalid input")
if largest is not None:
    print(f"Maximum: {largest}")
    print(f"Minimum: {smallest}")
else:
    print("No valid numbers were entered.")