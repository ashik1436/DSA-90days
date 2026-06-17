# DAY 3: STRINGS & PALINDROME VALIDATION

## Learning Objectives

By the end of this study session, you should understand:

* String fundamentals in Python
* String indexing and slicing
* Two Pointer Technique
* Character Frequency Counting
* Hash Maps (Dictionaries)
* Hash Sets
* Sliding Window Pattern
* Complexity Analysis
* Common Interview Questions

---

# Topic 1: String Fundamentals

## What is a String?

A string is a sequence of characters.

Example:

```python
s = "HELLO"
```

Strings in Python are immutable, which means they cannot be modified after creation.

---

## String Indexing

Access individual characters using indexes.

```python
s = "HELLO"

print(s[0])   # H
print(s[1])   # E
print(s[-1])  # O
print(s[-2])  # L
```

### Important

Positive indexing starts from left.

```text
H  E  L  L  O
0  1  2  3  4
```

Negative indexing starts from right.

```text
H  E  L  L  O
-5 -4 -3 -2 -1
```

---

## String Slicing

Used to extract a substring.

```python
s = "PYTHON"

print(s[0:2])   # PY
print(s[2:])    # THON
print(s[:3])    # PYT
print(s[::2])   # PTO
print(s[::-1])  # NOHTYP
```

### Most Important Trick

Reverse a string:

```python
s[::-1]
```

Used frequently in palindrome problems.

---

## Iterating Through Strings

```python
for char in "HELLO":
    print(char)
```

Output:

```text
H
E
L
L
O
```

---

## Useful String Methods

### Lowercase

```python
s.lower()
```

Example:

```python
"HELLO".lower()
```

Output:

```python
hello
```

---

### Uppercase

```python
s.upper()
```

Output:

```python
HELLO
```

---

### Check Alphabet

```python
"a".isalpha()
```

Output:

```python
True
```

---

### Check Digit

```python
"123".isdigit()
```

Output:

```python
True
```

---

### Check Letter or Digit

```python
"a1".isalnum()
```

Output:

```python
True
```

Very important for Valid Palindrome.

---

# Topic 2: Two Pointer Technique

## What is Two Pointer?

Use two pointers:

```python
left = 0
right = len(s) - 1
```

One starts from beginning.

One starts from end.

Move them toward each other.

---

## When to Use?

* Palindrome Problems
* Sorted Arrays
* Pair Finding Problems
* String Comparison

---

## Example: Simple Palindrome

```python
def is_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right:

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
```

---

## Example Walkthrough

Input:

```python
racecar
```

Compare:

```text
r == r
a == a
c == c
```

Pointers meet.

Output:

```python
True
```

---

## Optimized Valid Palindrome

Instead of creating a new string:

```python
cleaned = ""
```

Use two pointers directly.

Benefits:

```text
Time  : O(n)
Space : O(1)
```

---

# Topic 3: Character Frequency Counting

## What is Frequency Counting?

Count how many times each character appears.

Example:

```python
hello
```

Result:

```python
{
'h':1,
'e':1,
'l':2,
'o':1
}
```

---

## Using Dictionary

```python
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
```

---

## Example

```python
s = "hello"
```

Output:

```python
{
'h':1,
'e':1,
'l':2,
'o':1
}
```

---

## Why Frequency Counting?

Used in:

* Anagrams
* Character Counts
* Pattern Matching
* Hash Map Problems

---

# Topic 4: Valid Anagram

## Definition

Two strings are anagrams if:

1. Same length
2. Same characters
3. Same frequencies

---

## Example

```python
listen
silent
```

Frequency:

```python
{
l:1,
i:1,
s:1,
t:1,
e:1,
n:1
}
```

Both strings match.

Output:

```python
True
```

---

## Important Observation

If lengths differ:

```python
abc
abcd
```

Output:

```python
False
```

No need for further checking.

---

# Topic 5: Sliding Window

## What is Sliding Window?

A technique used for substring problems.

Maintain a window:

```python
[left .... right]
```

Expand window:

```python
right += 1
```

Shrink window:

```python
left += 1
```

---

## When to Use?

* Longest Substring
* Shortest Substring
* Subarray Problems
* Duplicate Detection

---

## Longest Substring Without Repeating Characters

Example:

```python
abcabcbb
```

---

### Step 1

Window:

```python
a
```

Length:

```python
1
```

---

### Step 2

Window:

```python
ab
```

Length:

```python
2
```

---

### Step 3

Window:

```python
abc
```

Length:

```python
3
```

---

### Step 4

New Character:

```python
a
```

Duplicate Found.

Remove old:

```python
a
```

Window becomes:

```python
bca
```

Length remains:

```python
3
```

---

Final Answer:

```python
3
```

---

## Why Use a Set?

```python
char_set = set()
```

Advantages:

* O(1) lookup
* O(1) insertion
* O(1) deletion

Perfect for duplicate detection.

---

# Complexity Analysis

## Valid Palindrome

### String Cleaning Approach

```text
Time  : O(n)
Space : O(n)
```

### Two Pointer Approach

```text
Time  : O(n)
Space : O(1)
```

---

## Valid Anagram

### Hash Map Approach

```text
Time  : O(n)
Space : O(n)
```

---

### Sorting Approach

```text
Time  : O(n log n)
Space : O(1)
```

Hash Map is better.

---

## Longest Substring

### Sliding Window

```text
Time  : O(n)
Space : O(n)
```

---

# Key Patterns Learned

## Pattern 1: Two Pointers

```python
left = 0
right = len(s)-1
```

Used For:

* Palindrome
* Pair Problems
* Sorted Arrays

---

## Pattern 2: Hash Map

```python
count = {}
```

Used For:

* Frequency Counting
* Anagrams
* Lookup Problems

---

## Pattern 3: Hash Set

```python
seen = set()
```

Used For:

* Duplicate Detection
* Sliding Window

---

## Pattern 4: Sliding Window

```python
left = 0

for right in range(len(s)):
```

Used For:

* Longest Substring
* Shortest Substring
* Window Problems

---

# Edge Cases Checklist

Always test:

```text
✓ Empty String
✓ Single Character
✓ All Same Characters
✓ All Different Characters
✓ Special Characters
✓ Uppercase / Lowercase
✓ Long Strings
✓ Strings With Spaces
```

---

# Day 3 Summary

Problems Solved:

1. Valid Palindrome
2. Valid Anagram
3. Longest Substring Without Repeating Characters

Patterns Learned:

1. String Manipulation
2. Two Pointers
3. Frequency Counting
4. Hash Map
5. Hash Set
6. Sliding Window

Most Important Concept:

Sliding Window + Two Pointers

These patterns appear very frequently in coding interviews and LeetCode problems.
