"""Checkpoint 3 test code with intentional issues."""

def unsafe_eval(user_input):
    # CRITICAL SECURITY ISSUE: Code injection / unsafe eval
    return eval(user_input)

def calculate_total(prices):
    # Performance issue: bare exception / inefficient loop
    try:
        total = 0
        for p in prices:
            total += p
        return total
    except:
        return 0
