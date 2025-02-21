# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):  # abc
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """

    if len(sequence) == 1:
        return [sequence]

    first_char = sequence[0]  # b

    sub_permutation_list = get_permutations(sequence[1:])  # ["c"] => ["bc", "cb"]
    permutations = {}  # { bc, cb }

    for curr_str in sub_permutation_list:
        for i in range(len(curr_str) + 1):
            permutation = curr_str[0:i] + first_char + curr_str[i:]
            permutations[permutation] = True

    return list(permutations.keys())


def check_if_testcase_passed(actual_output, expected_output):
    if len(actual_output) != len(expected_output):
        return False

    expected_output_dict = {sequence: True for sequence in expected_output}
    actual_output_dict = {sequence: True for sequence in actual_output}

    for sequence in expected_output_dict:
        if sequence not in actual_output_dict:
            return False

    return True


if __name__ == "__main__":
    test_cases = [
        {
            "sequence": "abc",
            "expected_output": ["abc", "acb", "bac", "bca", "cab", "cba"],
        },
        {"sequence": "xy", "expected_output": ["xy", "yx"]},
        {"sequence": "aaa", "expected_output": ["aaa"]},
        {"sequence": "c", "expected_output": ["c"]},
        {"sequence": "bc", "expected_output": ["bc", "cb"]},
    ]

    for test_case in test_cases:
        sequence = test_case["sequence"]
        expected_output = test_case["expected_output"]
        actual_output = get_permutations(sequence)
        print("Sequence:", sequence)
        print("Expected Output:", expected_output)
        print("Actual Output:", actual_output)

        testcase_passed = check_if_testcase_passed(actual_output, expected_output)

        if testcase_passed:
            print("SUCCESS")
        else:
            print("FAILURE")
        print("---------------\n")
