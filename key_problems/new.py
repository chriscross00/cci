def solution(str, set):

	# variables
	left, right = 0, 0
	letter_map = {}
	char_encountered = 0
	best_score = float('inf')
	
	# large set
	while left < len(str) and right < len(str):
		letter_map[str[right]] = letter_map.get(str[right], 0) + 1
		if letter_map[str[right]] == 1 and str[right] in char_set:
			char_encountered += 1
		right += 1
		# min set
		if len(letter_map) == char_encountered:
			while len(letter_map) == char_encountered:
				letter_map[str[left]] -= 1
				if letter_map[str[left]] == 0 and str[left] in char_set:
					char_encountered -= 1
				left += 1
			# best_score
			best_score = min(best_score, right - left + 1)
	
	# return
	return best_score
	
	
def bracket_solution(str):

	stack = []
	
	for letter in str:
		if open_bracket(letter):
			stack.append(letter):
			
		elif closed_bracket(letter):
			if len(stack) == 0:
				return False
			temp = stack.pop()
			if not matches(temp, letter):
				return False
				
	return len(stack) == 0
			
			
def open_bracket(letter):
	return letter in ('[', '{', '(')
	
def closed_bracket(letter):
	return letter in (']', '}', ')')
	
	
def matches(open, close):
	match_dict = {'{': '}', '[': ']', '(': ')'}
	return match_dict[open] == close
	
	