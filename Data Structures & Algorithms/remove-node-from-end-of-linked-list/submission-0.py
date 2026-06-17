class Solution:
    def removeNthFromEnd(self, head, n):

        def get_size(node):
            size = 0
            ptr = node

            while ptr:
                size += 1
                ptr = ptr.next

            return size

        size = get_size(head)

        if size == n:
            return head.next

        ptr = head

        for _ in range(size - n - 1):
            ptr = ptr.next

        ptr.next = ptr.next.next

        return head