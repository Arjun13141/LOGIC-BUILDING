## Take coordinates (x, y) and determine which quadrant the point lies in
def check_quadrant(x,y):
    if x>0 and y>0:
        return "coordinates of first Quadrant"
    elif x<0 and y>0:
        return "Coordinate of second Quadrant"
    elif x<0 and y<0:
        return "coordinate of third Quadrant"
    elif x>0 and y<0:
        return "coordinate of Forth Quadrant"
    elif x==0 and y==0:
        return "Point lies at the Origin"
    elif x == 0:
        return "Point lies on the Y-axis"
    elif y == 0:
        return "Point lies on the X-axis"

x = int(input("enter X-coordinate: "))
y = int(input("enter Y-coordinate: "))
print(check_quadrant(x,y))