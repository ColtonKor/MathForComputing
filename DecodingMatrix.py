import numpy as np
import math
from numpy.linalg import inv

message = input('Message to Decrypt: ')
message = message.lower()

if len(message)%4>0:
    message = message+(' '*(4-len(message)%4))

convertedmessage=[]
for character in message:
    if character == ' ':
        number=0
    else:
        number=ord(character)-96
    convertedmessage.append(number)

print("Encoded Message: %s" % convertedmessage)
E=np.reshape(convertedmessage, (4,-1), order='F')
print("Encoded Message Matrix: \n %s" % E)

A = np.matrix('2 1 3 1 ; -1 1 -2 0 ; 0 -2 1 1 ; 0 0 1 4')
print(A)
M = A*E
print("Matrix M=A*E :\n %s" % M)


MP = M%27
print("Encoded Matrix:\n %s" % MP)


print("Encoded Message:", end=" ")
MP = MP.T
num_rows, num_cols = MP.shape
for row in range(num_rows):
    for col in range(num_cols):
        print(chr(int(MP[row, col]) + 96), end="")


print("\nDecoded Message:", end=" ")
MP = MP.T
Inverse = np.linalg.inv(A)
Decode = np.dot(Inverse, MP)
Decode = Decode.T
Decode = Decode%27
num_rows, num_cols = Decode.shape
for row in range(num_rows):
    for col in range(num_cols):
        if(int(Decode[row, col]) + 96 == 96):
            print(" ", end="")
        else:
            print(chr(int(Decode[row, col]) + 96), end="")
Decode = Decode.T

newmessage = "VXMSPFDVATYMLZQSXXCRMCPGVJAYVIXSHFWQDITWQME WYKJHBRILJGDRJAY"
newmessage = newmessage.lower()

if len(newmessage)%4>0:
    newmessage = newmessage+(' '*(4-len(newmessage)%4))
print("\nEncoded Message: %s" % newmessage, end="")
print("\nDecoded Message: ", end="")
NewMessage=[]
for character in newmessage:
    if character == ' ':
        number=0
    else:
        number=ord(character)-96
    NewMessage.append(number)
Doctor=np.reshape(NewMessage, (4,-1), order='F')
Decode = np.dot(Inverse, Doctor)
num_rows, num_cols = Decode.shape
Decode = Decode.T
Decode = Decode%27
num_rows, num_cols = Decode.shape
for row in range(num_rows):
    for col in range(num_cols):
        if(int(Decode[row, col]) + 96 == 96):
            print(" ", end="")
        else:
            print(chr(int(Decode[row, col]) + 96), end="")
