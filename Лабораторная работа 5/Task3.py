from random import randint


def get_unique_list_numbers() -> list[int]:
    size_of_list = 15
    random_list = [randint(-10, 10) for _ in range(size_of_list)]
    while len(random_list) != len(set(random_list)):
        random_list = [randint(-10, 10) for _ in range(size_of_list)]
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
