nums = input()
while nums != "0":

    list = []
    nums = nums.split(" ")

    numofnums = int(nums[0])

    for i in range(1, numofnums+1):
        list.append(int(nums[i]))
    list.sort()
    list.reverse()

    num = list[0]
    num1 = list[1]
    num2 = list[2]

    numN1 = list[-1]
    numN2 = list[-2]
    if numN1 < 0 and numN2 < 0:
        if numN1 * numN2 > num1 * num2:
            product = num * numN1 * numN2
        else:
            product = num * num1 * num2
    else:
        product = num * num1 * num2

    print(product)

    nums = input()

