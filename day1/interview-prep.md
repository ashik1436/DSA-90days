# Day 1: Interview Preparation

## 🎤 CONCEPT QUESTIONS

### Q1: Explain what a hash map is. How does O(1) lookup work?
**My Answer:**
A hash map stores key-value pairs. When you add a key, it uses a hash function to compute where to store it in memory. When you lookup a key, it uses the same hash function to instantly find where it is - no searching needed. That's why it's O(1).

Example: Think of it like a library. Instead of checking every shelf (O(n)), you look up the call number (hash function) and go straight to the shelf. Instant!

---

### Q2: Why is Two-Pointer more efficient than checking all pairs?
**My Answer:**
Checking all pairs = nested loops = O(n²). For 1 million items, that's 1 trillion operations.

Two-Pointer = single loop = O(n). For 1 million items, that's 1 million operations.

We avoid nested loops by processing from both ends. As we move inward, we know we've already checked outer pairs, so no need to check twice.

---

### Q3: What's the time complexity of reversing a string with Two-Pointer? Why?
**My Answer:**
O(n) time because we visit each character exactly once. We have two pointers starting from opposite ends, moving towards middle. Each character is visited once and swapped, so n operations total.

---

### Q4: Could we solve Two Sum with a nested loop instead?
**My Answer:**
Yes, but it would be O(n²):
```python
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```
Works but slow for large arrays. Hash map is better.

---

### Q5: In Reverse String, why is Two-Pointer O(1) space but nested loops would be O(n)?
**My Answer:**
Two-Pointer just needs 2 variables (left, right) = O(1) space.

If we used nested loops or created a new array, we'd need O(n) extra space.

In-place swapping = memory efficient.

---

## 🧠 PROBLEM-SPECIFIC QUESTIONS

### Two Sum - Interview Style

**Q: Walk me through your approach for Two Sum**

A: I use a hash map. As I iterate through the array:
1. For each number, I calculate what I need: complement = target - number
2. I check if I've already seen this complement
3. If yes, I found my pair → return indices
4. If no, I store the current number for future reference

This gives O(n) time because dictionary lookup is O(1), and I only loop once.

---

**Q: What if there are multiple valid pairs?**

A: The problem asks for ONE pair, so I return the first one I find. If it asked for all pairs, I'd:
1. Use same hash map approach to find all
2. Return list of all valid pairs

---

**Q: Can you solve it without hash map?**

A: Yes, but less efficient:
1. Sort the array: O(n log n)
2. Use two-pointer on sorted array: O(n)
3. Total: O(n log n) time, O(1) space (if sorting in-place)

Hash map approach is better: O(n) time.

---

**Q: Space-time tradeoff - explain your choice**

A: I chose O(n) space to get O(n) time.

Alternative (nested loops): O(1) space, O(n²) time.

For large arrays, O(n) time is much better than O(n²) time, even if it uses more memory. Memory is cheap, speed is important.

---

### Reverse String - Interview Style

**Q: Explain your two-pointer solution**

A: I use two pointers:
- Left starts at index 0
- Right starts at last index

I move them towards each other, swapping elements at each step. When they meet in the middle, I'm done.

Time: O(n) - visit each element once
Space: O(1) - only pointers, no new array

---

**Q: Why not use Python's built-in reverse()?**

A: The problem tests understanding of algorithm design, not library functions. Using reverse() would be cheating - they want to see problem-solving skill.

---

**Q: Can you do it without swapping?**

A: No, the problem requires in-place modification. We can't use new array (would be O(n) space).

Swapping in-place is the optimal way.

---

## 🔥 TRICKY QUESTIONS

**Q: What if the array is empty?**
A: Two Sum - problem guarantees exactly one solution, so non-empty
   Reverse String - empty array stays empty

**Q: What if target is impossible?**
A: Two Sum - problem guarantees solution exists

**Q: What about duplicate values?**
A: Two Sum - can have duplicates, indices must be different
   Works fine with hash map

**Q: What about negative numbers?**
A: Both solutions work with negatives - no special handling needed

---

## 📝 MOCK INTERVIEW TRANSCRIPT

**Interviewer:** "Solve Two Sum in 30 minutes"

**You:** "I understand. Let me think...
- I need two numbers that add to target
- Could check all pairs but that's O(n²)
- Better approach: use hash map
- As I see each number, check if I've seen the complement
- This way O(n) time with one loop

Let me code it..."

[Write code]

**Interviewer:** "What's the complexity?"

**You:** "Time: O(n) - single loop, dictionary lookup is O(1)
Space: O(n) - storing numbers in dictionary"

**Interviewer:** "Any optimizations?"

**You:** "For this problem, O(n) time is optimal. Can't do better than linear because we need to check each element."

✅ **Strong answer!**

---

## 🎯 INTERVIEW TIPS FOR THESE PROBLEMS

1. Always state time and space complexity
2. Explain why you chose this approach
3. Mention tradeoffs
4. Talk through examples before coding
5. Don't just copy-paste - show thinking