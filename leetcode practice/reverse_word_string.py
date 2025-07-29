class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        break apart the words , space is the breakpoint
        then put the words in a list with reverse order
        join with space
        """
        s = list(filter(lambda a: a != '', s.split(' ')))
        s.reverse()
        s = ' '.join(s)
        return s

        