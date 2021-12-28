#19101185 강동현 - 3001 Caesar Cipher

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a,b = input().split()
b = int(b)
a = list(a)
ans = []
for i in a:
    ii = alpha.index(i)
    ans.append(alpha[(ii-b)%26])
for i in range(0,len(ans)-1):
    print(ans[i],end="")
print(ans[len(ans)-1])