## Take two angles of a triangle and compute the third angle.
def third_angle(a1,a2):
    if a1 <= 0 or a2 <=0 or a1+a2 >= 180:
        return "invaild angle, try again"
    return 180 - (a1+a2)

a1, a2 = 25 , 50
print(third_angle(a1, a2))