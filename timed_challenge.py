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

# What structure did I choose and why?

# I chose to stick with the structure that is used as the input, which is a list.
# I did this because it is easy to iterate through and also I can modify the given
# list in place and not have to create a second list. This helps with being more
# memory efficient as well. The alternative to this would be to create a second
# list and append the running total to that list instead. Although this would use
# more memory and be a bit slower, but the difference in this case is so small
# it is not an issue either way.

# How did the time limit shape my decision?

# The time limit had little to no effect on my decision of the data structure
# that I chose to solve the problem. This is because the most efficient data
# structure was already given to me in the form of the input parameter. If this
# were a more complex problem, the time limit would definitly affect my decision
# on which data structure I would choose as I would want the most efficient
# choice possible.

# What trade-offs or compromises did I make under time pressure?

# The only trade-off I made while solving this problem was modifying the given list
# in place and not creating a second list. This was done to help with the performance
# of the function. The preferred method with any function is to avoid modifying the
# input data, but can be done if needed and necessary.