import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as inp_file:
        list_of_headers = inp_file.readline().split(',')

        list_of_list_row = []
        number_of_rows_without_header = 0
        for line in inp_file:
            list_of_list_row.append(line.split(','))
            number_of_rows_without_header += 1

        end_list = []
        for row in range(number_of_rows_without_header):
            end_list.append({list_of_headers[column].rstrip(): list_of_list_row[row][column].rstrip() for column in range(len(list_of_headers))})

    return end_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
