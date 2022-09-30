width=int(input("Enter the width"))
height=int(input("Enter the height"))
coverage=5

def paint_calc(widht,height,coverage):
    cans=(width*height)/coverage
    print(f"Number of cans are {round(cans)}")


paint_calc(width,height,coverage)