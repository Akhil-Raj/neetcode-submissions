class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        def find_combs(curr, ind, candidates, target):
            if target == 0:
                out.append(curr.copy())
                return
            
            if target < 0 or ind >= len(candidates):
                return
            
            # take curr ele
            curr.append(candidates[ind])
            find_combs(curr, ind + 1, candidates, target - candidates[ind])
            curr.pop()

            # skip all dup eles
            while ind < len(candidates) - 1 and candidates[ind] == candidates[ind + 1]:
                ind = ind + 1
            
            find_combs(curr, ind + 1, candidates, target)
        
        find_combs([], 0, candidates, target)

        return out