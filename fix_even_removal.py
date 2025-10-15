# Original buggy code
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)  # Wrong logic

# ✅ Fixed version
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)  # Output: [1, 3, 5]

What’s wrong with the code?
Incorrect condition for removing even numbers and modification of list while iterating
What will it output?
The code will not print an output rather raises an exception:
How would you fix it to remove even numbers correctly?
First filter out even numbers without modifying the list during iteration and Iterate from the end of the list
