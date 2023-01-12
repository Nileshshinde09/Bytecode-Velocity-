'''
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


'''
class Solution(object):
    pairs = {')': '(',
             '}': '{',
             ']': '['}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c not in self.pairs:
                stack.append(c)
            else:
                if not stack or stack[-1] != self.pairs[c]:
                    return False
                stack.pop()
        return not stack
if __name__=="__main__":
    case1 = "()"
    case2 = "()[]{}"
    case3 = "(]"
    s1 = Solution()
    print(s1.isValid(case1))
    print(s1.isValid(case2))
    print(s1.isValid(case3))
'''


# def longestCommonPrefix(strs):
#     i=0
#     for x in zip(*strs):            
#         if len(set(x)) > 1: return strs[0][:i]            
#         i += 1            
#     return strs[0][:i] if strs else ''
# if __name__=="__main__":
#     case1 = ["flower","flow","flight"]
#     case2 = ["dog","racecar","car"]
#     print(longestCommonPrefix(case1))
#     print(longestCommonPrefix(case2))






# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if (len(s) == 0):
#             return 0
#         s = s.strip() 
#         l = s.split(" ")
#         return len(l[-1])

# if __name__=="__main__":   
#     solution = Solution()
#     case1 ="Hello World"
#     case2 = "   fly me   to   the moon  "
#     case3 = "luffy is still joyboy"
#     print(solution.lengthOfLastWord(case1))
#     print(solution.lengthOfLastWord(case2))
#     print(solution.lengthOfLastWord(case3))

