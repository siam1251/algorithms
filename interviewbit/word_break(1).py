class Solution:

	def sentences(self,i):
		if len(self.A) <= 0 or i >= len(self.A):
			return ['']
		if len(self.results[i])>0:
			return self.results[i]
		lst = []
		for j in range(i,len(self.A)):
			if self.A[i:j+1] in self.B:
				ret_lst = self.sentences(j+1)
				for l in ret_lst:
					lst.append(self.A[i:j+1]+' '+l)
		self.results[i] = lst
		return lst



	# @param A : string
	# @param B : list of strings
	# @return a list of strings
	def wordBreak(self, A, B):
		self.results = ['' for i in range(len(A))]
		self.A = A
		self.B = B
		rst = self.sentences(0)
		rst = [i.strip() for i in rst]

		return rst
		
s = Solution()
print(s.wordBreak('catsanddog',['cat','cats','sand','and','dog']))

