n1 = int(input("Enter n1"))
n2 = int(input("Enter n2"))
L1 = int(input("Enter L1"))
L2 = int(input("Enter L2"))
L3 = int(input("Enter L3"))
H = int(input("Enter H"))
redius = int(input("Enter redius"))


while True:
    selection = int(input("1. add/n"
                          "2. subtract/n"
                          "3. multiplication/n"
                          "4. division/n"
                          "5. Area triangle"
                          "6. Area circle"
                          "7. Area rectangle"
                          "8. Exit"))
    while True:
        if selection <=0:
            break
        else:
            selection = int(input("Invalid Input , Enter Valid selection"))

    if selection == 1:
        add = n1 + n2
        print(add(n1,n2))
    elif selection == 2:
        sub = n1 * n2
        print(sub(n1, n2))
    elif selection == 3:
         multi = n1 * n2
         print(multi(n1, n2))
    elif selection == 4:
        divi = n1 / n2
        print(divi(n1, n2))
    elif selection == 5:
        Area_triangle = 0.5 * L1 * H
        print(Area_triangle(L1,H))
    elif selection == 6:
        Area_circle = 3.14 * (redius ** 2)
        print(Area_circle(redius))
    elif selection == 7:
        Area_rectangle = L1 * L2
        print(Area_rectangle(L1,L2))
    elif selection == 8:
        exit()