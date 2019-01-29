class Heap:
	def __init__(self,list):
		self.list = list
		self.currentSize = len(list)-1

	def percUp(self, i):
		while i > 1:
			if self.heapList[i//2] < self.heapList[i]:
				tmp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i//2
	def getMin(self,i):
		if 2*i+1 > self.currentSize:
			return 2*i
		else:
			if self.heapList[2*i] < self.heapList[2*i+1]:
				return 2*i
			else:
				return 2*i+1

	def insert(self,i):
		self.heapList.append(i)
		self.currentSize += 1
		self.percUp(len(self.heapList)-1)
	def percDown(self,i):
		while 2*i <= self.currentSize:
			smallest = self.getMin(i)
			if self.heapList[i] > self.heapList[smallest]:
				#parent will be smaller than children
				tmp = self.heapList[smallest]
				self.heapList[smallest] = self.heapList[i]
				self.heapList[i] = tmp
			i = 2*i


	def buildHeap(self):
		lastParent = len(self.list)//2
		self.heapList = [0] + self.list
		for i in range(lastParent,0,-1):
			self.percDown(i)
	def sort(self):
		self.buildHeap()
		for i in range(len(self.heapList)-1,0,-1):
			self.currentSize = i-1
			tmp = self.heapList[1]
			self.heapList[1] = self.heapList[i]
			self.heapList[i] = tmp
			self.percDown(1)

heap = Heap([3,1,2,4,6,2])
heap.sort()
print(heap.heapList)
heap.insert(10)
print(heap.heapList)