class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = ""
        strs.sort()
        flag = 0
        str1 = strs[0]
        str2 = strs[len(strs)-1]
        index = 0
        while index < len(str1):
            if str1[index] == str2[index]:
                index += 1
                flag = 1
            else:
                break
                
        if flag == 1:
            return str1[0:index]
        else:
            return a