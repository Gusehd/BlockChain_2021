#19101185 강동현 - 3011 SHA-256 Tutorial

string = input()

#step 1
bn = ' '.join(map(bin, bytearray(string, "utf-8")))
bn = bn.replace("0b","0").replace("0100000","00100000")
# 이진수 변환시 앞쪽의 수의 크기가 작을시 자릿수를 채우지 못하는 것을 보정
# replace로 보정하였지만 , 아래서 처럼 길이가 모자란 만큼 앞쪽에 0을 붙여주는 것으로도 해결가능
# 여기서는 hello world 한 경우에 대해서 살펴보는 것이므로 replace 로 바꾸어 주었음
# 다른 문자열에 대해서도 하려면 코드 아래쪽 처럼 len으로 길이 체크후 부족한 만큼 ("0" * n)+ 문자열 로 해결가능
bn = bn + " 10000000"

for _ in range(51):
    bn = bn + " 00000000"
bn = bn + " 01011000"

#step 2
h0 = "0x6a09e667"
h1 = "0xbb67ae85"
h2 = "0x3c6ef372"
h3 = "0xa54ff53a"
h4 = "0x510e527f"
h5 = "0x9b05688c"
h6 = "0x1f83d9ab"
h7 = "0x5be0cd19"

#step 3
k = [
"0x428a2f98", "0x71374491", "0xb5c0fbcf", "0xe9b5dba5", "0x3956c25b", "0x59f111f1", "0x923f82a4", "0xab1c5ed5",
"0xd807aa98", "0x12835b01", "0x243185be", "0x550c7dc3", "0x72be5d74", "0x80deb1fe", "0x9bdc06a7", "0xc19bf174",
"0xe49b69c1", "0xefbe4786", "0x0fc19dc6", "0x240ca1cc", "0x2de92c6f", "0x4a7484aa", "0x5cb0a9dc", "0x76f988da",
"0x983e5152", "0xa831c66d", "0xb00327c8", "0xbf597fc7", "0xc6e00bf3", "0xd5a79147", "0x06ca6351", "0x14292967",
"0x27b70a85", "0x2e1b2138", "0x4d2c6dfc", "0x53380d13", "0x650a7354", "0x766a0abb", "0x81c2c92e", "0x92722c85",
"0xa2bfe8a1", "0xa81a664b", "0xc24b8b70", "0xc76c51a3", "0xd192e819", "0xd6990624", "0xf40e3585", "0x106aa070",
"0x19a4c116", "0x1e376c08", "0x2748774c", "0x34b0bcb5", "0x391c0cb3", "0x4ed8aa4a", "0x5b9cca4f", "0x682e6ff3",
"0x748f82ee", "0x78a5636f", "0x84c87814", "0x8cc70208", "0x90befffa", "0xa4506ceb", "0xbef9a3f7", "0xc67178f2"]

#step 4
#Chunk Loop "hello world" is too short , we only have one chunk

#step 5
w = []
sub_stack = list(bn.split(" "))
for i in range(0,16):
    ans = ""
    for t in range(0,4):
        n = sub_stack.pop(0)
        ans += n
    w.append(ans)
for t in range(0,48):
    w.append('00000000000000000000000000000000')

def right(string,times):
    sub_string = string[32-times:32]
    sub_string2 = sub_string + string[0:32-times]
    return sub_string2

def xor(str11 , str22):
    ans = ""
    str1 = list(str11)
    str2 = list(str22)
    for i in range(0,32):
        if str1[i] == "0" and str2[i] == "0":
           ans += "0"
        elif str1[i] == "0" and str2[i] == "1":
           ans += "1"
        elif str1[i] == "1" and str2[i] == "0":
           ans += "1"
        elif str1[i] == "1" and str2[i] == "1":
           ans += "0"
    return ans

def shift(string,times):
    if times == 3:
        return ("000" + string[0:29])
    else:
        return ("0000000000" + string[0:22])

