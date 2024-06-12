def calculate_area(width, height):
    return width * height

rectangles = []

for i in range(3):
    width = float(input(f"Введіть ширину прямокутника {i+1}: "))
    height = float(input(f"Введіть висоту прямокутника {i+1}: "))
    area = calculate_area(width, height)
    rectangles.append(area)
    print(f"Площа прямокутника {i+1}: {area}")