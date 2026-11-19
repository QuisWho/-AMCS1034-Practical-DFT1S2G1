numbers = []

while True:
    number = input("Enter an integer or 'Q'/'q' to exit:")

    if number == "Q" or number == 'q':
        break
    try:
        numbers.append(int(number))
    except ValueError:
        print("Only integer are allowed!")
        
if len(numbers):
        numbers = numbers[::-1]

        print("\nIntegers in reversed order:",end="")
        for num in numbers:
            print(num,end=" ")

else:
    print("No Integers.")