import math
a = int(input("X ekseni için bir değer giriniz:"))
c = int(input("X ekseni için ilk değerden büyük değer giriniz:"))
b = int(input("Y ekseni için bir değer giriniz:"))
d = int(input("Y ekseni için ilk değerden büyük değer giriniz:"))
# Noktaların Tanımlanması
points = [
    (a, b), # x1 ve y1 koordinatları
    (c, d) # x2 ve y2 koordinatları
]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    a, b = point1
    c, d = point2
    return math.sqrt((c - a)**2 + (d - b)**2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
