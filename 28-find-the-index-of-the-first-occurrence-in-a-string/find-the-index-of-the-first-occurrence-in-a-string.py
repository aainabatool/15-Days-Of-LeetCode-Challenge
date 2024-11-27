class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        import re
        match = re.search(needle, haystack)
        
        if not match:
            return -1
        else: 
            return match.start()
        