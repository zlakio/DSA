# mapping characters to different index
# ch-'a' = index of that character
s = "apple"

hash = [0] * 26

for ch in s:
    hash[ord(ch) - ord("a")] += 1

print(hash)
