class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for word in strs:
            sorted_key = ''.join(sorted(word))
            if sorted_key in anagrams:
                anagrams[sorted_key].append(word)
            else:
                anagrams[sorted_key] = [word]
        return anagrams.values()
