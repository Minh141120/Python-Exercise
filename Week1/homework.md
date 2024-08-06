## Exercise 1: Count Positive and Negative Numbers in a List

```python
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

positive_numbers = [x for x in data1 if x > 0]
negative_numbers = [x for x in data1 if x < 0]
```

## Exercise 2: Extract Elements with Frequency Greater than k

```python
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

sett = set(data2)
res = {key: data2.count(key) for key in sett if data2.count(key) > 3}
print(res)

```

## Exercise 3: Find the Strongest Neighbour

```python
# Given an array of N positive integers, find the maximum for every adjacent pair in the array.

def max_adjacent_pairs(arr):
    if len(arr) < 2:
        return []
    max_pairs = []
    for i in range(len(arr) - 1):
        max_pairs.append(max(arr[i], arr[i+1]))
    return max_pairs

data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]
result = max_adjacent_pairs(data3)
print(result)
```

## Exercise 4: Print All Possible Combinations from Three Digits

```python
import itertools

def print_combinations(arr):
    combinations = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if i != j and j != k and i != k:
                    combinations.append([arr[i], arr[j], arr[k]])
    return combinations

data4 = [1, 2, 3]
# combinations = list(itertools.permutations(data4))
# for combo in combinations:
#     print(combo)
    
res = print_combinations(data4)
print(res)
```

## Exercise 5: Add Elements to Each Row from Initial Matrix

```python
# Given two matrices (2 nested lists), write a Python program to add elements to each row from the initial matrix.
# For example:
# Input: test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]]
#        test_list2 = [[1], [9], [8]]
# Output: [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]

data5_list1 = [[4, 3, 5], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

# for idx, row in enumerate(data5_list1):
#     row.extend(data5_list2[idx])

for row1, row2 in zip(data5_list1, data5_list2):
    row1.extend(row2)

print(data5_list1)
```
## Exercise 6: Find Numbers Divisible by 7 but Not a Multiple of 5

```python
# Write a program to find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

res = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        res.append(str(num))
print(', '.join(res))
```
## Exercise 7: Find Numbers with All Even Digits

```python
# Write a program to find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def is_all_even_digits(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

res = []
for num in range(1000, 3001):
    if is_all_even_digits(num):
        res.append(str(num))

print(', '.join(res))
```

## ## Exercise 8: Shortest Word Chain

```python
from collections import defaultdict, deque
import itertools

def load_words(file_path):
    with open(file_path, 'r') as f:
        return set(word.strip().lower() for word in f if len(word.strip()) >= 3)

def build_graph(words):
    graph = defaultdict(list)
    for word in words:
        key = word[:2]
        graph[key].append(word)
    return graph

def find_shortest_chain(start, end, words):
    graph = build_graph(words)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path

        last_two = current[-2:]
        for next_word in graph[last_two]:
            if next_word not in visited:
                visited.add(next_word)
                queue.append((next_word, path + [next_word]))

    return None

def main():
    words = load_words('./wordsEn.txt')
    start = input("Please enter the start word: ").lower()
    end = input("Please enter the goal word: ").lower()
    
    if start not in words or end not in words:
        print("Both start and end words must be in the dictionary.")
        return

    chain = find_shortest_chain(start, end, words)
    if chain:
        print("The shortest chain is:")
        for word in chain:
            print(word)
    else:
        print("No valid chain found.")

if __name__ == "__main__":
    main()
```