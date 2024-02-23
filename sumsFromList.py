def sumList(numbers, count):
    total = 0
    for i in range(count):
        try:
            total += numbers[i]
        except IndexError:
            print(f"Error: No number found at index {i}")
    return total


def getNumber():
    while True:
        try:
            number = int(input("Enter a number: ")) 
            return number
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    numbers = []
    while True:
        print("Enter a non-negative number to add to the list.")
        print("Or enter a negative number to stop.")
        number = getNumber()
        if number >= 0:
            numbers.append(number)
        else:
            break

    while True:
        print("Enter many numbers from the list would you like to sum up.")
        print("Or enter a negative number to stop.")
        count = getNumber()
        if count >= 0:
            # Could maybe do exception handling here instead of within function to prevent print
            total = sumList(numbers, count)
            print(f"The sum of the first {count} numbers is {total}")     
        else:
            break


main()
