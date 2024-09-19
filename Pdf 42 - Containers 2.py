def min_containers(weights, max_capacity):
    weights.sort(reverse=True)
    containers = 0
    while weights:
        current_capacity = max_capacity
        i = 0
        while i < len(weights):
            if weights[i] <= current_capacity:
                current_capacity -= weights[i]
                weights.pop(i)
            else:
                i += 1
        containers += 1
    return containers

# Test cases
print(min_containers([5, 10, 15, 20, 25, 30, 35], 50))  # Output: 4
print(min_containers([10, 20, 30, 40, 50, 60, 70, 80], 10))  # Output: 6
