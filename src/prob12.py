
def check(str1, str2):

    if len(str2) > len(str1):
        temp = str1
        str1 = str2
        str2 = temp


    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    list1 = []
    list2 = []
    for letter in str1:
        list1.append(letter)
    for letter in str2:
        list2.append(letter)

    #print(str1, " ||| ", str2)
    for letter in list1:
        if letter in str1 and letter in str2:
            place1 = str1.find(letter)
            del(list1[place1])

            place2 = str2.find(letter)
            del(list2[place2])

        else:
            return False

        str1 = ""
        str2 = ""
        for letter in list1:
            str1 += letter
        for letter in list2:
            str2 += letter

    #print(list1, list2)
    if len(str1) == len(str2):
        return True
    else:
        return False





numcases = int(input())
cases = []
for i in range(numcases):
    cases.append(input())

numnewcases = int(input())
newcases = []
for i in range(numnewcases):
    newcases.append(input())

cases = sorted(cases)



for newcase in newcases:
    yes = False
    matching = ""
    for case in cases:
        #print(case, newcase)
        if check(case, newcase) and not yes:
            yes = True
            matching = case

    if yes:
        print("Yes:", matching)
    else:
        print("No: No matching case")

