s = "KAVYA"
res = ""

for char in s:
    if 'A' <= char <= 'Z':
        res += chr(ord(char) + 32)
    else:
        res += char

print(res)
