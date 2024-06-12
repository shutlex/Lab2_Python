def calculate_quadrilateral_area(X, Y, Z, T):
    return 0.5 * X * Y + 0.5 * Z * T

X = float(input("Введіть довжину сторони X: "))
Y = float(input("Введіть довжину сторони Y: "))
Z = float(input("Введіть довжину сторони Z: "))
T = float(input("Введіть довжину сторони Т: "))

area = calculate_quadrilateral_area(X, Y, Z, T)
print(f"Площа чотирикутника: {area}")