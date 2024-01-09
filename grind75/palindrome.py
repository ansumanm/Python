class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_lc = s.lower()

        forward_iter = 0
        backward_iter = len(s_lc) - 1

        while forward_iter < backward_iter:
            if not s_lc[forward_iter].isalnum():
                forward_iter += 1
                continue

            if not s_lc[backward_iter].isalnum():
                backward_iter -= 1
                continue

            if s_lc[forward_iter] != s_lc[backward_iter]:
                return False

            forward_iter += 1
            backward_iter -= 1

        return True
