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

