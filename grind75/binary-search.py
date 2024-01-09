class Solution:
    def search(self, nums: list, target: int) -> int:
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        mid = len(nums) // 2

        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            ret = self.search(nums[:mid], target)
            if ret == -1:
                return -1
            mid = ret
        elif target > nums[mid]:
            ret = self.search(nums[mid:], target)
            if ret == -1:
                return -1
            mid += ret
        return mid


def main():
    s = Solution()

    # nums = list(range(0, 20, 2))
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    # for n in nums:
    #   idx = s.search(nums, n)
    #   if idx != nums.index(n):
    #     print("Fail for target %d actual index %d got %d" % (n, nums.index(n)), idx)
    #   else:
    #     print("PASS: target %d idx %d" % (n, idx))

    idx = s.search(nums, target)
    print("Found index: %d" % idx)


main()
