class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index = 0
        carry = 0
        result = 0
        sumStr = ""
        a_indices = range(len(a) - 1, -1, -1)
        b_indices = range(len(b) - 1, -1, -1)
        
        print(f"aStr: {a} a_indices = {a_indices} bStr: {b} b_indices = {b_indices}")

        while index < len(a) or index < len(b):
            a_bit = a[a_indices[index]] if index < len(a) else "0"
            b_bit = b[b_indices[index]] if index < len(b) else "0"
            
            if carry == 0:
                if a_bit == "1" and b_bit == "1":
                    result = 0
                    carry = 1
                elif a_bit == "0" and b_bit == "0":
                    result = 0
                    carry = 0
                elif (a_bit == "1" and b_bit == "0") or (a_bit == "0" and b_bit == "1"):
                    result = 1
                    carry = 0
            else:  # carry = 1
                if a_bit == "1" and b_bit == "1":
                    result = 1
                    carry = 1
                elif a_bit == "0" and b_bit == "0":
                    result = 1
                    carry = 0
                elif (a_bit == "1" and b_bit == "0") or (a_bit == "0" and b_bit == "1"):
                    result = 0
                    carry = 1
                    
            sumStr = str(result) + sumStr
            index = index + 1

        if carry:
            sumStr = str(carry) + sumStr

        return sumStr


if __name__ == "__main__":
    s = Solution()
    # result = s.addBinary("110010", "100")
    # result = s.addBinary("100", "110010")
    result = s.addBinary("100", "10000")

    print(f"{result}")
