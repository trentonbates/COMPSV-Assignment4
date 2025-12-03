# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 2. Running Total with Reset
# Track a running total of values. If a negative number is added, reset the total to 0.
# Input: [5, 7, -1, 3, 2]
# Output: [5, 12, 0, 3, 5]

def running_with_reset(numbers):
    for number in numbers:
        if not isinstance(number, int):
            return "Input list needs to be numbers."

    if len(numbers) == 0:
        return "List is empty."
    elif len(numbers) == 1 and numbers[0] >= 0:
        return numbers
    else:
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
assert running_with_reset([5, 'a', -1, 3, 2]) == "Input list needs to be numbers."
assert running_with_reset(list()) == "List is empty."
assert running_with_reset([5]) == [5]
assert running_with_reset([-5]) == [0]