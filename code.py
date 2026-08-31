class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        e=set(allowed)
        c=0
        for word in words:
            g=True
            for wo in word:
                if wo not in e:
                    g=False
                    break
            if g:
                c+=1
                print(c)

        return c
        
