word="studying"
result=""
for ch in word:
    if ch not in "aeiouAEIOU":
        result+=ch
print(result)
