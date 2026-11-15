#this is actually day 6 sorry got a  little behind due to festive season so had to come back with
# a palindrome linkedList problem

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

class Solution:

    def isPlaindromeCheck(self, head:ListNode | None) -> bool:
        slow = head
        fast = head

        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next

        #reverse the middle node and reverse the pointers

        prev = None

        while slow:
            temp = slow.next

            slow.next = prev

            prev = slow

            slow = temp

        left = head
        right = prev

        while right:
            if left is None or left.val != right.val:
                return False

            left = left.next
            right = right.next
        return True

exLinkedList = [1,2,2,1]
exLinkedList = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

ex2LinkedList = ListNode(1, ListNode(2))

confirmPalindrome = Solution()

print(confirmPalindrome.isPlaindromeCheck(exLinkedList))
print(confirmPalindrome.isPlaindromeCheck(ex2LinkedList))

class SecondSolution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotatedNum = {
            '0' : '0',
            '1' : '1',
            '6' : '9',
            '8' : '8',
            '9' : '6'}
        left = 0
        right = len(num) - 1
        while left <= right:
            if rotatedNum[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True

test1 = "69"

verifyStrobogrammatic = SecondSolution()
print(verifyStrobogrammatic.isStrobogrammatic(test1))
        
