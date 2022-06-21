def get_ini_data() -> dict and float:
    """Returns initial math sets and number.
    Types of math sets:
        -inf                                                +inf
        *------------------------------------------------------*
        *-----------------------| |----------------------------*
        *--------------------------------------------|
                |----------------------------------------------*
        *------------|  |----------|
                  |--------------|      |----------------------*
        *------------|    |----|       |--|     |--------------*
                    |-------------------------------|
            |------|        |------|    |-|       |-------|
        All nine types are given in "all_sets"."""

    sets_1 = {'set_1': [[-10.3, 10.3], [18.7, '+inf']],
              'set_2': [['-inf', -8.2], [8.6, '+inf']],
              'set_3': [['-inf', -3.7]]}
    sets_2 = {'set_1': [['-inf', 10], [18, 26]],
              'set_2': [['-inf', -8], [8.1, 22]],
              'set_3': [['-inf', -3.74], [10, 30]]}
    sets_3 = {'set_1': [[-10, 10], [18, '+inf']],
              'set_2': [['-inf', -8], [8, '+inf']],
              'set_3': [['-inf', -3], [19, '+inf']]}
    sets_4 = {'set_1': [[-10, 10], [18, 22]],
              'set_2': [[-16, -8], [8, 40]],
              'set_3': [[-10, 23]]}
    sets_5 = {'set_1': [[-5, 16.08]],
              'set_2': [[16.02, 20]]}
    all_sets = {
        'type_1': [['-inf', '+inf']],
        'type_2': [['-inf', -10], [10, '+inf']],
        'type_3': [['-inf', 99]],
        'type_4': [[-98, '+inf']],
        'type_5': [['-inf', -32], [-17, 22]],
        'type_6': [['-inf', -41], [-18, 24], [51, 62], [103, '+inf']],
        'type_7': [[-89, -61], [-24, '+inf']],
        'type_8': [[-77, 61]],
        'type_9': [[-89, -61], [-43, -12], [10, 27], [61, 72]]
    }

    x_1 = 6
    x_2 = -16.51
    x_4 = 14
    x_5 = 16.06
    x_6 = -1

    return sets_2, -10
    # return sets_3, 5.5
    # return all_sets, -39


def format_sets(input_dict: dict) -> list and dict:
    """Returns list of all endpoints and dictionary with formatted sets:
    '-inf' changed to min value, '+inf' changed to max value."""
    all_ranges = set()

    for ranges in input_dict.values():
        add_data = [end_point
                    for sub_set in ranges
                    for end_point in sub_set
                    if not isinstance(end_point, str)]
        all_ranges.update(add_data)

    min_value = min(all_ranges)
    max_value = max(all_ranges)

    ini_sets = dict()

    for set_name, ranges in input_dict.items():
        temp_list = list()
        for sub_range in ranges:
            if sub_range == ['-inf', '+inf']:
                temp_list.append([min_value, max_value])
            elif sub_range[0] == '-inf':
                if sub_range[1] != min_value:
                    temp_list.append([min_value, sub_range[1]])
            elif sub_range[1] == '+inf':
                if sub_range[0] != max_value:
                    temp_list.append([sub_range[0], max_value])
            else:
                temp_list.append(sub_range)
        ini_sets[set_name] = temp_list

    return all_ranges, ini_sets


def get_ranges_for_check(input_list: set) -> list:
    """Converts endpoints list to list of ranges."""
    input_list = sorted(input_list)
    output_list = [[input_list[point - 1], input_list[point]]
                   for point in range(1, len(input_list))]
    return output_list


def check_ranges(ini_range: list, checking_range: list) -> list:
    """Checks two ranges for overlap."""
    intersection_ranges = list()
    for sub_set in ini_range:
        for sub_range in checking_range:
            if sub_set[0] <= sub_range[0] and sub_set[1] >= sub_range[1]:
                intersection_ranges.append(sub_range)
    return intersection_ranges


def common_inf_range(ini_dict: dict, intersection: list, min_value: int or float, max_value: int or float) -> list:
    """Checks initial math sets for the next conditions:
        if all sets start from '-inf', then range ['-inf', min_value] will be added to the intersection list;
        if all sets end with '+inf', then range [max_value, '+inf'] will be added to the intersection list."""
    if all(sub_set[0][0] == '-inf' for sub_set in ini_dict.values()):
        intersection.insert(0, ['-inf', min_value])
    if all(sub_set[-1][1] == '+inf' for sub_set in ini_dict.values()):
        intersection.append([max_value, '+inf'])
    return intersection


