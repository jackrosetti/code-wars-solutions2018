inpoot = input()

while(inpoot != "0 0 0"):
    inpoot = inpoot.split(" ")
    v = float(inpoot[0])
    q = float(inpoot[1])
    t = float(inpoot[2])


    dist = v*t
    dist += .5 * (q*t**2)

    print(dist)

    inpoot = input()

