def logngest_common_prefix(strs: list) -> str:
    if not strs:
        return ""
    
    for i, chars in enumerate(zip(*strs)):
        if len(set(chars)) > 1:
            return strs[0][:i]
    return strs[0]

if __name__ == "__main__":
    list_strss = [["flower","flow","flight"], ["dog","racecar","car"]]
    for strs in list_strss:
        result = logngest_common_prefix(strs)
        print(f"{strs} of {result}")