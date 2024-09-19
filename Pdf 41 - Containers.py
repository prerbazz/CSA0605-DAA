def max_loaded_weight(weights, max_capacity):
    weights.sort(reverse=True)
    total_weight = 0
    for weight in weights:
        if total_weight + weight <= max_capacity:
            total_weight += weight
        else:
            break
    return total_weight

# Test cases
print(max_loaded_weight([10, 20, 30, 40, 50], 60))  # Output: 50
print(max_loaded_weight([5, 10, 15, 20, 25, 30], 50))  # Output: 50
