import math



points = [(0, 0), (3, 4), (6, 8), (1, 1), (2, 2)]

def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

print("Noktalar arasındaki minimum mesafe:", min_distance)