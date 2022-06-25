def format_sets(ini_math_sets: list) -> set and list:
    """Returns set of all unique endpoints and list with formatted math sets:
    '-inf' changed to min endpoint, '+inf' changed to max endpoint."""
    all_endpoints = [end_point
                     for sets_list in ini_math_sets
                     for sub_set in sets_list
                     for end_point in sub_set
                     if not isinstance(end_point, str)]

    all_endpoints = set(all_endpoints)

    min_value = min(all_endpoints)
    max_value = max(all_endpoints)

    sub_sets_formatted = list()

    for ranges in ini_math_sets:
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
        sub_sets_formatted.append(temp_list)

    return all_endpoints, sub_sets_formatted


def get_ranges_for_check(input_data: set) -> list:
    """Converts endpoints set to list of ranges."""
    input_data = sorted(input_data)
    output_list = [[input_data[point - 1], input_data[point]]
                   for point in range(1, len(input_data))]
    return output_list


def check_ranges(ini_range: list, checking_range: list) -> list:
    """Checks if the intersection sub range belongs to initial math sets."""
    intersection_ranges = [checking_sub_range
                           for ini_sub_set in ini_range
                           for checking_sub_range in checking_range
                           if ini_sub_set[0] <= checking_sub_range[0] and ini_sub_set[1] >= checking_sub_range[1]]

    return intersection_ranges


def common_inf_range(ini_sets: list, intersection: list, min_value: int or float, max_value: int or float) -> list:
    """Checks initial given math sets for the next cases:
        if all sets start from '-inf', then range ['-inf', min_value] will be added to the intersection list;
        if all sets end with '+inf', then range [max_value, '+inf'] will be added to the intersection list."""
    if all(sub_set[0][0] == '-inf' for sub_set in ini_sets):
        intersection.insert(0, ['-inf', min_value])
    if all(sub_set[-1][1] == '+inf' for sub_set in ini_sets):
        intersection.append([max_value, '+inf'])

    return intersection


def compare_num_with_intersection(input_num: float, input_list: list) -> 'output data':
    """Checks if given number belongs to intersection of initial math sets,
    else returns the nearest range(s) from intersection list and the nearest endpoint(s)."""
    for sub_range in input_list:
        if sub_range[0] == '-inf':
            if input_num <= sub_range[1]:
                return True, sub_range, None, None
        elif sub_range[1] == '+inf':
            if input_num >= sub_range[0]:
                return True, sub_range, None, None
        elif input_num >= sub_range[0] and input_num <= sub_range[1]:
            return True, sub_range, None, None

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


def main(ini_sub_sets: list, initial_num: float or int) -> None:
    """This script gets math sets and some number,
    then the intersection of the given math sets is defined.
    and also checks if given number belongs to subrange of the intersection.
    The first step is to get all endpoints from given math sets and form sub ranges to determine the intersection.
    The second step is to check all sub ranges from minimum value to the maximum for belonging to all given subsets.
    The third step is to check the ranges from minus infinity to the minimum value
    and from maximum value to the plus infinity for belonging to all initial math subsets.
    And the forth step is to check if given number belongs to the intersection of the initial math sets,
    otherwise the nearest range(s) from the intersection and the nearest endpoint(s) are returned."""

    all_ini_endpoints, all_ini_sets = format_sets(ini_sub_sets)
    sub_ranges_to_check = get_ranges_for_check(all_ini_endpoints)
    for subset in all_ini_sets:
        sub_ranges_to_check = check_ranges(subset, sub_ranges_to_check)
    intersection_set = common_inf_range(ini_sub_sets, sub_ranges_to_check,
                                        min(all_ini_endpoints), max(all_ini_endpoints))
    in_range, num_in_range, nearest_num_endpoints, nearest_num_range = compare_num_with_intersection(initial_num,
                                                                                                     intersection_set)
    if in_range:
        print(f'\tTASK_1, TASK_2: The given number "{initial_num}" is in intersection range: {num_in_range}')
    else:
        print(f'\tTASK_1: The given number "{initial_num}" is out of intersection range,\n'
              f'\tthe nearest endpoint(s) is(are): {nearest_num_endpoints}\n\n'
              f'\tTASK_2: The given number "{initial_num}" is out of intersection range,\n'
              f'\tthe nearest is(are): {nearest_num_range}')


if __name__ == '__main__':
    all_math_sets = {
        'set_type_1': [['-inf', '+inf']],
        'set_type_2': [['-inf', -10], [10, '+inf']],
        'set_type_3': [['-inf', 99]],
        'set_type_4': [[-98, '+inf']],
        'set_type_5': [['-inf', -32], [-17, 22]],
        'set_type_6': [['-inf', -41], [-18, 24], [51, 62], [103, '+inf']],
        'set_type_7': [[-89, -61], [-24, '+inf']],
        'set_type_8': [[-77, 61]],
        'set_type_9': [[-89, -61], [-43, -12], [10, 27], [61, 72]]
    }
    for cnt, input_number in enumerate([-83, -75, -39, -14, -1, 18, 31], 1):
        print(f'\nCase {cnt}: all types of math sets are given, number is equal to {input_number}\n')
        main(list(all_math_sets.values()), input_number)
