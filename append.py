s = [1, 2, 2, 3, 4, 4, 5]
res = []
freq = {}

for num in s:
    freq[num] = freq.get(num, 0) + 1

for val in freq:
    if freq[val] > 1:
        res.append(val)

print(res)
