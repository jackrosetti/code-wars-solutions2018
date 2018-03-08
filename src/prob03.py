num = int(input("Gimme a num! "))
num1 = 0
list = []
for(i in range (num)):
    list.__add__(i)

def isPrime(yes):
    for i in range(yes, 1, 1):
        if(yes % i == 0 and (i != 0 or i != yes)):
            print("no")
            return False
    print('yes')
    return True

while(num != 0):
    for i in range(num):
        if(not(isPrime(num[i]))):
            print("Petty")
        num1 += num[i]


