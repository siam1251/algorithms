class Solution:
	def getChars(self,s):
		codes = ['0','1','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
		return codes[int(s)]

	# @param A : string
	# @return a list of strings
	def letterCombinations(self, A):
		if len(A) == 0:
			return ['']
		rt_str = self.letterCombinations(A[1:])
		st = ''
		cur_chars = self.getChars(A[0])
		cur_combinations = []
		for i in cur_chars:
			for rt_comb in rt_str:
				cur_combinations.append(i+rt_comb)
		return cur_combinations

s = Solution()
A = '234'
print(s.letterCombinations(A))