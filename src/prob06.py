
def check(number):
    if int(number[0]) >= 2 and int(number[0]) <= 9:
        if int(number[1]) >= 0 and int(number[1]) <= 9:
            if int(number[2]) >= 0 and int(number[2]) <= 9:
                if int(number[3]) >=2 and int(number[3]) <=9:
                    if int(number[4]) >= 0 and int(number[4]) <=9:
                        if int(number[5]) >= 0 and int(number[5]) <=9:
                            if not(int(number[4]) == 1 and int(number[5]) == 1):
                                if int(number[6]) >= 0 and int(number[6]) <=9:
                                    if int(number[7]) >= 0 and int(number[7]) <=9:
                                        if int(number[8]) >= 0 and int(number[8]) <=9:
                                            if int(number[9]) >= 0 and int(number[9]) <=9:
                                                if not(int(number[1]) == 9):
                                                    return True
    return False


num = int(input())

for i in range(num):

    impoot = input()
    orig = impoot
    impoot = impoot.replace("(","")
    impoot = impoot.replace(")","")
    impoot = impoot.replace(" ","")
    impoot = impoot.replace("-","")
    impoot = impoot.replace(".","")

    result = check(impoot)

    if result:
        print(orig, "VALID")
    else:
        print(orig, "INVALID")