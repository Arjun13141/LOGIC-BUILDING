## 5. Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”.
def greeting(time):
    if time>=18 and time<4:
        print("Good Night")
    elif time>=4 and time<12:
        print("Good Morning")
    elif time>=12 and time<=16:
        print("Good Afternoon")
    elif time>=16 and time<18:
        print("Good Evening")
    elif time>=24:
        print("Enter a vaild time between 0-23")

greeting(4)