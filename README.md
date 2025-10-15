# Apprenticeship Entry Test

This repository contains my solutions for the Apprenticeship Entry Test covering:
1. Logic & Problem Solving  
2. Web / Software Development  
3. Debugging & Reasoning  
4. Version Control & Collaboration

Each section includes both code and explanations.

# SECTION 1: Logic & Problem Solving (10 marks)

## Question 1:
Write a function that returns the second-largest number in a given list of integers.  
(Provide your code and a short explanation of your approach.)

```python
def second_largest(nums):
    if len(nums) < 2:
        return None
    unique_nums = sorted(set(nums), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None
````
## Explanation

The function takes a list of integers (nums) as input then checks whether the list has fewer than 2 elements; if so, it returns None.
It uses set(nums) to remove duplicates and sorted(..., reverse=True) to sort in descending order.
If the sorted unique list has at least 2 elements, it returns the second element (unique_nums[1]); otherwise, it returns None.

# Question 2:
Explain how you would optimize a page that loads too slowly. Mention at least three causes and how you’d fix each.
First identify the root cause and apply specific optimization. 
Some of the cause includes uncompressed and resolution images which increases file size and download time. To resolve this, compress and resize the images.  

Poor server performance due to distance and inadequate hosting. This can be fixed by opting for providers with faster hosting for example AWS and implementing CDN that caches content closer to users and reduces latency.  

Excessive HTTP requests that may overwhelm the browser. This can be minimized by concatenating multiple JS and CSS files.

# Question 3 (Front-end):

You are creating a simple profile page that fetches user data from an API (https://jsonplaceholder.typicode.com/users/1).

## Explain or show code for:

### Fetching and displaying the user’s name and email.

To get user data from the API ( https://jsonplaceholder.typicode.com/users/1), use the fetch() function, which sends a network request and returns a promise.

Use fetch() to call the API.

Convert the response to JSON with .json().

Access the required data fields (name and email).

Display them in the webpage.

---

### Handling the loading and error states.

When fetching data from an API, users should see feedback — either that the data is loading or that an error occurred.

In the loading State before the data arrives, display a message like "Loading user data...". And display this message immediately before the fetch request, and remove it once data arrives.

In the error State If something goes wrong , use .catch() to handle it gracefully and show an error message instead of leaving the user waiting.

# Question 4 (Back-end / Logic):

A small store wants to calculate total sales from this dataset:

[
  {"item": "Pen", "price": 20, "quantity": 3},
  {"item": "Book", "price": 200, "quantity": 2},
  {"item": "Bag", "price": 800, "quantity": 1}
]

Write a short function to calculate the total revenue.

```python
def calculate_total_revenue(sales):
    return sum(item["price"] * item["quantity"] for item in sales)

sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]

total = calculate_total_revenue(sales_data)
print(f"Total Revenue: ${total}")

# Question 5:

You’ve been given this code snippet:

```python
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    if i % 2 == 0:
        numbers.remove(i)
print(numbers)
````
### Questions 
What’s wrong with the code?
Incorrect condition for removing even numbers and modification of the list while iterating.

What will it output?
The code will not print an output; it raises an exception.

How would you fix it to remove even numbers correctly?
First filter out even numbers without modifying the list during iteration and iterate from the end of the list.

# Question 6:

Explain how you would use Git to collaborate on a team project with other developers.

Using Git for collaboration on a team project allows multiple developers to work on the same codebase efficiently, track changes, and avoid conflicts.

---



### One common Git command you use often
Commit

---

### One problem you’ve faced while using Git and how you solved it
Merge conflicts were avoided by not committing changes directly to the master branch; instead, a new branch was created for work.





