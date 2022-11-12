list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_pos = 0
max_elem = list_numbers[0]
for pos, current_elem in enumerate(list_numbers):
    if current_elem > max_elem:
        max_elem = current_elem
        max_pos = pos

list_numbers[-1], list_numbers[max_pos] = max_elem, list_numbers[-1]

print(list_numbers)
