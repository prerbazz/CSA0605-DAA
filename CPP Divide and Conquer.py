def closest_pair_of_points(points):
    def squared_distance(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def merge_and_find(points_sorted_by_y, delta_squared):
        min_dist_squared = delta_squared
        num_points = len(points_sorted_by_y)
        
        for i in range(num_points):
            for j in range(i + 1, min(i + 8, num_points)):
                dist_squared = squared_distance(points_sorted_by_y[i], points_sorted_by_y[j])
                if dist_squared < min_dist_squared:
                    min_dist_squared = dist_squared
        
        return min_dist_squared

    def divide_and_conquer(points_sorted_by_x, points_sorted_by_y):
        num_points = len(points_sorted_by_x)
        if num_points <= 3:
            min_dist_squared = float('inf')
            for i in range(num_points):
                for j in range(i + 1, num_points):
                    dist_squared = squared_distance(points_sorted_by_x[i], points_sorted_by_x[j])
                    if dist_squared < min_dist_squared:
                        min_dist_squared = dist_squared
            return min_dist_squared

        mid = num_points // 2
        midpoint = points_sorted_by_x[mid]

        left_y = [p for p in points_sorted_by_y if p[0] <= midpoint[0]]
        right_y = [p for p in points_sorted_by_y if p[0] > midpoint[0]]

        delta_left_squared = divide_and_conquer(points_sorted_by_x[:mid], left_y)
        delta_right_squared = divide_and_conquer(points_sorted_by_x[mid:], right_y)
        delta_squared = min(delta_left_squared, delta_right_squared)

        strip = [p for p in points_sorted_by_y if abs(p[0] - midpoint[0]) ** 2 < delta_squared]
        min_dist_squared = merge_and_find(strip, delta_squared)

        return min_dist_squared

    points_sorted_by_x = sorted(points, key=lambda p: p[0])
    points_sorted_by_y = sorted(points, key=lambda p: p[1])

    min_dist_squared = divide_and_conquer(points_sorted_by_x, points_sorted_by_y)
    return min_dist_squared ** 0.5  # Return the actual distance by taking the square root


points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (7, 7)]

result = closest_pair_of_points(points)
print(f"The closest pair distance is {result:.6f}")
