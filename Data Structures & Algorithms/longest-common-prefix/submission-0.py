class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mlen=len(strs[0])
        res=""
        for i in range (len(strs)):
            if len(strs[i])<mlen:
                mlen=len(strs[i])
        for j in range(mlen):
            for i in range (len(strs)):
                if strs[i][j]!=strs[0][j]:
                    return res
            res+=strs[i][j]
        return res