print("a" < "b")

s = "azcbobobegghakl"
l = 0
ct = 0



while l < len(s):
    if l+1 < len(s):
        if l < l+1:
            ct = 1
            print(s[l]+s[l+1])
    l += 1
print(s)

menor = s.lower()+"a"
print(menor)

lstring = s[0]
slen = 1

for i in range(len(s)):
    for j in range(i,len(s)-1):
            if s[j+1] >= s[j]:
                    if (j+1)-i+1 > slen:
                        lstring = s[i:(j+1)+1]
                        slen = (j+1)-i+1
            else:
                        break

print("Longest substring in alphabetical order is: " + lstring)