# Day 2: Interview Preparation

## 🎤 CONCEPT QUESTIONS

### Q1: Why is single-pass better than nested loops?
**Answer:**
Single pass = O(n) = n operations
Nested loops = O(n²) = n × n operations

For 1,000 items:
- Single pass = 1,000 operations
- Nested loops = 1,000,000 operations

Single pass is 1000x faster!

---

### Q2: How do you decide what to "track" in a single-pass algorithm?
**Answer:**
Ask yourself: "What information do I need as I go?"

Stock problem: Need to know minimum price before current price → track min
Duplicate problem: Need to know if I've seen number → track seen set

The answer tells you what to track.

---

### Q3: Can you solve stock problem with nested loops?
**Answer:**
Yes:
```python
for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        profit = prices[j] - prices[i]
        max_profit = max(max_profit, profit)
```
Time: O(n²) - checks all pairs
Space: O(1)

My approach: O(n) time - only one loop. Better!

---

## 🧠 INTERVIEW QUESTIONS

### Stock Problem Interview

**Q: Walk through your solution**

A: For the stock problem:
1. I track the minimum price I've seen so far
2. For each new price, I calculate what profit I'd get if selling today
3. I keep track of the maximum profit
4. One loop through prices gives me the answer

Time: O(n) - single loop
Space: O(1) - just variables

---

**Q: What if you wanted maximum profit with multiple buys/sells?**

A: Different problem (Leetcode #122). You'd:
1. Buy at every local minimum
2. Sell at every local maximum
3. Similar approach but slight variation

For THIS problem (single buy/sell), my approach is optimal.

---

**Q: Optimization ideas?**

A: Current approach is already O(n) optimal. Can't do better because we must check each price.

Could use different approach:
- Sort prices: O(n log n) time - slower
- Reverse pass: O(n) time, O(n) space - unnecessary

My approach is best.

---

### Duplicate Problem Interview

**Q: Explain your duplicate detection**

A: I iterate through the array with a set:
- If number is already in set → duplicate found
- If not in set → add it
- If I finish loop → no duplicates

Time: O(n) - one loop, set operations are O(1)
Space: O(n) - set stores numbers

---

**Q: What if I need to find ALL duplicates, not just yes/no?**

A: Same approach works:
```python
seen = set()
duplicates = []
for num in nums:
    if num in seen:
        duplicates.append(num)
    seen.add(num)
return duplicates
```

Still O(n) time.

---

**Q: Can you use less space?**

A: If array is limited range (like 0-100):
- Use boolean array instead of set
- Space: O(100) instead of O(n)
- Still O(1) lookup

But if array is large range, set is fine.

---

## 🔥 TRICKY QUESTIONS

**Q: What if array has millions of numbers?**

Stock: O(n) works fine
Duplicates: O(n) space might be concern
  - But need to check each, so can't avoid O(n)
  - Or use sorting approach: O(n log n) time, O(1) space

**Q: Negative prices in stock problem?**

A: Doesn't matter. Profit = price[j] - price[i]. Works with negatives.

**Q: What about floating point prices?**

A: Also works fine. No special handling needed.

---

## 💡 INTERVIEW STRATEGY

**When asked stock problem:**
1. State your approach first (min tracking)
2. Explain time/space
3. Show example walkthrough
4. Code it
5. Test with edge cases
6. Discuss optimizations

**Result:** Strong interview performance ✅