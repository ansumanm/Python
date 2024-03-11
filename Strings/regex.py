class Solution:
	def isMatch1(self, s: str, p: str) -> bool:
		# Regex rules:
		# . matches any single character
		# * matches any number of preceding character
		
		s_index = 0
		p_index = 0
		match = True

		while p_index < len(p) and s_index < len(s):
			if p_index < (len(p) - 1) and p[p_index + 1] == '*':
				# Special processing
				if p[p_index] == '.':
					# Special case: .*
					# If there is a character after * in the pattern string
					# We need to consume all the characters till we hit that character
					# for example: .*b will match ab and acb but will not match abb
					if (p_index + 1) < (len(p) - 1):
						# Case: .*x
						endChar = p[p_index + 2]
						# Match all till we find endChar
						while s_index < len(s) and s[s_index] != endChar:
							s_index += 1

						if s_index == len(s):
							# Mismatch
							match = False
							break

						# Increase the p_index and s_index and continue
						p_index += 3 # 3 because . * endChar
						s_index += 1

						continue
					else:
						# Case: .*  
						# .* is the last character so everything match. Return true
						return True
				else:
					# Case: a*
					while s_index < len(s) and s[s_index] == p[p_index]:
						s_index += 1
					# Case a*a : Reduce it to a* by incrementing the p_index by 1
					if (p_index + 2) < len(p) and p[p_index] == p[p_index + 2]:
						p_index += 1
					p_index += 2
			else:
				if p[p_index] == '.' or p[p_index] == s[s_index]:
					s_index += 1
					p_index += 1
				else:
					match = False
					break
		# Now we have come out of the while loop. 
		if match == True:
			# if s is completely processed, but p is not and vice versa, then its not a match
			if (p_index >= len(p) and s_index < len(s)) or (s_index >= len(s) and p_index < len(p)):
				match = False
    
		return match

	def isMatch(self, s: str, p: str) -> bool:
		"""
        dp[i][j] is a 2D list (a list of lists) where dp[i][j] is True if the first i characters of s match the first j characters of p. The dimensions of dp are (len(s) + 1) x (len(p) + 1) to account for the case where either or both the string and the pattern are empty.
		The algorithm initializes the first row of dp based on patterns that consist of elements followed by *, since * can match zero instances of the preceding element.
		It then iterates over each character in s and p, updating dp based on whether characters match directly, match any character (.), or match zero or more of the preceding elements (*).

		Args:
			s (str): String
			p (str): Pattern

		Returns:
			bool: True if matches else False.
		"""
		dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
  
		# print(dp, len(dp), len(dp[0]))
		for row in dp:
			print(row, len(row))
		print("--------------------------------------")
		
		# Empty string and empty pattern are a match
		dp[0][0] = True
		
		for row in dp:
			print(row, len(row))
		print("--------------------------------------")

		# Handle patterns like a*, a*b*, a*b*c* etc.
		for i in range(1, len(p) + 1):
			if p[i-1] == '*':
				dp[0][i] = dp[0][i-2]
		
		for row in dp:
			print(row, len(row))
		print("--------------------------------------")
  
		for i in range(1, len(s) + 1):
			for j in range(1, len(p) + 1):
				if p[j-1] == '.' or p[j-1] == s[i-1]:
					dp[i][j] = dp[i-1][j-1]
				elif p[j-1] == '*':
					dp[i][j] = dp[i][j-2]  # Match 0 time
					if p[j-2] == '.' or p[j-2] == s[i-1]:
						dp[i][j] = dp[i][j] or dp[i-1][j]  # Match 1 or more times

		for row in dp:
			print(row, len(row))
		print("--------------------------------------")
  
		return dp[-1][-1]


if __name__ == "__main__":
	s = Solution()
	# print(f"s = aa, p = a match: {s.isMatch('aa', 'a')}")  
	# print(f"s = aa, p = a* match: {s.isMatch('aa', 'a*')}")  
	# print(f"s = ab, p = .* match: {s.isMatch('ab', '.*')}")  
	# print(f"s = aab, p = c*a*b match: {s.isMatch('aab', 'c*a*b')}")
	# print(f"s = ab, p = .*c match: {s.isMatch('ab', '.*c')}")
	# print(f"s = aaa, p = aaaa match: {s.isMatch('aaa', 'aaaa')}")
	# print(f"s = aaa, p = a*a match: {s.isMatch('aaa', 'a*a')}")
	print(f"s = aaa, p = ab*a*c*a match: {s.isMatch('aaa', 'ab*a*c*a')}")
