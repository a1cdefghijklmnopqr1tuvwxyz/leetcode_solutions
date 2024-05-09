class Solution:

    def commonPrefix(self, word1,word2):
        prefix = ""
        for i in range(min(len(word1),len(word2))):
            if word1[i] == word2[i]:
                prefix += word1[i]
            else : 
                break

        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for w in strs:
            for u in strs:
                common_prefix = self.commonPrefix(u, w)
                if common_prefix == "":
                    return ""
                if len(common_prefix) < len(prefix):
                    prefix = common_prefix
        return prefix
