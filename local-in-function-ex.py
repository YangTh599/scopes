y = 10

print(f"GLOBAL Y: {y}") # USES GLOBAL Y

def func_1():
    y = 20
    print(f"LOCAL Y: {y}") # USES LOCAL Y

func_1()

print(y) # USES GLOBAL Y