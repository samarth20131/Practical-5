data = input("Enter Message to Send : ") # 1100101010010110
k = int(input("Enter Number of Block : ")) # 4

sum =""
def findsum(data , k):
    d1 = data[0:k]
    d2 = data[k:2*k]
    d3 = data[2*k:3*k]
    d4 = data[3*k:4*k]

    temp = bin(int(d1,2) + int(d2,2) +int(d3,2) + int(d4,2))[2:]
    temp1 = temp[0:len(temp)-k]
    temp2 = temp[len(temp1):]
    sum = bin(int(temp1,2) + int(temp2,2))[2:]
    num = len(sum)
    final_sum = ""
    while(num<k):
        final_sum = "0" + sum
        num+=1
    print("sum : ", final_sum)
    return final_sum

def complement(sum):
    checksum=""
    for i in sum:
        if i == '1':
            checksum += "0"
        else :
            checksum += "1"
    return checksum

print("------------------- Sender Side -------------------")

sum = findsum(data,k)
scheckcum = complement(sum)
print("Checksum Sended : " ,scheckcum)

print("------------------- Receiver Side -------------------")

rsum = findsum(data,k)

rchecksum = bin(int(scheckcum,2)+int(rsum,2))[2:]

final_checksum = complement(rchecksum)
print("Result : ",final_checksum)

if(int(final_checksum,2)==0):
    print("Accept")
else:
    print("Resend")


