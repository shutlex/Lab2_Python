import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

cathetus1 = (float(input("Введіть перший катет трикутника 1: ")), float(input("Введіть другий катет трикутника 1: ")))
cathetus2 = (float(input("Введіть перший катет трикутника 2: ")), float(input("Введіть другий катет трикутника 2: ")))

hypotenuse1 = calculate_hypotenuse(*cathetus1)
hypotenuse2 = calculate_hypotenuse(*cathetus2)

print(f"Гіпотенуза трикутника 1: {hypotenuse1}")
print(f"Гіпотенуза трикутника 2: {hypotenuse2}")

if hypotenuse1 > hypotenuse2:
    print("Гіпотенуза трикутника 1 більша.")
elif hypotenuse1 < hypotenuse2:
    print("Гіпотенуза трикутника 2 більша.")
else:
    print("Гіпотенузи трикутників рівні.")