s = "eat"
r = "ate"

def anagrame(s, r):
    if len(s) != len(r):
        return "not anagram"
    
    for char in s:
        if char not in r:
            return False
    
    return True

print(anagrame(s, r))
