
num = int(input())

for i in range(num):
    impoot = input()
    impoot = impoot.split(" ")

    gold = int(impoot[0])
    silver = int(impoot[1])
    bronze = int(impoot[2])

    while bronze > 6:
        silver += 1
        bronze -= 5

    while silver > 11:
        gold += 1
        silver -= 10






    print(gold,silver,bronze)

