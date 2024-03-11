from typing import Tuple


def lengthOfLongestSubstring(s: str) -> Tuple[int, str]:
    charMap = {}

    maxl = 0
    maxsubstr = ""
    substr = ""
    count = 0
    index = 0

    while index < len(s):
        c = s[index]

        if c in charMap.keys():
            # Duplicate character detected.
            if count > maxl:
                maxsubstr = substr

            maxl = max(maxl, count)

            # Reset the index
            index = charMap[c]
            count = 0
            substr = ""
            charMap = {}
        else:
            # Store the character and its index.
            charMap[c] = index
            count += 1
            substr = substr + c

        index += 1

    if count > maxl:
        maxsubstr = substr

    maxl = max(maxl, count)
    return maxl, maxsubstr


def LS(s: str) -> int:
    substr = ""
    maxSubstr = ""

    for index in range(0, len(s)):
        # print(f"index: {index} substr: {substr}")
        c = s[index]

        if c in substr:
            if len(substr) > len(maxSubstr):
                maxSubstr = substr

            # Find the index of c in substr
            cIndex = substr.find(c)
            substr = substr[cIndex + 1:]
            print(f"char {c} cIndex: {cIndex} substr: {substr}")

        substr = substr + c

    if len(substr) > len(maxSubstr):
        maxSubstr = substr

    return maxSubstr


if __name__ == "__main__":
    # maxl, maxSubstr = lengthOfLongestSubstring("abcabcdeab")
    # print(maxl, maxSubstr)

    # maxl, maxSubstr = lengthOfLongestSubstring("abcabcdefghijkabcdefghi")
    # print(maxl, maxSubstr)

    # maxSubstr = LS('abcabcdefghijkabcdefghi')
    # print(f"{maxSubstr} {len(maxSubstr)}")

    # maxSubstr = LS('abcdabc')
    # print(f"{maxSubstr} {len(maxSubstr)}")

    maxSubstr = LS("dvdf")
    print(f"{maxSubstr} {len(maxSubstr)}")
