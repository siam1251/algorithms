class Solution:
	
		
	# @param gas : tuple of integers
	# @param cost : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		total_gas_stations = len(gas)
		#rst = [gas[i] - cost[i] for i in range(len(gas))]
		l = 0
		index = 0
		start = 0
		total_gas = 0
		cur_station = 0
		while l < len(gas):
			total_gas += gas[cur_station]
			if total_gas-cost[cur_station] < 0:
				l = 0
				total_gas = 0
				start = cur_station
				if cur_station >= len(gas)-1:
					return -1
			
			total_gas -= cost[cur_station]
			l+=1
			cur_station = (cur_station+1)%total_gas_stations
			if l == total_gas_stations:
				return index
		return -1


gas =[1, 2]

cost =[2, 1]
s = Solution()
print(s.canCompleteCircuit(gas,cost))



