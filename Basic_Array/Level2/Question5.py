## Check if all elements in an array are unique
def all_unique(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return False
        seen.add(i)
    return True

arr = [10, 20, 30, 40, 50]
print(all_unique(arr))