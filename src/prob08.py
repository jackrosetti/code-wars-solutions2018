

inp = input().split(" ")

while inp != "0 0":

    start = int(inp[0])
    target = int(inp[1])

    serial = ""
    currentnum = start

    while len(serial) < target:
        serial += str(currentnum)
        currentnum += 1

    print(start, target, currentnum-2)
    inp = input().split(" ")

