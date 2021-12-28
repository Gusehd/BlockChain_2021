#19101185 강동현 - 3013 Toy Cipher

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

sbox = [

232, 226,  52, 242, 220, 198, 199, 237,  57, 164,   0,  63,  70, 211, 222, 137,

62,   59,   2, 171,  77,  12,  71, 177,  83,   7, 102,  64,  75, 170, 153,  98,

190,  36, 241, 154, 238,  39,  30, 244, 172,  50,  73,  82,  87, 145, 181, 176,

245, 125,  31, 173, 253,  27,  17, 138, 122, 135,   5, 156, 113,  28, 118, 105,

107, 168,   3, 225, 217, 243, 229,  19,  20,  18, 223, 109, 108, 123,  78,  96,

208,  14, 130, 240,  97, 104, 174,  88,  58, 103, 194, 110,  81,  94,  43,  49,

114, 139,  44, 132, 115, 142, 140, 106, 197, 169, 117,  24, 165,  29,  41, 188,

162, 134,  15, 191, 157, 163, 231, 207,  46,  10,   8, 116,  23, 111,  74,  25,

206,  99,   1,  11, 175, 246,  45, 200, 192,  60, 189,  90, 148, 143,  40,   6,

69,  218, 121,  26, 100,  80, 152, 250, 179, 228, 214, 161,  34, 203, 213, 193,

89,  204,  21, 221, 205, 233,  76, 249, 230,  51, 227, 147,  53, 149, 182, 196,

9,    72,  47,  48, 248, 186, 167,  66, 202, 160, 183,  95,  79,  91,  32, 234,

68,   85,  22,  67, 239, 120, 180, 150, 201, 124, 184, 178, 235,  93, 252, 216,

127, 101,  54, 158,  55,  33, 128, 136,  61,  92,  56, 255, 187,  84, 254, 126,

159, 185, 236, 151, 247, 141,  16, 251,  65, 209, 131, 166,   4,  35, 215, 133,

146, 144, 224, 119,  37,  38,  86, 212, 210, 129,  13,  42, 155, 112, 219, 195

]

plain = input()
key = input()

key_num =  int("0x" + key , 16)
key_bin = bin(key_num).replace("0b","")
if len(key_bin) < 32:
    key_bin = "0"*(32-len(key_bin)) + key_bin

plain_num =  int("0x" + plain , 16)
plain_bin = bin(plain_num).replace("0b","")
if len(plain_bin) < 32:
    plain_bin = "0"*(32-len(plain_bin)) + plain_bin


rr_bit = right(plain_bin,14) # 타임 인자는 돌려보면서 어떤 수인지 찾기 / 14로 나옴

rr_hex_bit = hex(int("0b" + rr_bit , 2)).replace("0x","")
if len(rr_hex_bit) < 8:
    rr_hex_bit = "0"*(8-len(rr_hex_bit)) + rr_hex_bit

hex_bit_1 = hex(sbox[int("0x"+rr_hex_bit[0:2],16)]).replace("0x","")
hex_bit_2 = hex(sbox[int("0x"+rr_hex_bit[2:4],16)]).replace("0x","")
hex_bit_3 = hex(sbox[int("0x"+rr_hex_bit[4:6],16)]).replace("0x","")
hex_bit_4 = hex(sbox[int("0x"+rr_hex_bit[6:8],16)]).replace("0x","")

if len(hex_bit_1) < 2:
    hex_bit_1 = "0"*(2-len(hex_bit_1)) + hex_bit_1
if len(hex_bit_2) < 2:
    hex_bit_2 = "0"*(2-len(hex_bit_2)) + hex_bit_2
if len(hex_bit_3) < 2:
    hex_bit_3 = "0"*(2-len(hex_bit_3)) + hex_bit_3
if len(hex_bit_4) < 2:
    hex_bit_4 = "0"*(2-len(hex_bit_4)) + hex_bit_4

last_bit = bin(int("0x" + hex_bit_1 + hex_bit_2 + hex_bit_3 + hex_bit_4 , 16)).replace("0b","")
if len(last_bit) < 32:
    last_bit = "0"*(32-len(last_bit)) + last_bit

ans_bit = xor(last_bit,key_bin)
ans_hex_bit = hex(int("0b"+ans_bit,2)).replace("0x","")

if len(ans_hex_bit) < 8:
    ans_hex_bit = "0"*(8-len(ans_hex_bit)) + ans_hex_bit
print(ans_hex_bit)