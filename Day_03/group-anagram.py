class Solution(object):
    def groupAnagrams(self, strs):
        dictionary = {}
        for i in strs:
            arr = [0]*26
            for j in i:
                arr[ord(j)-ord('a')]+=1 
            ke_val = tuple(arr)
            if ke_val not in dictionary:
                dictionary[ke_val]=[]
            dictionary[ke_val].append(i)
        return list(dictionary.values())        