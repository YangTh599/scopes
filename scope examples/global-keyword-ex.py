x = 10

print(f"Before: {x}")

def change_x():
    global x

    x *= 11

change_x()

print(f"After by using change_x function: {x}")