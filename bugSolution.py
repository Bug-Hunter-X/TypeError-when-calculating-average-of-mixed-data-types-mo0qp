def calculate_average(numbers):
    try:
        total = sum(numbers)
        count = len(numbers)
        if count == 0:
            return 0
        return total / count
    except TypeError:
        print("Error: List contains non-numeric values.")
        return None # Or handle the error as appropriate

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = [10, 20, 'a']
average = calculate_average(my_list) #This will print the error message, but not crash