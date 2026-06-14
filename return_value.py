# function with return

def safe_divide(a,b):
    if b == 0:
        return "cannot divide by 0"
    return a/b
print(safe_divide(1,0))
print(safe_divide(0,1))

# dunction can also return multiple value
#python puts them in a tuple

def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

scores = [65,32,76,90,54]
print(min_max_avg(scores))
low , high , avg = min_max_avg(scores)
print(f"Lowers: (low), Highest : (high), Avg : (avg)")

