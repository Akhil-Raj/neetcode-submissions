class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pal_dict = {}

        def find_pals(ind, s, k):
            while ind - k >= 0 and ind + k < len(s):
                if s[int(ind - k)] == s[int(ind + k)]:
                    pal_dict.setdefault(int(ind - k), []).append(int(ind + k))
                    k += 1
                else:
                    return

        for ind in range(len(s)):
            find_pals(ind, s, 0)
        
        ind = 0.5
        while(ind < len(s)):
            find_pals(ind, s, 0.5)
            ind += 1

        out = []
        # print(pal_dict)
        def find_subs(ind, curr):
            if ind == len(s):
                out.append(curr.copy())
                return

            for end_ind in pal_dict.get(ind, []):
                curr.append(s[ind : end_ind + 1])
                find_subs(end_ind + 1, curr)
                curr.pop()

        find_subs(0, [])

        return out