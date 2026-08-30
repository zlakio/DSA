def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    s = {}
    for word in strs:
        key = "".join(sorted(word))
        s.setdefault(key, []).append(word)

    return s.values()
