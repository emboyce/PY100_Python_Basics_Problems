# Demonstration of float('-inf') in Python

# Basic properties of negative infinity
neg_inf = float('-inf')
print("1. Basic Properties of float('-inf'):")
print(f"Value: {neg_inf}")
print(f"Type: {type(neg_inf)}")
print()

# Comparisons with other numbers
print("2. Comparisons:")
print(f"float('-inf') < -1000000:", neg_inf < -1000000)
print(f"float('-inf') < 0:", neg_inf < 0)
print(f"float('-inf') < float('inf'):", neg_inf < float('inf'))
print()

# Practical example 1: Finding maximum value in a list
def find_max(numbers):
    max_value = float('-inf')  # Initialize with smallest possible value
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

numbers = [-5, 12, -3, 8, 0]
print("3. Finding maximum value example:")
print(f"List: {numbers}")
print(f"Maximum value: {find_max(numbers)}")
print()

# Practical example 2: Window maximum in sliding window
def max_in_window(arr, k):
    if not arr or k <= 0:
        return []
    
    result = []
    window_max = float('-inf')
    
    # Process first window
    for i in range(k):
        window_max = max(window_max, arr[i])
    result.append(window_max)
    
    # Process remaining windows
    for i in range(k, len(arr)):
        window_max = float('-inf')
        for j in range(i-k+1, i+1):
            window_max = max(window_max, arr[j])
        result.append(window_max)
        
    return result

# Example of sliding window maximum
array = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3
print("4. Sliding Window Maximum example:")
print(f"Array: {array}")
print(f"Window size: {window_size}")
print(f"Maximum in each window: {max_in_window(array, window_size)}")
print()

# Mathematical operations
print("5. Mathematical operations with float('-inf'):")
print(f"float('-inf') + 100:", neg_inf + 100)
print(f"float('-inf') * -1:", neg_inf * -1)
print(f"min(float('-inf'), -999999):", min(neg_inf, -999999))

