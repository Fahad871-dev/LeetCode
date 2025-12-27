class Solution:
    def SortString(sels,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for s in strs:
            key=self.SortString(s)     #sort current s to make key
            if key in dict1:           #if the key is in dict
                dict1[key].append(s)   #append current s in that key
            else:
                dict1[key]=[s] #if not then save new key for values

        return list(dict1.values())       



        