'''
Think of time complexity as a way to measure how the execution time grows when the amount of data (n) increases.
Let's assume:
Pythonn = number of itemsShow more lines
For example:

Small list = 10 items
Medium list = 1,000 items
Large list = 1,000,000 items

The more slowly the execution time grows, the more efficient the algorithm is.

1. O(1) — Constant Time ✅ Most Efficient
Meaning
The operation always takes the same amount of time, regardless of the input size.
Example
Access an element in a list:
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
Python directly jumps to index 2.
Performance


List Size  Operations 
10              1
1000            1
1,000,000       1
No matter how big the list gets, only one operation is needed.
Real-Life Example
Finding a person's seat number in a theater when you already know the seat number.
Efficiency
⭐⭐⭐⭐⭐ Best

2. O(log n) — Logarithmic Time ✅ Very Efficient
Meaning
The data is repeatedly divided into halves.
Example
Binary Search
Sorted list:
[10,20,30,40,50,60,70,80]
Find 70:

Check middle (40)
Ignore left half
Check middle of right half (60)
Check next middle (70)

Found!
Performance


Items   Checks Needed
8       3
100     7
1,000   10
1,000,000 20
Even for one million items, only about 20 comparisons.
Real-Life Example
Searching a word in a dictionary.
You don't start from page 1—you open near the middle.
Efficiency
⭐⭐⭐⭐ Excellent

3. O(n) — Linear Time ✅ Good
Meaning
The algorithm checks items one by one.
Example
Linear Search
numbers = [10,20,30,40,50]
target = 50
The program may need to look at every element.
Performance
Items  Max Checks
10     10
100    100
1,000  1,000
1,000,000  1,000,000
As data doubles, work doubles.
Real-Life Example
Finding a student in an attendance register by reading names one at a time.
Efficiency
⭐⭐⭐ Good

4. O(n log n) — Efficient Sorting ✅ Industry Standard
Meaning
A combination of linear growth and logarithmic growth.
Example
Python's built-in:
numbers.sort()
or
sorted(numbers)
Internally Python uses a highly optimized algorithm called Timsort.
Performance
Items   Approximate Operations
100     664
1,000   9,966
10,000  132,877
The growth is much slower than O(n²).
Real-Life Example
Sorting millions of customer records in a database.
Efficiency
⭐⭐⭐⭐ Very Good

5. O(n²) — Quadratic Time ❌ Slow for Large Data
Meaning
Every item is compared with almost every other item.
Example
Bubble Sort
for i in range(n):    
    for j in range(n):        # compare items
        
Nested loops create quadratic growth.
Performance
Items   Operations
10      100
100     10,000
1,000   1,000,000
10,000  100,000,000
The number of operations explodes as data grows.
Real-Life Example
Every student in a class comparing marks with every other student.
Efficiency
⭐ Poor

Visual Comparison
Suppose we have 1,000,000 items:
Complexity   Approximate Operations
O(1)         1
O(log n)     20
O(n)         1,000,000
O(n log n)   20,000,000
O(n²)        1,000,000,000,000
Notice how huge the difference becomes for large datasets.

Easy Way to Remember
🏆 Best → Worst
Plain Text
O(1)   
↓
O(log n)   
↓
O(n)   
↓
O(n log n)   
↓
O(n²)
For searching:
Binary Search (O(log n))   better than
Linear Search (O(n))
For sorting:
Python sort() (O(n log n))   better than
Bubble Sort (O(n²))   better than
Selection Sort (O(n²))

Which complexity is most efficient?

O(1) – Best possible.
O(log n) – Very efficient for searching.
O(n) – Acceptable for many problems.
O(n log n) – Best practical complexity for sorting large data.
O(n²) – Avoid for large datasets because performance degrades quickly.

A simple thumb rule:

As the input size grows, algorithms with smaller complexity scale better and run faster.
'''