for i in range(16,64):
    s0 = xor(xor(right(w[i-15],7),right(w[i-15],18)) ,shift(w[i-15],3))
    s1 = xor(xor(right(w[i-2],17),right(w[i-2],19)) ,shift(w[i-2],10))
    aa = (int(("0b"+w[i-16]),2) + int(("0b"+s0),2) + int(("0b"+w[i-7]),2) + int(("0b"+s1),2)) % (2**32)
    bb = bin(aa).replace("0b","")
    if len(bb) < 32:
        bb = ((32 - len(bb)) * "0") + bb
    w[i] = bb

#step 6
#h0 ~ h7 16진수 -> 2진수
a = "01101010000010011110011001100111"
b = "10111011011001111010111010000101"
c = "00111100011011101111001101110010"
d = "10100101010011111111010100111010"
e = "01010001000011100101001001111111"
f = "10011011000001010110100010001100"
g = "00011111100000111101100110101011"
h = "01011011111000001100110100011001"

def and_b(str1,str2):
    ans = ""
    for i in range(0,32):
        if str1[i] == "0" and str2[i] == "0":
            ans += "0"
        elif str1[i] == "0" and str2[i] == "1":
            ans += "0"
        elif str1[i] == "1" and str2[i] == "0":
            ans += "0"
        elif str1[i] == "1" and str2[i] == "1":
            ans += "1"
    return ans

def not_b(str1):
    ans = ""
    for i in range(0,32):
        if str1[i] == "0":
            ans += "1"
        elif str1[i] == "1":
            ans += "0"
    return ans

for i in range(0,64):
    s1 = xor(xor(right(e,6),right(e,11)),right(e,25))
    ch = xor(and_b(e,f),and_b(not_b(e),g))

    aa = (int(("0b" + h), 2) + int(("0b" + s1), 2) + int(("0b" + ch), 2) + int(k[i], 16) + int(("0b" + w[i]), 2)) % (2**32)
    bb = bin(aa).replace("0b", "")
    if len(bb) < 32:
        bb = ((32 - len(bb)) * "0") + bb
    temp1 = bb

    s0 = xor(xor(right(a,2),right(a,13)),right(a,22))
    maj = xor(xor(and_b(a,b),and_b(a,c)),and_b(b,c))

    aa = (int(("0b" + s0), 2) + int(("0b" + maj), 2)) % (2 ** 32)
    bb = bin(aa).replace("0b", "")
    if len(bb) < 32:
        bb = ((32 - len(bb)) * "0") + bb
    temp2 = bb

    h = g
    g = f
    f = e

    aa = (int(("0b" + d), 2) + int(("0b" + temp1), 2)) % (2 ** 32)
    bb = bin(aa).replace("0b", "")
    if len(bb) < 32:
        bb = ((32 - len(bb)) * "0") + bb
    e = bb

    d = c
    c = b
    b = a

    aa = (int(("0b" + temp1), 2) + int(("0b" + temp2), 2)) % (2 ** 32)
    bb = bin(aa).replace("0b", "")
    if len(bb) < 32:
        bb = ((32 - len(bb)) * "0") + bb
    a = bb

real_ans = ""

aa0 = (int(h0,16) + int(("0b"+ a),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h0 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h0

aa0 = (int(h1,16) + int(("0b"+ b),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h1 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h1

aa0 = (int(h2,16) + int(("0b"+ c),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h2 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h2

aa0 = (int(h3,16) + int(("0b"+ d),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h3 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h3

aa0 = (int(h4,16) + int(("0b"+ e),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h4 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h4

aa0 = (int(h5,16) + int(("0b"+ f),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h5 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h5

aa0 = (int(h6,16) + int(("0b"+ g),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h6 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h6

aa0 = (int(h7,16) + int(("0b"+ h),2)) % (2**32)
bb0 = bin(aa0).replace("0b", "")
if len(bb0) < 32:
    bb0 = ((32 - len(bb0)) * "0") + bb0
h7 = hex(int("0b" + bb0,2)).replace("0x","")
real_ans += h7

print(real_ans)