def print_result(intersection: list) -> None:
    """Displays intersection for input math sets."""
    if not intersection:
        print(f'\nThere is no intersection for input math sets')
    else:
        print(f'\nFor input math sets the subset intersection is {intersection}\n')


def compare_num_with_intersection(input_num: float, input_list: list) -> 'output':
    """Checks if given number belong to intersection of initial math sets,
    else returns the nearest range from intersection list and the nearest endpoints."""
    in_range = False
    for sub_range in input_list:
        if sub_range[0] == '-inf' and input_num <= sub_range[1]:
            in_range = True
            return True, sub_range, None, None
        elif sub_range[1] == '+inf' and input_num >= sub_range[0]:
            in_range = True
            return True, sub_range, None, None
        elif not isinstance(sub_range[0], str) and not isinstance(sub_range[1], str)\
                and input_num >= sub_range[0] and input_num <= sub_range[1]:
            # 'if B >= A and B <= C' is faster than 'if A <= B <= C'
            in_range = True
            return True, sub_range, None, None

    if not in_range:
        ini_num_endpoints, ini_num_range = clc_diff(input_num, input_list)
        return False, None, ini_num_endpoints, ini_num_range


def clc_diff(input_num: float, input_list: list) -> 'two lists':
    """Returns the list of the nearest endpoint(s) and the list of the nearest range(s) for given number."""
    diff_endpoints = list()
    diff_range = list()
    for sub_range in input_list:
        if sub_range[0] == '-inf':
            value_1 = sub_range[0]
            value_2 = abs(input_num - sub_range[1])
            diff_range.append(value_2)
        elif sub_range[1] == '+inf':
            value_1 = abs(input_num - sub_range[0])
            value_2 = sub_range[1]
            diff_range.append(value_1)
        else:
            value_1 = abs(input_num - sub_range[0])
            value_2 = abs(input_num - sub_range[1])
            diff_range.append(min([value_1, value_2]))
        diff_endpoints.append([value_1, value_2])

    nearest_endpoints = list()
    nearest_ranges = list()
    for cnt, element in enumerate(diff_range):
        if diff_range[cnt] == min(diff_range):
            nearest_ranges.append(input_list[cnt])
            if diff_endpoints[cnt][0] == min(diff_range):
                nearest_endpoints.append(input_list[cnt][0])
            else:
                nearest_endpoints.append(input_list[cnt][1])
    return nearest_endpoints, nearest_ranges


def main():
    """This script gets math sets and some number and outputs the intersection of the given sets
    and also checks if given number belongs to subrange of the intersection.
    The first step is to get all endpoints from given math sets and form sub ranges to determine the intersection.
    The second step is to check all ranges from minimum value to the maximum for belonging to all given subsets.
    The third step is to check the ranges from minus infinity to the minimum value
    and from maximum value to the plus infinity for belonging to all given subsets.
    And the forth step is to check if given number belongs to the intersection of the initial math sets,
    otherwise the nearest range(s) from the intersection and the nearest endpoint(s) are returned."""

    initial_sets, initial_num = get_ini_data()
    print(f'input data is:\n\tinitial_sets\n{initial_sets}\n\tinitial_num = {initial_num}\n')
    all_endpoints, all_ini_sets = format_sets(initial_sets)
    print(f'>> all endpoints are ({len(all_endpoints)}): {sorted(all_endpoints)}\n'
          f'>> edited initial math set looks like:\n{all_ini_sets}\n')
    intersection_set = get_ranges_for_check(all_endpoints)
    print(f'>> endpoints converted to ranges ({len(intersection_set)}): {intersection_set}\n')
    for set_range in all_ini_sets.values():
        intersection_set = check_ranges(set_range, intersection_set)
        print(f'all_ranges_list ({len(intersection_set)}):\t{intersection_set}')
    intersection_set = common_inf_range(initial_sets, intersection_set, min(all_endpoints), max(all_endpoints))
    print_result(intersection_set)
    status, num_in_range, num_endpoints, num_range = compare_num_with_intersection(initial_num, intersection_set)
    if status:
        print(f'TASK_1, TASK_2: The given number "{initial_num}" is in intersection range: {num_in_range}')
    else:
        print(f'TASK_1: The given number "{initial_num}" is out of intersection range,\n'
              f'the nearest endpoint(s) is(are): {num_endpoints}\n'
              f'TASK_2: The given number {initial_num} is out of intersection range, the nearest is(are): {num_range}')


if __name__ == '__main__':
    main()
