## 2. If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene
def classify_triangle(a,b,c):
    if a+b>c and b+c>a and c+a>b:

        if a==b==c:
            print("Equilateral Triangle")
        elif a==b or b==c or c==a:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")
    else:
        print("not a vaild triangle")

classify_triangle(6,6,10)