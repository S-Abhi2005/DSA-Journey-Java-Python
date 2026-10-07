class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        sign = ""
        if num < 0:
            sign = "-"
            num = -num

        res = ""

        while num != 0:
            total = num % 7
            res += str(total)
            num = num // 7

        return sign + res[::-1]