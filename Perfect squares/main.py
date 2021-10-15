""" give me a number and i will return to you the least number of perfect square number
that sum to the number and also i will give you the list of that squares """

# get the number
GIVEN_NUMBER = int(input("enter a number: "))


def find_start_point(number: int):
    half = int(number/2)
    while half**2 > GIVEN_NUMBER:
        half = int(half/2)
    return half


def start_calculation():
    start_point = find_start_point(GIVEN_NUMBER)
    start_point_square = start_point**2
    multiple = 1
    check = True
    total_list = []
    while check:
        if multiple*start_point_square < GIVEN_NUMBER:
            total_list.append(start_point_square)
            multiple += 1

        elif multiple*start_point_square == GIVEN_NUMBER:
            total_list.append(start_point_square)
            final_num = multiple * start_point_square
            return [final_num, total_list, start_point]

        else:
            final_num = multiple * start_point_square - start_point_square
            del total_list[0]
            return [final_num, total_list, start_point]


def end():
    data_list = start_calculation()
    final_num = data_list[0]
    total_list = data_list[1]
    start_point = data_list[2]

    start_point += 1
