## Count how many times a given element appears.
def count_element(arr, x):
    count = 0
    for element in arr:
        if element == x:
            count += 1
    return count

lst = [1,2,3,3,3,4,5,4,3,7,4]
x = 3
print(count_element(lst, x))