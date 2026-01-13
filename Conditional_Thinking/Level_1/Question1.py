## Phase 1 – Conditional Thinking (If–Else, Boolean Logic)
## Level 1: Simple Conditions (Getting started)

## 1. Take a number and print whether it’s positive, negative, or zero

def is_num_postive(num):
    if num == 0:
        return f"{num} is zero"
    elif num>0:
        return f"{num} is postitve number"
    else:
        return f"{num} is negetive number"

print(is_num_postive(45))