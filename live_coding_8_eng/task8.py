#class Solution:

def longestCommonPrefix(strs: list[str]) -> str:
    min_len = min([len(s) for s in strs])

    result_s = ''

    for i in range(0, min_len):
        temp_s = strs[0][i]
        for s in strs:
            if temp_s != s[i]:
                return result_s
        else:
            result_s += temp_s

    return result_s

if __name__ == '__main__':
    assert longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ''
    assert longestCommonPrefix(["flower", "flow"]) == 'flow'
    assert longestCommonPrefix(["dod", "did"]) == 'd'

# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

