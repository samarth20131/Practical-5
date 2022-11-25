print("20012021007 Gupta Samarth Rajeshkumar")
print("Bit Stuffing and Unstuffing")

flag = list(input("Enter Flag : "))
data = list(input("Enter Data String : "))

no_of_1s = 0
for i in flag:
    if i == '1':
        no_of_1s += 1

ans1 = []
ans2 = []

def Stuffing(data, no_of_1s):
    count1 = 0
    for i in data:
        if i == '1':
            count1 += 1
            if count1 == no_of_1s - 1:
                ans1.append(i)
                ans1.append('0')
                count1 = 0
            else:
                ans1.append(i)
        else:
            ans1.append(i)
            count1 = 0
    str1 = "".join(ans1)
    print(str1)


def Unstuffing(ans1, no_of_1s):
    skip = -1
    count2 = 0
    for i in range(len(ans1)):
        if i != skip:
            if ans1[i] == '1':
                count2 += 1
                if count2 == no_of_1s - 1:
                    ans2.append('1')
                    skip = i + 1
                    count2 = 0
                else:
                    ans2.append('1')
            else:
                ans2.append('0')
                count2 = 0
    str2 = "".join(ans2)
    print(str2)


Stuffing(data, no_of_1s)
Unstuffing(ans1, no_of_1s)
