# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 1. Rotate Right
# Rotate the values in a collection to the right by k steps.
# Input: [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate_right(numbers, rotate):
    return numbers[len(numbers) - rotate:] + numbers[:-rotate]

assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
print(rotate_right([1, 2, 3, 4, 5], 2))

# 2. Running Total with Reset
# Track a running total of values. If a negative number is added, reset the total to 0.
# Input: [5, 7, -1, 3, 2]
# Output: [5, 12, 0, 3, 5]

def running_with_reset(numbers):
    total = 0

    for i in range(len(numbers)):
        if numbers[i] >= 0:
            total += numbers[i]
            numbers[i] = total
        else:
            total = 0
            numbers[i] = total

    return numbers

assert running_with_reset([5, 7, -1, 3, 2]) == [5, 12, 0, 3, 5]
print(running_with_reset([5, 7, -1, 3, 2]))

# 3. Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]


def remove_dupes(values):
    values_set = set(values)
    no_dupes = list()

    for value in values:
        if value in values_set and value not in no_dupes:
            no_dupes.append(value)

    return no_dupes

assert remove_dupes(["apple", "banana", "apple", "kiwi", "banana"]) == ["apple", "banana", "kiwi"]
print(remove_dupes(["apple", "banana", "apple", "kiwi", "banana"]))

# 4. Remove Every k-th Value
# Remove every k-th value from a collection and return the result.
# Input: [10, 20, 30, 40, 50, 60], k = 3
# Output: [10, 20, 40, 50]

def remove_every_kth(values, kth):
    result = list()

    for i in range(len(values)):
        if (i + 1) % kth != 0:
            result.append(values[i])

    return result

assert remove_every_kth([10, 20, 30, 40, 50, 60], 3) == [10, 20, 40, 50]
print(remove_every_kth([10, 20, 30, 40, 50, 60], 3))