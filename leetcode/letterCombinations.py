class Solution:
    """
    Problem: Given a list of strings, for ex. ["abc", "defg", "hij" ..] , generate
    all possible combinations using a character from each list.
    Solution #1: Most simple, using recursion and python generators.
    """
    def generateCombinations(self, strList, index=0, prefix=""):
        if index == len(strList):
            yield prefix
        else:
            for char in strList[index]:
                yield from self.generateCombinations(strList, index + 1, prefix + char)

    """
    Solution #2: Make a list of indices, for [m, n, o, p], where each value is an index
    into the String list. Generate the index for least value and max value, i.e
    [0,0,0,0] to [len(str0) -1, len(str1) -1, ...]. Using this index list, index into 
    each string of the string list and generate the combination.
    This uses a while loop without using recursion.
    """
    def generateIndex(self, max_index_list):
        index_list = [0] * len(max_index_list)

        while True:
            yield index_list
            index = len(index_list) - 1
            while index > -1:
                index_value = index_list[index]
                index_max_value = max_index_list[index]

                if index_value < index_max_value:
                    index_list[index] += 1
                    break
                else:
                    index_list[index] = 0
                    index -= 1


            # Break when all the indices in the index_list are at their max value.
            if all(
                (value == max_index_list[idx]) for idx, value in enumerate(index_list)
            ):
                yield index_list
                return

    def genComb3(self, strList):
        combinations = []
        max_index_list = [(lambda x: len(x) - 1)(x) for x in strList]

        for index_list in self.generateIndex(max_index_list):
            combination = []
            for index, value in enumerate(index_list):
                combination += strList[index][value]

            combinations.append(''.join(combination))

        return combinations

    def genComb2(self, strList):
        combinations = []
        # Maintain an index list, where each index points to the char in the strList
        # index_list = [0 for _ in strList]
        index_list = [0] * len(strList)
        max_index_list = [(lambda x: len(x) - 1)(x) for x in strList]

        # Start incrementing the index from last
        while True:
            combination = ""
            print(index_list)
            for index, value in enumerate(index_list):
                combination += strList[index][value]

            combinations.append(combination)

            # Break when all the indices in the index_list are at their max value.
            if all(
                (value == max_index_list[idx]) for idx, value in enumerate(index_list)
            ):
                break

            # Initialize the index selector to select one from index_list
            index = len(strList) - 1
            while index > -1:
                index_value = index_list[index]
                index_max_value = len(strList[index]) - 1

                if index_value < index_max_value:
                    index_list[index] += 1
                    break
                else:
                    index_list[index] = 0
                    index -= 1

        return combinations

    def letterCombination(self, digits: str):
        digitToStr = {
            "0": "",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        strList = []
        for d in digits:
            strList.append(digitToStr[d])

        if False:
            combinations = []
            for combination in self.generateCombinations(strList):
                combinations.append(combination)

            return combinations
        else:
            return self.genComb3(strList)


def main():
    combinations = []
    strList = ["abc", "def"]

    s = Solution()

    # combinations = []
    # for combination in s.generateCombinations(strList):
    #   combinations.append(combination)

    # print(combinations)

    combinations = s.letterCombination("234")
    print(combinations)


main()
