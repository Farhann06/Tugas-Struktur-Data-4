class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None


# ==============================
# LINKED LIST IMPLEMENTATION
# ==============================
class BigIntegerLinkedList:
    def __init__(self, value="0"):
        self.head = None
        for d in reversed(value):
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

        return BigIntegerLinkedList(result[::-1])

    def __iadd__(self, other):
        return self.add(other)


# ==============================
# LIST IMPLEMENTATION
# ==============================
class BigIntegerList:
    def __init__(self, value="0"):
        self.digits = [int(d) for d in value]

    def toString(self):
        return ''.join(map(str, self.digits))

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

        return BigIntegerList(''.join(map(str, result[::-1])))

    def __iadd__(self, other):
        return self.add(other)


# ==============================
# OPERATOR TAMBAHAN (UMUM)
# ==============================
def subtract(a, b):
    return str(int(a) - int(b))

def multiply(a, b):
    return str(int(a) * int(b))

def divide(a, b):
    return str(int(a) // int(b))

def mod(a, b):
    return str(int(a) % int(b))

def power(a, b):
    return str(int(a) ** int(b))


# ==============================
# TEST / DEMO
# ==============================
if __name__ == "__main__":
    print("=== LINKED LIST ===")
    a = BigIntegerLinkedList("12345")
    b = BigIntegerLinkedList("6789")
    c = a.add(b)
    print("12345 + 6789 =", c.toString())

    print("\n=== LIST ===")
    x = BigIntegerList("99999")
    y = BigIntegerList("1")
    z = x.add(y)
    print("99999 + 1 =", z.toString())

    print("\n=== OPERATOR TAMBAHAN ===")
    print("Pengurangan:", subtract("1000", "250"))
    print("Perkalian:", multiply("123", "45"))
    print("Pembagian:", divide("100", "5"))
    print("Modulus:", mod("100", "3"))
    print("Pangkat:", power("2", "10"))