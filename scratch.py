# Return min substring with all characters
# A initialize 2 pointers
# B increment right until all char encountered
# C increment left until a char not in window, store score l-1 : r as best score
# D repeat until right reaches end of string

def window_solution(string, char_set):
    left, right = 0, 0
    best_score = float('inf')
    best_substring = []
    char_encountered = 0
    letter_map = {}

    while right < len(string):
        letter_map[string[right]] = letter_map.get(string[right], 0) + 1
        if letter_map[string[right]] == 1 and string[right] in char_set:
            char_encountered += 1
        right += 1

        if char_encountered == len(char_set):
            while char_encountered == len(char_set):
                letter_map[string[left]] -= 1
                if letter_map[string[left]] == 0 and string[left] in char_set:
                    char_encountered -= 1
                left += 1
            best_score = min(best_score, right - left + 1)
    return best_score



print(window_solution("abdddddcbeba", {'a', 'b', 'c'}))
print(window_solution("abweweffawefcaaaaboiwuroqiwuroiueeeb", {'a', 'b', 'c'}))

