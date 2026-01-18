# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    # Guard against empty input or non-list types
    if not values or not isinstance(values, list):
        return 0.0

    valid_numbers = []
    for v in values:
        if v is not None:
            try:
                valid_numbers.append(float(v))
            except (ValueError, TypeError):
                continue

    if not valid_numbers:
        return 0.0

    return sum(valid_numbers) / len(valid_numbers)