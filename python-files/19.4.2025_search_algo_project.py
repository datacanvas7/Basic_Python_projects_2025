# %% [markdown]
# # Binary Search Algorithm in Python

# %% [markdown]
# **Purpose**: Efficiently search for an element in a sorted list by repeatedly dividing the search interval in half.
# 
# **Key Features**\
# ✔ O(log n) time complexity (vs. O(n) for Linear Search)\
# ✔ Works only on sorted lists\
# ✔ Uses divide-and-conquer strategy

# %% [markdown]
# ## Code Implementation

# %% [markdown]
# ## 01- Binary Search Function

# %%
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2  # Find middle index
        if sorted_list[mid] == target:
            return mid  # Target found
        elif sorted_list[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Target not found

# %% [markdown]
# ## 02-Linear Search (For Comparison)
# 

# %%
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# %% [markdown]
# ## 03-Testing & Comparison
# ### Generate a Sorted List

# %%
import random

# Create a sorted list of 1000 random numbers
data = sorted(random.sample(range(1, 10000), 1000))
target = random.choice(data)  # Pick a random element to search
print(f"Target: {target}")

# %% [markdown]
# ### Run Both Algorithms

# %%
# Binary Search
binary_result = binary_search(data, target)
print(f"Binary Search: Found at index {binary_result}")

# Linear Search
linear_result = linear_search(data, target)
print(f"Linear Search: Found at index {linear_result}")

# %% [markdown]
# ## 04-Time Complexity Analysis

# %% [markdown]
# Algorithm	Time  - Complexity	- Best Case	 - Worst Case\
# Binary Search -	O(log n) -	O(1) - O(log n)\
# Linear Search -	O(n) -	O(1) -	O(n)\

# %% [markdown]
# ### Why Binary Search is Faster?
# Eliminates half the remaining elements in each step.
# 
# For a list of 1,000 elements, max steps:
# 
# Binary Search: ~10 steps (log₂1000 ≈ 10)
# 
# Linear Search: 1,000 steps (worst case).

# %% [markdown]
# ## 05-Visualizing Performance

# %%
import time
import matplotlib.pyplot as plt

# Measure execution time
def time_search(search_func, data, target):
    start = time.time()
    search_func(data, target)
    return time.time() - start

# Test on increasing data sizes
sizes = [100, 1000, 10000, 100000]
binary_times = []
linear_times = []

for size in sizes:
    data = sorted(random.sample(range(1, size * 10), size))
    target = random.choice(data)
    binary_times.append(time_search(binary_search, data, target))
    linear_times.append(time_search(linear_search, data, target))

# Plot results
plt.plot(sizes, binary_times, label='Binary Search')
plt.plot(sizes, linear_times, label='Linear Search')
plt.xlabel("List Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.title("Binary vs. Linear Search Performance")
plt.show()

# %% [markdown]
# ## 06-Key Takeaways

# %% [markdown]
# - Binary Search is faster but requires a sorted list.
# 
# - Linear Search is simpler but slower for large datasets.
# 
# - Real-world use cases:
# 
# - Searching in databases (indexed columns).
# 
# - Autocomplete suggestions (sorted words).
# 
# ---


