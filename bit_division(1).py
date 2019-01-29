class Solution:
    # @param div : integer
    # @param sor : integer
    # @return an integer
    def divide(self, dividend, divisor):
        cnt = 0
        rt = 0
        m = -1 if dividend*divisor < 0 else 1
        div = abs(dividend)
        sor = abs(divisor)
        while div>= sor:
            #for each bit
            cnt = 0
            while div >= sor <<cnt:
                cnt += 1
            
            rt += 1<<(cnt-1)
            div -= sor<<(cnt-1)
        if dividend == -2147483648 and divisor == -1:
        	return 2147483647
        return rt*m
