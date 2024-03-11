from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Special case
        # if len(strs) == 1:
        #    return strs[0]

        stringLengths = [len(s) for s in strs]
        minLength = min(stringLengths)
        minIndex = stringLengths.index(minLength)
        smallStr = strs[minIndex]

        for index in range(minLength - 1, -1, -1):
            prefix = smallStr[0 : index + 1]

            if all((s.find(prefix) == 0) for s in strs):
                return prefix

        # Could not find a common prefix
        return ""
