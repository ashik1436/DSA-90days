# Day 3 Interview Preparation

# Problem 1: Valid Palindrome

## Original Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch

        rev = cleaned[::-1]

        return cleaned == rev
```

---

## Q1: How did you handle special characters and spaces?

### Interview Answer

I converted the string to lowercase and used `isalnum()` to keep only letters and numbers. This removes spaces and special characters automatically. Then I compared the cleaned string with its reverse.

### Example

```python
s = "A man, a plan, a canal: Panama"
```

After lowercase:

```python
"a man, a plan, a canal: panama"
```

After cleaning:

```python
"amanaplanacanalpanama"
```

Reverse:

```python
"amanaplanacanalpanama"
```

Result:

```python
True
```

---

## Q2: What is the time complexity?

### Interview Answer

The time complexity is O(n).

Reason:

1. Traverse string to clean it → O(n)
2. Reverse string → O(n)
3. Compare strings → O(n)

Overall:

```text
O(n)
```

### Space Complexity

```text
O(n)
```

because we create cleaned and reversed strings.

---

## Q3: What edge cases did you test?

### Edge Case 1

```python
s = ""
```

Output:

```python
True
```

---

### Edge Case 2

```python
s = "a"
```

Output:

```python
True
```

---

### Edge Case 3

```python
s = "!!!"
```

Cleaned:

```python
""
```

Output:

```python
True
```

---

### Edge Case 4

```python
s = "race a car"
```

Cleaned:

```python
"raceacar"
```

Reverse:

```python
"racaecar"
```

Output:

```python
False
```

---

# Problem 2: Valid Anagram

## Original Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False

            count[ch] -= 1

            if count[ch] < 0:
                return False

        return True
```

---

## Q4: Did you use dictionary, Counter, or sorting? Why?

### Interview Answer

I used a dictionary because it provides O(1) average lookup and update operations.

Dictionary solution:

```python
count = {}
```

Sorting solution:

```python
sorted(s) == sorted(t)
```

Sorting takes:

```text
O(n log n)
```

Dictionary takes:

```text
O(n)
```

So dictionary is more efficient.

---

### Example

```python
s = "listen"
t = "silent"
```

Dictionary after first loop:

```python
{
'l':1,
'i':1,
's':1,
't':1,
'e':1,
'n':1
}
```

After processing second string:

```python
{
'l':0,
'i':0,
's':0,
't':0,
'e':0,
'n':0
}
```

Result:

```python
True
```

---

## Q5: Why can strings of different lengths never be anagrams?

### Interview Answer

Anagrams must contain exactly the same characters with exactly the same frequencies.

Example:

```python
"abc"
"abcd"
```

The second string contains an extra character.

Therefore frequencies cannot match.

Result:

```python
False
```

---

### Complexity

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

# Problem 3: Longest Substring Without Repeating Characters

## Original Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length = max(
                max_length,
                right - left + 1
            )

        return max_length
```

---

## Q6: Explain how the sliding window moves through "abcabcbb".

### Interview Answer

I use two pointers:

```python
left
right
```

and a set to store current window characters.

### Walkthrough

Input:

```python
"abcabcbb"
```

Step 1

```python
"a"
```

Length:

```python
1
```

---

Step 2

```python
"ab"
```

Length:

```python
2
```

---

Step 3

```python
"abc"
```

Length:

```python
3
```

---

Next character:

```python
"a"
```

Duplicate found.

Remove old:

```python
"a"
```

Window becomes:

```python
"bca"
```

Length:

```python
3
```

Maximum remains:

```python
3
```

---

## Q7: How do you track characters in the current window?

### Interview Answer

I use a set.

```python
char_set = set()
```

Example:

```python
{'a','b','c'}
```

Checking:

```python
'a' in char_set
```

takes O(1) time.

---

## Q8: What happens when a repeated character appears?

### Interview Answer

When a duplicate is found:

```python
while s[right] in char_set:
```

I keep removing characters from the left side.

Example:

Current window:

```python
abc
```

New character:

```python
a
```

Duplicate found.

Remove:

```python
a
```

Window:

```python
bc
```

Now add current character:

```python
a
```

Window becomes:

```python
bca
```

Continue processing.

---

### Complexity

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

# General Questions

## Q9: Which problem was hardest and why?

### Interview Answer

Longest Substring Without Repeating Characters was the hardest because it required understanding the Sliding Window technique and managing two pointers correctly.

---

## Q10: If you had to optimize one solution further, which one?

### Interview Answer

I would optimize Valid Palindrome.

Current:

```text
Time: O(n)
Space: O(n)
```

Using Two Pointers:

```python
left = 0
right = len(s)-1
```

we can achieve:

```text
Time: O(n)
Space: O(1)
```

which is more memory efficient.
