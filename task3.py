def is_point_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Введіть координату a центру кола: "))
b = float(input("Введіть координату b центру кола: "))
R = float(input("Введіть радіус R кола: "))

points = [
    (float(input("Введіть координату р1 точки P: ")), float(input("Введіть координату р2 точки P: "))),
    (float(input("Введіть координату f1 точки F: ")), float(input("Введіть координату f2 точки F: "))),
    (float(input("Введіть координату l1 точки L: ")), float(input("Введіть координату l2 точки L: "))),
]

inside_count = sum(is_point_inside_circle(x, y, a, b, R) for x, y in points)

print(f"Кількість точок всередині кола: {inside_count}")