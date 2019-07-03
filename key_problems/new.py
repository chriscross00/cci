# given a string, check if brackets are balanced
# Stack: LIFO
# 1. initialize stack
# 2. iterate through string
# 3. if char in open_bracket dict, push to stack
# 4. if char is in closed_bracket dict, pop from stack
# 5. compare to


def solution(string):

	stack = []
	open_bracket = ['[', '{', '(']
	closed_bracket = [']', '}', ')']

	for char in string:
		if char in open_bracket:
			stack.append(char)
		elif char in closed_bracket:
			if len(stack) == 0:
				return False
			temp = stack.pop()
			if not bracket_match(temp, char):
				return False

	return len(stack) == 0


def bracket_match(open, close):

	mapper = {'{': '}', '[': ']', '(': ')'}
	return mapper[open] == close


print(solution("(3+9{12+4})(25)"))  # true
print(solution("3+9{12+4})(25)"))  # false