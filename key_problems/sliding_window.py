# Problem: Given a string and set of characters find smallest substring that contains all the characters.
# Approach:
# A. Initialize 2 pointers: left and right
# B. Increment right until all characters in set encountered
# C. Increment left until a required character not in window. Minimized substring is now left-1 : right, store in variable.
# D. Repeat B and C until right reaches end of list
#
# Time: O(n)
# Space: n


def solution(string, char_set):

	if len(string) == 0:
		return None
	if len(char_set) == 0:
		return None
	
	# Initializing variables
	left, right = 0, 0
	letter_map = {}
	char_encountered = 0
	best_score = float('inf')
	
	# Finding all characters in char_set 
	while left < len(string) and right < len(string):
		letter_map[string[right]] = letter_map.get(string[right], 0) + 1
		if letter_map[string[right]] == 1 and string[right] in char_set:
			char_encountered += 1
		right += 1
		
		# Minimizing substring
		if char_encountered == len(char_set):
			while char_encountered == len(char_set):
				letter_map[string[left]] -= 1
				if letter_map[string[left]] == 0 and string[left] in char_set:
					char_encountered -= 1
				left += 1
			best_score = min(best_score, right - left + 1)
	return best_score

	
print(solution("adddddbcbba", {'a','b','c'}))
print(solution("abc", {'a','b','c'}))
print(solution('af', {}))