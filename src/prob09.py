inp = input()

while(inp != "0"):
    binary = bin(int(inp))[2:]
    ones = int(str(binary).count("1"))
    zeros = int(str(binary).count("0"))

    if ones> zeros:
        print(inp, "HEAVY")
    elif zeros> ones:
        print(inp, "LIGHT")
    elif ones== zeros:
        print(inp, "BALANCED")
    else:
        print("This shouldn't show up, but please pass us anyway :D ")

    inp = input()

#print(bin(int(input()))[2:])