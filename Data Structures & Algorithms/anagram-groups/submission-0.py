class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp={}
        n=[]
        for x in strs:
            dict={}
            for i in x:
                if i in dict:
                    dict[i]+=1
                else:
                    dict[i]=1
            key=tuple(sorted(dict.items()))
            if key in grp:
                grp[key].append(x)
            else:
                grp[key]=[x]
        for i in grp:
            n.append(grp[i])
        return n
