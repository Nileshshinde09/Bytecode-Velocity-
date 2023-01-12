import streamlit as st
def snippet(year):
    if '1' in year:
        return '''
class Solution(object):
    pairs = {')': '(',
             '}': '{',
             ']': '['}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
if __name__=="__main__":
    case1 = "()"
    case2 = "()[]{}"
    case3 = "(]"
    s1 = Solution()
    print(s1.isValid(case1))
    print(s1.isValid(case2))
    print(s1.isValid(case3))
    '''
    if '2' in year:

            return '''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

if __name__=="__main__":   
    solution = Solution()
    case1 ="Hello World"
    case2 = "   fly me   to   the moon  "
    case3 = "luffy is still joyboy"
    print(solution.lengthOfLastWord(case1))
    print(solution.lengthOfLastWord(case2))
    print(solution.lengthOfLastWord(case3))
        '''

    if '3' in year:
            return '''
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
if __name__=="__main__":
    case1 = ["flower","flow","flight"]
    case2 = ["dog","racecar","car"]
    print(longestCommonPrefix(case1))
    print(longestCommonPrefix(case2))

    '''
