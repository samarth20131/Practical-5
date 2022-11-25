def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def binary_division(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]
    while pick < len(divident):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]
        else:
            tmp = xor('0'*pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    checkword = tmp
    return checkword

def encodeData(data, key):
    l_key = len(key)
    send_data = data + '0'*(l_key-1)
    rem = binary_division(send_data, key)
    codeword = data + rem
    return codeword
def decodeData(receivedData, key):
    l_key = len(key)
    receive_data = receivedData + '0'*(l_key-1)
    remainder = binary_division(receive_data, key)
    return remainder

data = input("Enter the dataword : ")
divisor = input("Enter the value of divisor : ")
answer = encodeData(data, divisor)
print("------------------- Sender Side -------------------")
print("Remainder after encoding is: ", answer)
print("------------------- Receiver Side -------------------")
print(f"Received data is : {answer}")
receivedData=answer
remainder = decodeData(receivedData, divisor)
if remainder == '0'*(len(divisor) - 1):
    print("Received data is correct")
else:
    print("Received data is incorrect")