import sys
f = open('input.txt','r')
sys.stdin = f


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        B = A
        l = 0
        while B != None:
            print(B.val)
            B = B.next

            l+=1
        tmp = A
        cnt = 0
        mid = ceil(l/2)
        stc = []
        while tmp != None:
            if cnt >= mid:
                stc.append(tmp.val)
            cnt+=1
            tmp = tmp.next
                
        cnt = 0
        
        while cnt < mid:
            
            if A.val != stc.pop():
                return 0
            A = A.next
            cnt+=1
        return 1
s = Solution()
node = ListNode(2)
tmp = node
for i in range(2,3):
    newNode = ListNode(i)
    tmp.next = newNode
    tmp = newNode

print(s.lPalin(node))