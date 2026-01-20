## 1. Take three sides and check if they form a valid triangle.
def is_triangle(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        print("It form a vaild triangle")
    else:
        print("It don't form a vaild trangle")

is_triangle(2,3,6)