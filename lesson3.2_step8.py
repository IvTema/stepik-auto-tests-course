a = [int(i) for i in input().split()]
expected_result = a[0]
actual_result = a[1]
assert expected_result == actual_result, \
    f'expected {expected_result}, got {actual_result}'