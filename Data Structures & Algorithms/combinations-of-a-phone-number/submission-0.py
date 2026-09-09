class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = []
        mapping = {"2" : 'abc', "3" : 'def', "4" : 'ghi', "5" : 'jkl', "6" : 'mno', "7" : 'pqrs', "8" : 'tuv', "9" : 'wxyz'}

        def find_combs(digits, ind, curr):
            if ind == len(digits):
                if curr != "":
                    out.append(curr)
                return
            for char in mapping[digits[ind]]:
                find_combs(digits, ind + 1, curr + char)

        find_combs(digits, 0, "")

        return out