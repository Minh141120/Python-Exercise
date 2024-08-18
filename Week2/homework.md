# Homework Week 2

## Exercise 1
```python
# Ex1: Write a NumPy program to reverse an array (first element becomes last).
data = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
print(data[::-1])
```

## Exercise 2

```python
# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
import numpy as np
arr1 = np.array([0, 10, 20, 40, 60])
arr2 = np.array([10, 30, 40])

result = np.in1d(arr1, arr2)
print(arr1[result])
```

## Exercise 3

```python
# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
import numpy as np
arr = np.array([1, 6, 4, 8, 9, -4, -2, 11])

max_index = np.argmax(arr)
min_index = np.argmin(arr)

print("Index of the maximum value:", max_index)
print("Index of the minimum value:", min_index)

```
## Exercise 4

```python
# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

import re


word_counts = {}
with open('./story.txt', 'r') as file:
    text = file.read()
    words = re.findall(r'\b\w+\b', text.lower())
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    most_common_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:100]
    
    for word, count in most_common_words:
        print(f"{word}: {count}")

```