class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None


class BigInteger:
    def __init__(self, initValue="0"):
        self.head = None
        for d in reversed(initValue):
            self._add_digit(int(d))

    def _add_digit(self, digit):
        new_node = Node(digit)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def toString(self):
        digits = []
        temp = self.head
        while temp:
            digits.append(str(temp.digit))
            temp = temp.next
        return ''.join(reversed(digits))

    def compare(self, other):
        return int(self.toString()) - int(other.toString())

    def add(self, other):
        result = ""
        carry = 0

        a = self.toString()[::-1]
        b = other.toString()[::-1]

        for i in range(max(len(a), len(b))):
            d1 = int(a[i]) if i < len(a) else 0
            d2 = int(b[i]) if i < len(b) else 0

            total = d1 + d2 + carry
            result += str(total % 10)
            carry = total // 10

        if carry:
            result += str(carry)

        return BigInteger(result[::-1])