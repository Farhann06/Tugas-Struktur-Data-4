    def __iadd__(self, other):
        return self.add(other)

    def __isub__(self, other):
        result = int(self.toString()) - int(other.toString())
        return BigInteger(str(result))

    def __imul__(self, other):
        result = int(self.toString()) * int(other.toString())
        return BigInteger(str(result))

    def __ifloordiv__(self, other):
        result = int(self.toString()) // int(other.toString())
        return BigInteger(str(result))

    def __imod__(self, other):
        result = int(self.toString()) % int(other.toString())
        return BigInteger(str(result))

    def __ipow__(self, other):
        result = int(self.toString()) ** int(other.toString())
        return BigInteger(str(result))