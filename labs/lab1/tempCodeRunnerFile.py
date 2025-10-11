def draw_diamond():
### START OF GABBY'S CODE PT. I
    while True:
        try:
            height = int(input("Enter an odd number: "))
            if height % 2 == 1:
                break
            else:
                print("Error must enter an odd value, retry: ")
        except ValueError:
            print("Refer to directions and please try again")
    middle = height // 2
    for idx in range (middle, -1, -1):
        before = " " * idx
        between = " " * ((middle - idx) * 2 - 1)
        if (middle - idx) * 2 - 1 == -1:
            print(before + "*")
        else:
            print(before + "*" + between + "*")
    for idx in range (1, middle + 1):
        before = " " * idx
        between = " " * ((middle - idx) * 2 -1)
        if (middle - idx) * 2 -1 == -1:
            print(before + "*")
        else:
            print(before + "*" + between + "*")

draw_diamond()