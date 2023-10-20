# points are given in the ascending order.
# outputs: the minimum number of segments of length at most 2 needed to cever all the points

def PointsCoverSorted(points):
    segments = []
    left = 1
    while left < len(points):
        segments.append([points[left - 1], points[left]])
        left += 1
        while left < len(points) and points[left] <= segments[-1][1]:
            left += 1
    return segments


# Example usage:
points = [1, 3, 4, 5, 7, 9, 10, 11, 12, 13]
print(PointsCoverSorted(points))
