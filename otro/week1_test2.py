s2 = "ybobbpbobobobobxboaobobbobbtbobbevioboob"
cuento = 0
s3 = ""
l = 0

while l < len(s2):

    if l+2 < len(s2):
        if s2[l] == 'b' and s2[l + 1] == 'o' and s2[l + 2] == 'b':
            print(s2[l])
            cuento += 1
    l += 1

print("Number of times bob occurs is: ", cuento)