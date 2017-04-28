class Solution:
    def isIsomorphic(self, s, t):
        check_index = []
        counter = 0
        ref = len(s)
        while counter != ref:
            repeat_index = [i for i, x in enumerate(s) if x == s[counter]]
            repeat_index2 = [j for j, k in enumerate(t) if k == t[counter]]
            if repeat_index != repeat_index2:
                return False
            counter += 1
        return True
