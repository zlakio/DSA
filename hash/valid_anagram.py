def valid_anagram(s, t):
    map1 = {}
    for ch in s:
        if ch in map1:
            map1[ch] += 1
        else:
            map1[ch] = 1
    if len(s) != len(t):
        return False

    for ch in t:
        if ch not in map1:
            return False
        map1[ch] = map1[ch] - 1
        if map1[ch] < 0:
            return False
    return True


print(valid_anagram("sad", "dad"))
