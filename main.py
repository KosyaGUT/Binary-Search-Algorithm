import time
start_time = time.time()  # время начала выполнения


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return f"Элемент {target} найден в позиции {mid}."
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return f"Элемент {target} не найден в списке."


# Пример использования
if __name__ == "__main__":
    # Создаем список от 1 до 100
    my_list = list(range(1, 101))

    # Пользователь вводит число для поиска
    user_input = int(input("Введите число для поиска: "))

    # Вызываем функцию двоичного поиска
    result = binary_search(my_list, user_input)

    # Выводим результат
    print(result)

end_time = time.time()  # время окончания выполнения
print(execution_time := end_time - start_time)  # вычисляем время выполнения