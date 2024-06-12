def find_numbers_divisible_by_all(n, numbers):
    result = []
    for i in range(1, n + 1):
        if all(i % num == 0 for num in numbers):
            result.append(i)
    return result

n = int(input("Введіть значення n: "))
numbers = list(map(int, input("Введіть числа, розділені пробілом: ").split()))

divisible_numbers = find_numbers_divisible_by_all(n, numbers)
print(f"Числа, що не перевищують {n} і діляться на кожне із заданих чисел: {divisible_numbers}")