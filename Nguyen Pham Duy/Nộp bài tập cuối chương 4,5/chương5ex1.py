count = 0
total = 0 
while True:
    try:
        line = input("Enter a number: ")
        if line.lower() == 'done':
            break
        number = float(line)
        total = total + number 
        count = count + 1     
    except ValueError:
        print("Invalid input")
if count > 0:
    average = total / count 
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")
else:
    print("No valid numbers were entered.")