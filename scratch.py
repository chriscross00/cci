# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem


# Return min substring with all characters
# A initialize 2 pointers
# B increment right until all char encountered
# C increment left until a char not in window, store score l-1 : r as best score
# D repeat until right reaches end of string

def window_solution(string, char_set):
    left, right = 0, 0
    char_encountered = 0
    letter_map = {}
    best_score = float('inf')
    best_substring = []

    # initialize right
    while right < len(string):
        letter_map[string[right]] = letter_map.get(string[right], 0) + 1
        if string[right] in char_set and letter_map[string[right]] == 1:
            char_encountered += 1
        right += 1

    # incrementing left and window
        if char_encountered == len(char_set):
            while char_encountered == len(char_set):
                letter_map[string[left]] -= 1
                if string[left] in char_set and letter_map[string[left]] == 0:
                    char_encountered -= 1
                left += 1

            best_score = min(best_score, right - left + 1)
            best_substring = string[left - 1:right]

    return best_score, best_substring


print(window_solution("ADOBECODEBANC", list('ABC'))) # should be 4
print(window_solution("abc", {'a','b','c'}))
print(window_solution("abweweffawefcaaaaboiwuroqiwuroiueeeb", {'a', 'b','c'}))

# Problem: Given a equation as a string, return whether or not the brackets are
# balanced

# create a stack
# if open bracket push onto stack
# encounter close bracket pop stack
# if does not match return false


def balanced_solution(string):

    stack = []

    for letter in string:
        if open_bracket(letter):
            stack.append(letter)
        elif closed_bracket(letter):
            if len(stack) == 0:
                return False
            temp = stack.pop()
            if not matches(temp, letter):
                return False

    return len(stack) == 0


def open_bracket(letter):
    return letter in ['(', '{', '[']


def closed_bracket(letter):
    return letter in [')', '}', ']']


def matches(open, close):
    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    return bracket_dict[open] == close


print(balanced_solution("(3+9{12+4})(25)")) # true
print(balanced_solution("3+9{12+4})(25)")) # false
