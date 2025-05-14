# Introduction
![GitHub License](https://img.shields.io/github/license/LesBoys43/TimeLimitPro?style=plastic) ![GitHub branch status](https://img.shields.io/github/checks-status/LesBoys43/TimeLimitPro/master?style=plastic)  
A simple Python task time-limiting tool for easily setting maximum execution durations for complex tasks.

# Usage
## Basic Usage
```python
# First, initialize a TimeLimit object with the maximum duration (in milliseconds)
limit = TimeLimit(1000)  # 1 second
# Use a with statement to limit task execution time
with limit:
    try:
        # Insert checkpoints within the task
        limit.checkpoint()  # Does not trigger
    except TimeoutError:
        print("Task timed out!")
        # Handle timeout logic here
    # Write time-sensitive code here
    time.sleep(1.5)  # Simulate time-consuming operation
    try:
        # Insert checkpoints
        limit.checkpoint()  # Triggers
    except TimeoutError:
        print("Task timed out!")
        # Handle timeout logic here
```

## Custom Handlers
```python
# Define a custom handler
def custom_handler():
    print("Task timed out!")
    # Handle timeout logic here

# Initialize a TimeLimit object with maximum duration and custom handler
limit = TimeLimit(1000)  # 1 second
limit.set_custom_handler(custom_handler)  # Set custom handler after initialization

# Use a with statement to limit task execution time
with limit:
    # Insert checkpoints
    limit.checkpoint()  # Does not trigger
    # Write time-sensitive code here
    time.sleep(1.5)  # Simulate time-consuming operation
    limit.checkpoint()  # Triggers
```
