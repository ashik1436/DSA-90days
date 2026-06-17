# 🚀 DSA Mastery: 90-Day Challenge

## 📊 DAILY PROGRESS

### ✅ Day 1: Python Fundamentals
**Problems:** Two Sum, Reverse String
**Topics:** Hash Maps, Two-Pointer  
**Status:** COMPLETE ✅
**Key Learning:** O(1) lookups, in-place swaps

### ✅ Day 2: Arrays & Single-Pass
**Problems:** Best Time to Buy Stock, Contains Duplicate
**Topics:** Min tracking, Hash Sets
**Status:** COMPLETE ✅
**Key Learning:** State tracking, early exit optimization

### ⏳ Day 3: Strings & Validation
**Problems:** Valid Palindrome, Valid Anagram, Longest Substring
**Status:** IN PROGRESS...
**Expected:** [Date]

### Coming Soon...
- Day 4: More string problems
- Day 5: ...
- ...
- Day 90: INTERVIEW READY!

---

## 🔥 CURRENT STATS
- **Days Completed:** 2/90
- **Problems Solved:** 4/90+
- **Streak:** 🔥🔥
- **GitHub Commits:** 2
- **Code Quality:** Production-Ready

---

## 📁 HOW TO USE

Each Day folder has:
- `problemX.py` - Solutions with tests
- `notes.md` - Theory + practical understanding
- `interview-prep.md` - Q&A for interviews

---

**Last Updated:** Day 2
# Day 3: Strings & Palindrome Validation

## 📚 Topics Learned
1. String manipulation basics (indexing, slicing, iteration)
2. Two-Pointer technique for strings
3. Character frequency counting (dictionaries)
4. Sliding window technique (intro)

## ✅ Problems Solved

### Problem 1: Valid Palindrome (LeetCode #125)
- **Status**: ✅ Complete
- **Approach**: String filtering + two-pointer comparison
- **Time Complexity**: O(n)
- **Space Complexity**: O(n) - due to creating cleaned string
- **Optimization**: Can reduce space to O(1) with two-pointer on original string
- **Key Insight**: Filter alphanumeric characters and compare with reverse

### Problem 2: Valid Anagram (LeetCode #242)
- **Status**: ✅ Complete
- **Approach**: Character frequency counting with dictionary
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) - at most 26 lowercase letters
- **Key Insight**: Same length + same character frequencies = anagram

### Problem 3: Longest Substring Without Repeating Characters (LeetCode #3)
- **Status**: ✅ Complete
- **Approach**: Sliding window with set tracking
- **Time Complexity**: O(n)
- **Space Complexity**: O(min(n, m)) where m = charset size
- **Key Insight**: Expand window, shrink when duplicate found, track max length

## 🧠 Key Learnings

### Strings & Two-Pointer
- Two-pointer is efficient for palindrome checking
- Filtering (isalnum()) makes palindrome checking robust
- Case-insensitive comparison needed for real-world palindromes

### Character Frequency
- Dictionaries are O(n) for counting
- Anagrams must have identical character frequencies
- Length check is a quick early exit

### Sliding Window
- Maintain window with two pointers (left, right)
- Expand right to include new characters
- Shrink left when condition violated
- Track max/min while sliding

## 🚀 Next Steps
- Review Day 3 solutions
- Prepare for Day 4: Stacks & Queues
- Continue daily LeetCode streak

**Last Updated:** Day 3