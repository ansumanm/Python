class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Convert to lists
        ls = list(s)
        lt = list(t)

        for m in lt:
            if m not in ls:
                return False

            ls.remove(m)

        if len(ls) > 0:
            return False

        return True
