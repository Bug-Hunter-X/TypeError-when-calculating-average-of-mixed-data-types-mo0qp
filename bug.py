def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return total / count

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 0, as intended

my_list = [10,20,30,40,50]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 30.0, as intended

my_list = [10,20, 'a']
average = calculate_average(my_list) #This will throw TypeError