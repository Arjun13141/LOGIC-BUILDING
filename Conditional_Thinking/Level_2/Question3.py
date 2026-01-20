## 3. Take marks (0–100) and print the corresponding grade (A/B/C/D/F).
def grade(marks):
    if marks>=85:
        print("A")
    elif marks<85 and marks>=60:
        print("B")
    elif marks<60 and marks>=40:
        print("C")
    elif marks<40 and marks>=33:
        print("D")
    else:
        print("F")

grade(72)