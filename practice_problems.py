"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

testLst1 = [10, 20, 30, 20, 40]
testLst2 = [1, 2, 3, 4, 5]

def has_duplicates(product_ids):
    temp_set = set(product_ids)

    if len(temp_set) < len(product_ids):
        return True
    else:
        return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskNode:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_task(self, task):
        new_task = TaskNode(task)
        if not self.front:
            self.front = new_task
            self.rear = new_task
        else:
            self.rear.next = new_task
            self.rear = new_task

    def remove_oldest_task(self):
        if not self.front:
            return None
        removed_task = self.front
        self.front = self.front.next

        if not self.front:
            self.rear = None
        
        return removed_task.task


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# Problem 1 Test Cases
assert has_duplicates(testLst1) == True
assert has_duplicates(testLst2) == False

# Problem 2 Test Case
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
assert task_queue.remove_oldest_task() == "Email follow-up"
assert task_queue.front.task == "Code review"

# Problem 3 Test Case
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
assert tracker.get_unique_count() == 2