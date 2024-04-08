# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = []
        carry_next = 0 
        lenth_range = max(len(l1), len(l2))
        for i in range(lenth_range+1):
            l1_value = l1[i:i+1][0] if l1[i:i+1] else 0
            l2_value = l2[i:i+1][0] if l2[i:i+1] else 0
            sum_value = l1_value + l2_value + carry_next
            if sum_value >= 10:
                carry_next = int(str(sum_value)[:-1])
                result_list.append(int(str(sum_value)[-1]))
                continue

            result_list.append(sum_value)
        return result_list


if __name__ == "__main__":
    #l1, l2 = [2,4,3], [5,6,4]
    l1, l2 = [9,9,9,9,9,9,9], [9,9,9,9]
    solution_obj = Solution()
    result = solution_obj.addTwoNumbers(l1, l2)
    print(f"Result: {result}")