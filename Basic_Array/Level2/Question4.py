## Find the last occurrence of a given number.
def last_occurrence(arr, x):
    inde = -1
    for i in range(len(arr)):
        if arr[i]==x:
            inde = i
    return f"The last occurrence of the element {x} is {inde}"

arr = [10,20,30,40,50,20]
x = 20
print(last_occurrence(arr, x))