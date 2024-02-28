print("20012021007 Gupta Samarth Rajeshkumar")
print("Byte Stuffing and Unstuffing")

list1 = []
list2 = []

flag = input("Enter Flag : ")
esc = input("Enter ESC character : ")
while(esc==flag):
    print("Enter the value of Esc Character other than flag")
    esc = input("Enter ESC character : ")

msg = input("Enter your message : ")

def stuffing(msg):
    list1.append(flag)
    for i in msg:
        if i == flag:
            list1.append(esc)
            list1.append(i)
        elif i == esc:
            list1.append(esc)
            list1.append(i)
        else:
            list1.append(i)
    list1.append(flag)

    str1 = "".join(list1)
    return (str1)


def unstuffing(list1, esc):
    list2 = []

    del list1[0], list1[len(list1) - 1]
    p = -1
    for i in range(len(list1)):
        if list1[i] == esc:
            if i == p:
                list2.append(list1[i])
            else:
                p = i + 1
        else:
            list2.append(list1[i])
    str2 = "".join(list2)
    return (str2)


print(f"Stuffed Data : {stuffing(msg)}")
print(f"unstuffed Data : {unstuffing(list1, esc)}")
print("hello World")



