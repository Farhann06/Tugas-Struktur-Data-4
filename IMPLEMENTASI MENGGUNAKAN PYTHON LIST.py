class BigInteger:
    def __init__(self, value="0"):
        self.digits = [int(d) for d in value]

    def toString(self):
        return ''.join(map(str, self.digits))

    def compare(self, other):
        return int(self.toString()) - int(other.toString())

    def add(self, other):
        a = self.digits[::-1]
        b = other.digits[::-1]

        result = []
        carry = 0

        for i in range(max(len(a), len(b))):
            d1 = a[i] if i < len(a) else 0
            d2 = b[i] if i < len(b) else 0

            total = d1 + d2 + carry
            result.append(total % 10)
            carry = total // 10

        if carry:
            result.append(carry)

        return BigInteger(''.join(map(str, result[::-1])))