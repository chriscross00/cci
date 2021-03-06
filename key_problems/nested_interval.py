# Problem: Given a equation as a string, return whether or not the brackets are
# balanced
#
# Approach
# A Initialize empty stack
# B While iterating over list, push open brackets onto stack
# C If a closing bracket is encountered, compare item popped from stack to
# closing bracket
# D If C is never violated and the stack is empty return True, else return False
# 
# Time: O(n)
# Space: n
# https://www.geeksforgeeks.org/merging-intervals/
# https://www.leetfree.com/problems/non-overlapping-intervals.html
# https://www.glassdoor.com/Interview/Recently-I-attended-the-interview-at-Google-and-I-was-asked-You-are-given-a-sorted-list-of-disjoint-intervals-and-an-inter-QTN_345488.htm


def solution(string):

	stack = []
	
	for letter in string:
		if open_bracket(letter):
			stack.append(letter)
		elif close_bracket(letter):
			if len(stack) == 0:
				return False
			temp = stack.pop()
			if not match(temp, letter):
				return False
				
	return len(stack) == 0	
		
		
def open_bracket(letter):
	return letter in ('{', '[', '(')


def close_bracket(letter):
	return letter in ('}', ']', ')')


def match(open, close):
	mapper = {'{': '}', '[': ']', '(': ')'}
	return mapper[open] == close

	
#print(solution('aff2bb'))  # false
print(solution("(3+9{12+4})(25)"))  # true
print(solution("3+9{12+4})(25)"))  # false
