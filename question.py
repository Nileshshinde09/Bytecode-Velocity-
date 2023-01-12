import streamlit as st
def question(year):
    if '1' in year:
        st.header(
        '''
            Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
            An input string is valid if:

            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.
            

            Example 1:

            Input: s = "()"
            Output: true
            Example 2:

            Input: s = "()[]{}"
            Output: true

        '''
        )
    if '2' in year:
            st.header(
            '''
                Given a string s consisting of words and spaces, return the length of the last word in the string.

                A word is a maximal 
                substring
                consisting of non-space characters only.

                

                Example 1:

                Input: s = "Hello World"
                Output: 5
                Explanation: The last word is "World" with length 5.
                Example 2:

                Input: s = "   fly me   to   the moon  "
                Output: 4
                Explanation: The last word is "moon" with length 4.
            '''
            )
    if '3' in year:
            st.header(
            '''
                Write a function to find the longest common prefix string amongst an array of strings.

                If there is no common prefix, return an empty string "".

                

                Example 1:

                Input: strs = ["flower","flow","flight"]
                Output: "fl"
                Example 2:

                Input: strs = ["dog","racecar","car"]
                Output: ""
                Explanation: There is no common prefix among the input strings.

                '''
            )
